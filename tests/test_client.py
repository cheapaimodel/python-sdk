import pytest

from cheapaimodel import DEFAULT_BASE_URL, AsyncCheapAIModel, CheapAIModel


def test_missing_key_raises(monkeypatch):
    monkeypatch.delenv("CHEAPAIMODEL_API_KEY", raising=False)
    with pytest.raises(ValueError):
        CheapAIModel()


def test_reads_env(monkeypatch):
    monkeypatch.setenv("CHEAPAIMODEL_API_KEY", "test-key")
    monkeypatch.delenv("CHEAPAIMODEL_BASE_URL", raising=False)
    client = CheapAIModel()
    assert client.api_key == "test-key"
    assert str(client.base_url).rstrip("/") == DEFAULT_BASE_URL


def test_custom_base_url():
    client = AsyncCheapAIModel(api_key="k", base_url="https://example.test/v1")
    assert str(client.base_url).rstrip("/") == "https://example.test/v1"
