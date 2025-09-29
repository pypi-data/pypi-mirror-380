# tests/test_benchmark.py
import sys
import pickle
import numpy as np
import pytest

from inatinqperf.benchmark import benchmark
from inatinqperf.utils.embed import ImageDatasetWithEmbeddings


# ---------- Safe dummy backend ----------
class DummyBE:
    def __init__(self, dim, metric, **params):
        self.inited = True
        self.trained = False
        self.dim = dim
        self.metric = metric
        self.params = params
        self.ntotal = 0
        self.init_args = {"dim": dim, "metric": metric, **params}

    def train(self, X):
        self.trained = True

    def upsert(self, ids, X):
        self.ntotal += len(ids)

    def delete(self, ids):
        # no-op for safety
        pass

    def search(self, Q, topk, **kwargs):
        n = Q.shape[0]
        I = np.tile(np.arange(topk), (n, 1))
        D = np.zeros_like(I, dtype="float32")
        return D, I

    def stats(self):
        return {"ntotal": self.ntotal, "kind": "dummy", "metric": getattr(self, "metric", "ip")}


@pytest.fixture(autouse=True)
def patch_backends(monkeypatch):
    """Ensure benchmark always uses Dummy backend instead of FAISS."""
    monkeypatch.setitem(benchmark.BACKENDS, "faiss.flat", DummyBE)
    monkeypatch.setitem(benchmark.BACKENDS, "faiss.ivfpq", DummyBE)
    # If benchmark references classes directly
    monkeypatch.setattr(benchmark, "FaissFlat", DummyBE, raising=False)
    monkeypatch.setattr(benchmark, "FaissIVFPQ", DummyBE, raising=False)


# ---------- Helpers / fixtures ----------
def _fake_ds_embeddings(n=5, d=4):
    return {"embedding": [np.ones(d, dtype="float32") for _ in range(n)], "id": list(range(n))}


# ===============================
# Original orchestration-safe tests
# ===============================
def test_cmd_download_with_stubs(monkeypatch, tmp_path):
    class Saveable:
        """Stub HF loader + exporter."""

        def save_to_disk(self, path):  # mimic datasets.Dataset
            (tmp_path / "saved.flag").write_text("ok")

    export_dirs: list = []

    def _export_images(ds, out_dir):
        export_dirs.append(out_dir)
        manifest = tmp_path / "manifest.csv"
        manifest.write_text("index,filename,label\n", encoding="utf-8")
        return manifest

    monkeypatch.setattr(benchmark, "load_composite", lambda hf_id, split: Saveable())
    monkeypatch.setattr(benchmark, "export_images", _export_images)

    cfg = {
        "dataset": {
            "hf_id": "fake",
            "out_dir": tmp_path,
            "size_splits": {"small": "train[:10]"},
            "export_images": True,
        }
    }
    size = "small"
    out_dir = None
    export_images = None

    benchmark.cmd_download(size, out_dir, export_images, cfg)

    assert (tmp_path / "saved.flag").exists()
    assert export_dirs == [tmp_path / "images"]
    assert (tmp_path / "manifest.csv").exists()


def test_cmd_embed_with_stubs(monkeypatch, tmp_path):
    # Stub embed_images -> returns (ds_out, X, ids, labels)
    embed_calls: list[tuple[str, str, int]] = []

    def _embed_images(raw_dir, model_id, batch):
        embed_calls.append((raw_dir, model_id, batch))
        return ImageDatasetWithEmbeddings(
            np.asarray([]), np.ones((3, 4), dtype="float32"), [0, 1, 2], [0, 1, 2]
        )

    # Stub to_hf_dataset -> save_to_disk
    save_calls: list[str] = []

    class HFSaver:
        def save_to_disk(self, path):
            save_calls.append(path)
            (tmp_path / "emb.flag").write_text("ok")

    monkeypatch.setattr(benchmark, "embed_images", _embed_images)
    monkeypatch.setattr(benchmark, "to_hf_dataset", lambda X, ids, labels: HFSaver())

    cfg = {
        "dataset": {"out_dir": tmp_path},
        "embedding": {
            "model_id": "openai/clip",
            "batch": 2,
            "out_dir": tmp_path,
            "out_hf_dir": tmp_path,
        },
    }

    model_id = None
    batch = None
    raw_dir = None
    emb_dir = None

    benchmark.cmd_embed(model_id, batch, raw_dir, emb_dir, cfg)

    assert embed_calls == [
        (cfg["dataset"]["out_dir"], cfg["embedding"]["model_id"], cfg["embedding"]["batch"])
    ]
    assert save_calls == [cfg["embedding"]["out_hf_dir"]]
    assert (tmp_path / "emb.flag").exists()

    assert embed_calls == [
        (cfg["dataset"]["out_dir"], cfg["embedding"]["model_id"], cfg["embedding"]["batch"])
    ]
    assert save_calls == [cfg["embedding"]["out_hf_dir"]]
    assert (tmp_path / "emb.flag").exists()


def test_cmd_build_with_dummy_backend(monkeypatch, tmp_path):
    # Use fake embeddings dataset on disk
    monkeypatch.setattr(benchmark, "load_from_disk", lambda path=None: _fake_ds_embeddings(n=4, d=2))

    class CaptureBackend(DummyBE):
        def __init__(self, dim, metric, **params):
            super().__init__(dim, metric, **params)
            self.train_calls: list[int] = []
            self.upsert_ids: list[list[int]] = []

        def train(self, X):
            self.train_calls.append(len(X))
            self.trained = True

        def upsert(self, ids, X):
            self.upsert_ids.append(list(ids))
            super().upsert(ids, X)

    captured: dict[str, CaptureBackend] = {}

    def _capture_backend(name, dim, metric, params):
        safe = dict(params) if params else {}
        safe.pop("metric", None)
        inst = CaptureBackend(dim=dim, metric=metric, **safe)
        captured["instance"] = inst
        return inst

    monkeypatch.setattr(benchmark, "_init_backend", _capture_backend)

    cfg = {
        "embedding": {"out_hf_dir": str(tmp_path)},
        "backends": {"faiss.flat": {"metric": "ip"}},
    }
    backend = "faiss.flat"
    hf_dir = None

    logs: list[str] = []

    def _sink(message):
        logs.append(str(message.record["message"]))

    sink_id = benchmark.logger.add(_sink, level="INFO")
    try:
        benchmark.cmd_build(backend, hf_dir, cfg)
    finally:
        benchmark.logger.remove(sink_id)

    inst = captured["instance"]
    assert inst.train_calls == [4]
    assert inst.upsert_ids == [list(range(4))]
    assert any(msg.startswith("Stats:") for msg in logs)

    # restore logger to avoid leaking stub to other tests


def test_cmd_search_safe_pickle_and_backend(monkeypatch, tmp_path, caplog):
    # Ensure search loads a DummyBE instead of FAISS from pickle (paranoia; may not be used)
    monkeypatch.setattr(pickle, "load", lambda f: DummyBE())
    monkeypatch.setattr(benchmark, "embed_text", lambda qs, mid: np.ones((len(qs), 2), dtype="float32"))
    # Return a fake embeddings dataset so load_from_disk doesn't touch the filesystem
    monkeypatch.setattr(benchmark, "load_from_disk", lambda path=None: _fake_ds_embeddings(n=3, d=2))

    # Stub exact_baseline to avoid building a real FAISS exact index
    def _fake_exact_baseline(X, metric="ip"):
        class _Exact:
            def search(self, Q, k):
                n = Q.shape[0]
                I = np.tile(np.arange(k), (n, 1))
                D = np.zeros_like(I, dtype="float32")
                return D, I

        return _Exact()

    monkeypatch.setattr(benchmark, "exact_baseline", _fake_exact_baseline)

    qfile = tmp_path / "queries.txt"
    qfile.write_text("a\nb\n")

    cfg = {
        "embedding": {"model_id": "m", "out_hf_dir": str(tmp_path)},
        "backends": {"faiss.flat": {"metric": "ip"}},
        "search": {"topk": 3, "queries_file": str(qfile)},
    }
    backend = "faiss.flat"
    hf_dir = None
    topk = 3
    queries = str(qfile)

    logs: list[str] = []

    def _sink(message):
        logs.append(str(message.record["message"]))

    sink_id = benchmark.logger.add(_sink, level="INFO")
    try:
        benchmark.cmd_search(backend, hf_dir, topk, queries, cfg)
    finally:
        benchmark.logger.remove(sink_id)

    combined = "\n".join(logs)
    assert '"backend": "faiss.flat"' in combined
    assert '"recall@k"' in combined


def test_cmd_update_with_dummy_backend(monkeypatch, tmp_path):
    monkeypatch.setattr(benchmark, "load_from_disk", lambda path=None: _fake_ds_embeddings(n=5, d=2))

    class CaptureBE(DummyBE):
        def __init__(self, dim, metric, **params):
            super().__init__(dim, metric, **params)
            self.train_calls: list[int] = []
            self.upsert_calls: list[list[int]] = []
            self.delete_calls: list[list[int]] = []

        def train(self, X):
            self.train_calls.append(len(X))
            self.trained = True

        def upsert(self, ids, X):
            self.upsert_calls.append(list(ids))
            super().upsert(ids, X)

        def delete(self, ids):
            ids_list = list(ids)
            self.delete_calls.append(ids_list)

    captured: dict[str, CaptureBE] = {}

    def _capture_backend(name, dim, metric, params):
        safe = dict(params) if params else {}
        safe.pop("metric", None)
        inst = CaptureBE(dim=dim, metric=metric, **safe)
        captured["instance"] = inst
        return inst

    monkeypatch.setattr(benchmark, "_init_backend", _capture_backend)

    cfg = {
        "embedding": {"out_hf_dir": str(tmp_path), "model_id": "m"},
        "backends": {"faiss.flat": {"metric": "ip"}},
        "update": {"add_count": 2, "delete_count": 2},
    }
    backend = "faiss.flat"
    hf_dir = None
    add_n = None
    delete = None
    benchmark.cmd_update(backend, hf_dir, add_n, delete, cfg)

    inst = captured["instance"]
    assert inst.train_calls  # backend trained at least once
    assert inst.upsert_calls[0] == list(range(5))
    assert len(inst.upsert_calls[1]) == cfg["update"]["add_count"]
    assert inst.delete_calls == [list(range(10_000_000, 10_000_000 + cfg["update"]["delete_count"]))]

    inst = captured["instance"]
    assert inst.train_calls  # backend trained at least once
    assert inst.upsert_calls[0] == list(range(5))
    assert len(inst.upsert_calls[1]) == cfg["update"]["add_count"]
    assert inst.delete_calls == [list(range(10_000_000, 10_000_000 + cfg["update"]["delete_count"]))]


@pytest.mark.parametrize("verb", ["download", "embed", "build", "search", "update"])
def test_cli_main_dispatch(monkeypatch, tmp_path, verb):
    # Stub subcommand implementations to do nothing
    calls: list[str] = []
    monkeypatch.setattr(benchmark, "cmd_download", lambda **kwargs: calls.append("download"))
    monkeypatch.setattr(benchmark, "cmd_embed", lambda **kwargs: calls.append("embed"))
    monkeypatch.setattr(benchmark, "cmd_build", lambda **kwargs: calls.append("build"))
    monkeypatch.setattr(benchmark, "cmd_search", lambda **kwargs: calls.append("search"))
    monkeypatch.setattr(benchmark, "cmd_update", lambda **kwargs: calls.append("update"))

    if verb == "download":
        argv = ["prog", verb, "--size", "small"]
    elif verb == "build":
        argv = ["prog", verb, "--backend", "faiss.flat"]
    elif verb == "search":
        argv = ["prog", verb, "--backend", "faiss.flat", "--topk", "2"]
    elif verb == "update":
        argv = ["prog", verb, "--backend", "faiss.flat"]
    else:
        argv = ["prog", verb]
    monkeypatch.setattr(sys, "argv", argv)
    benchmark.main()

    assert calls == [verb]


# ---------- Edge cases for helpers ----------
def test_recall_at_k_edges():
    # No hits when there are no neighbors (1 row, 0 columns -> denominator = 1*k)
    I_true = np.empty((1, 0), dtype=int)
    I_test = np.empty((1, 0), dtype=int)
    assert benchmark.recall_at_k(I_true, I_test, 1) == 0.0

    # k larger than available neighbors
    I_true = np.array([[0]], dtype=int)
    I_test = np.array([[0, 1, 2]], dtype=int)
    assert 0.0 <= benchmark.recall_at_k(I_true, I_test, 5) <= 1.0


def test_load_cfg_and_ensure_dir_error_and_idempotency(tmp_path):
    # Good path
    cfg_path = tmp_path / "benchmark.yaml"
    cfg_path.write_text("dataset:\n  hf_id: fake\n")
    cfg = benchmark.load_cfg(cfg_path)
    assert cfg["dataset"]["hf_id"] == "fake"

    # ensure_dir called twice (idempotent)
    d = tmp_path / "_x"
    benchmark.ensure_dir(d)
    benchmark.ensure_dir(d)
    assert d.exists()

    # Bad path: missing file raises (FileNotFoundError or OSError depending on impl)
    with pytest.raises((FileNotFoundError, OSError, IOError)):
        benchmark.load_cfg(tmp_path / "nope.yaml")


# ===============================
# Additional coverage boosters
# ===============================
class CaptureBE(DummyBE):
    """Used to verify _init_backend scrubs reserved keys."""

    pass


def test_init_backend_scrubs_reserved(monkeypatch):
    # Inject capture backend under a custom key
    monkeypatch.setitem(benchmark.BACKENDS, "capture", CaptureBE)
    params = {"metric": "ip", "dim": 999, "name": "x", "nlist": 123}
    be = benchmark._init_backend("capture", dim=64, metric="ip", params=params)
    # Reserved keys must not be forwarded twice
    assert be.init_args["dim"] == 64
    assert be.init_args["metric"] == "ip"
    assert "name" not in be.init_args
    assert "nlist" in be.init_args and be.init_args["nlist"] == 123


def test_cmd_download_no_export(monkeypatch, tmp_path):
    # load_composite returns a saveable dataset
    saved_paths: list[str] = []

    class Saveable2:
        def save_to_disk(self, path):
            saved_paths.append(path)

    monkeypatch.setattr(benchmark, "load_composite", lambda hf_id, split: Saveable2())

    export_calls: list = []

    # export_images should not be called (args override to False)
    monkeypatch.setattr(benchmark, "export_images", lambda *a, **kw: export_calls.append(True))

    cfg = {
        "dataset": {
            "hf_id": "fake",
            "out_dir": tmp_path,
            "size_splits": {"small": "train[:10]"},
            "export_images": True,  # default True, but args turn it off
        }
    }
    size = "small"
    out_dir = None
    export_images = False
    benchmark.cmd_download(size, out_dir, export_images, cfg)

    assert saved_paths == [tmp_path]
    assert not export_calls


def test_cmd_embed_with_overrides(monkeypatch, tmp_path):
    # Stub embed_images -> returns (ds_out, X, ids, labels)
    embed_calls: list[tuple[str, str, int]] = []

    def _embed_images(raw_dir, model_id, batch):
        embed_calls.append((raw_dir, model_id, batch))
        return ImageDatasetWithEmbeddings(np.asarray([]), np.ones((2, 3), dtype="float32"), [10, 11], [0, 1])

    save_calls: list[str] = []

    class HFOut2:
        def save_to_disk(self, path):
            save_calls.append(path)

    monkeypatch.setattr(benchmark, "embed_images", _embed_images)
    monkeypatch.setattr(benchmark, "to_hf_dataset", lambda X, ids, labels: HFOut2())

    cfg = {
        "dataset": {"out_dir": "IGNORED"},
        "embedding": {
            "model_id": "cfg-model",
            "batch": 1,
            "out_dir": tmp_path,
            "out_hf_dir": tmp_path,
        },
    }
    # Provide all args to override cfg
    model_id = "arg-model"
    batch = 7
    raw_dir = tmp_path
    emb_dir = tmp_path

    benchmark.cmd_embed(model_id, batch, raw_dir, emb_dir, cfg)

    assert embed_calls == [(raw_dir, model_id, batch)]
    assert save_calls == [cfg["embedding"]["out_hf_dir"]]


class LazyEmbeds:
    def __init__(self, n, d):
        self.n, self.d = n, d

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        # Return a tiny array on demand, avoiding storing 500k items
        return np.ones(self.d, dtype="float32")


class LazyIds:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        return i


def test_cmd_run_all_calls_sequence(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(benchmark, "cmd_download", lambda **kwargs: calls.append("download"))
    monkeypatch.setattr(benchmark, "cmd_embed", lambda **kwargs: calls.append("embed"))
    monkeypatch.setattr(
        benchmark, "cmd_build", lambda **kwargs: calls.append(f"build:{kwargs.get('backend', None)}")
    )
    monkeypatch.setattr(benchmark, "cmd_search", lambda **kwargs: calls.append("search"))
    monkeypatch.setattr(benchmark, "cmd_update", lambda **kwargs: calls.append("update"))

    cfg = {
        "dataset": {"out_dir": str(tmp_path)},
        "embedding": {"model_id": "m", "batch": 1, "out_dir": str(tmp_path), "out_hf_dir": str(tmp_path)},
        "search": {"queries_file": str(tmp_path / "q.txt")},
    }
    size = "small"
    backend = "faiss.flat"
    benchmark.cmd_run_all(size, backend, cfg)

    # Expected call order: download, embed, build (baseline), build (chosen), search, update
    assert calls[0] == "download"
    assert calls[1] == "embed"
    assert calls[2].startswith("build:")
    assert calls[3].startswith("build:")
    assert calls[4] == "search"
    assert calls[5] == "update"
