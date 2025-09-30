import builtins
from types import SimpleNamespace
from mirdip_client.http import MirDIPClient


class DummyHandler:
	def __init__(self, payload: str):
		self._payload = payload.encode("utf-8")

	def read(self):
		return self._payload

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc, tb):
		return False


def test_parse_response(monkeypatch):
	# Prepare a payload with ASCII 0x01 and 0x02 separators
	entry = chr(0x01)
	kv = chr(0x02)
	payload = (
		f"generated_at{kv}2025-01-01{entry}"
		f"results_size{kv}3{entry}"
		f"results{kv}A\tB\tC"
	)

	def fake_urlopen(url, data, timeout):
		return DummyHandler(payload)

	monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

	client = MirDIPClient(base_url="http://example.test")
	resp = client.search_genes("A,B", "High")
	assert resp.generated_at == "2025-01-01"
	assert resp.results_size == "3"
	assert resp.results == "A\tB\tC"

