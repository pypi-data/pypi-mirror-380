import types
import os
import pandas as pd
import pytest

# Ajusta este import al nombre real de tu paquete
from mfdev_scraper_sdk.library import MFDevScraper
from mfdev_scraper_sdk.errors import (
    ConfigurationError, HTTPStatusError, MaxRetriesExceeded,
    NotADictError, MissingFieldError
)

# ---------- Helpers para mockear curl_cffi ----------

class _Resp:
    def __init__(self, status_code=200, text="ok"):
        self.status_code = status_code
        self.text = text

@pytest.fixture
def fake_curl_ok():
    """curl_cffi con GET/POST devolviendo 200."""
    c = types.SimpleNamespace()
    c.calls = {"get": 0, "post": 0}

    def _get(**kwargs):
        c.calls["get"] += 1
        return _Resp(200, "ok")

    def _post(**kwargs):
        c.calls["post"] += 1
        return _Resp(200, "ok")

    c.get = _get
    c.post = _post
    return c

@pytest.fixture
def fake_curl_bad_then_bad():
    """Siempre devuelve 500 para forzar reintentos y MaxRetriesExceeded."""
    c = types.SimpleNamespace()
    c.calls = {"get": 0, "post": 0}

    def _get(**kwargs):
        c.calls["get"] += 1
        return _Resp(500, "fail")

    def _post(**kwargs):
        c.calls["post"] += 1
        return _Resp(500, "fail")

    c.get = _get
    c.post = _post
    return c

# ---------- Tests: importación / setup ----------

def test_can_instantiate():
    client = MFDevScraper()
    assert client is not None

# ---------- Tests: request_mfdev ----------

def test_request_get_success(monkeypatch, fake_curl_ok):
    # Reemplaza el módulo curl_cffi dentro del módulo library ya importado
    import mfdev_scraper_sdk.library as lib
    monkeypatch.setattr(lib, "curl_cffi", fake_curl_ok, raising=True)

    client = MFDevScraper()
    r = client.request_mfdev(method="GET", url="https://example.com")
    assert r.status_code == 200
    assert fake_curl_ok.calls["get"] == 1

def test_request_post_success(monkeypatch, fake_curl_ok):
    import mfdev_scraper_sdk.library as lib
    monkeypatch.setattr(lib, "curl_cffi", fake_curl_ok, raising=True)

    client = MFDevScraper()
    r = client.request_mfdev(method="POST", url="https://example.com")
    assert r.status_code == 200
    assert fake_curl_ok.calls["post"] == 1

def test_request_without_url_raises_configuration_error():
    client = MFDevScraper()
    with pytest.raises(ConfigurationError):
        client.request_mfdev(method="GET", url=None)

def test_request_retries_and_raises_max(monkeypatch, fake_curl_bad_then_bad):
    import mfdev_scraper_sdk.library as lib
    monkeypatch.setattr(lib, "curl_cffi", fake_curl_bad_then_bad, raising=True)

    client = MFDevScraper()
    # Como tu código atrapa HTTPStatusError y reintenta,
    # el error final esperado es MaxRetriesExceeded
    with pytest.raises(MaxRetriesExceeded):
        client.request_mfdev(method="GET", url="https://example.com", max_retries=3)

    # Debe haber intentado exactamente max_retries veces
    assert fake_curl_bad_then_bad.calls["get"] == 3

# ---------- Tests: clean_duplicates_dict ----------

def test_clean_duplicates_happy_path():
    client = MFDevScraper()
    data = [
        {"id": 1, "name": "a"},
        {"id": 1, "name": "a-dup"},
        {"id": 2, "name": "b"},
    ]
    out = client.clean_duplicates_dict(data, field="id", strict=True)
    assert out == [{"id": 1, "name": "a"}, {"id": 2, "name": "b"}]

def test_clean_duplicates_not_a_dict_strict_true_raises():
    client = MFDevScraper()
    data = [{"id": 1}, "not-a-dict"]
    with pytest.raises(NotADictError):
        client.clean_duplicates_dict(data, field="id", strict=True)

def test_clean_duplicates_missing_field_strict_true_raises():
    client = MFDevScraper()
    data = [{"id": 1}, {"name": "sin-id"}]
    with pytest.raises(MissingFieldError):
        client.clean_duplicates_dict(data, field="id", strict=True)

def test_clean_duplicates_strict_false_skips_invalids():
    client = MFDevScraper()
    data = [{"id": 1}, {"name": "sin-id"}, "not-a-dict", {"id": 1}, {"id": 2}]
    out = client.clean_duplicates_dict(data, field="id", strict=False)
    assert out == [{"id": 1}, {"id": 2}]

# ---------- Tests: generate_csv / generate_excel ----------

def test_generate_csv_creates_file(tmp_path):
    client = MFDevScraper()
    records = [{"id": 1, "name": "a"}, {"id": 2, "name": "b"}]
    path = client.generate_csv(records, name="out.csv", folder=str(tmp_path))
    assert os.path.exists(path)

    df = pd.read_csv(path)
    assert list(df.columns) == ["id", "name"]
    assert len(df) == 2

def test_generate_excel_creates_file(tmp_path):
    client = MFDevScraper()
    records = [{"id": 1, "name": "a"}, {"id": 2, "name": "b"}]
    path = client.generate_excel(records, name="out.xlsx", folder=str(tmp_path))
    assert os.path.exists(path)

    df = pd.read_excel(path, engine="openpyxl")
    assert list(df.columns) == ["id", "name"]
    assert len(df) == 2
