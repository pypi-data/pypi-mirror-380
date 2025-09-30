from ordeq_sentence_transformers.sentence_transformer import (
    SentenceTransformer,
)


class DummySentenceTransformer:
    def __init__(self, model, **kwargs):
        self.model = model
        self.kwargs = kwargs


def test_init_model():
    model = SentenceTransformer(model="all-mpnet-base-v2")
    assert model.model == "all-mpnet-base-v2"


def test_load_passes_kwargs(monkeypatch):
    model = SentenceTransformer(model="all-mpnet-base-v2")
    monkeypatch.setattr(
        "sentence_transformers.SentenceTransformer", DummySentenceTransformer
    )
    dummy = model.load(kwarg="abc123")
    assert dummy.model == "all-mpnet-base-v2"
    assert dummy.kwargs["kwarg"] == "abc123"  # type: ignore[non-subscriptable]
