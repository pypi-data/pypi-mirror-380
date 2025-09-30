import dataclasses
import traceback
import urllib.parse
import urllib.request
from typing import Dict, Optional


DEFAULT_BASE_URL = "http://ophid.utoronto.ca/mirDIP"


@dataclasses.dataclass
class MirDIPResponse:
	raw_text: str
	fields: Dict[str, str]

	def get(self, key: str, default: str = "") -> str:
		return self.fields.get(key, default)

	@property
	def generated_at(self) -> str:
		return self.get("generated_at")

	@property
	def gene_symbols(self) -> str:
		return self.get("gene_symbols")

	@property
	def micro_rnas(self) -> str:
		return self.get("micro_rnas")

	@property
	def minimum_score(self) -> str:
		return self.get("minimum_score")

	@property
	def db_occurrences(self) -> str:
		return self.get("dbOccurrences")

	@property
	def sources(self) -> str:
		return self.get("sources")

	@property
	def results_size(self) -> str:
		return self.get("results_size")

	@property
	def results(self) -> str:
		return self.get("results")


class MirDIPClient:
	SCORE_TO_CLASS = {
		"Very High": "0",
		"High": "1",
		"Medium": "2",
		"Low": "3",
	}

	def __init__(self, base_url: str = DEFAULT_BASE_URL, timeout: Optional[float] = 60.0) -> None:
		self.base_url = base_url.rstrip("/")
		self.timeout = timeout

	def _post(self, path: str, params: Dict[str, str]) -> MirDIPResponse:
		encoded = urllib.parse.urlencode(params).encode()
		url = f"{self.base_url}{path}"
		try:
			with urllib.request.urlopen(url, encoded, timeout=self.timeout) as handler:
				raw = handler.read().decode("utf-8")
		except Exception:
			traceback.print_exc()
			raise
		return MirDIPResponse(raw_text=raw, fields=self._parse_kv_payload(raw))

	def _parse_kv_payload(self, text: str) -> Dict[str, str]:
		# Server uses ASCII 0x01 for entry delimiter and 0x02 for key/value delimiter
		ENTRY_DEL = chr(0x01)
		KEY_DEL = chr(0x02)
		result: Dict[str, str] = {}
		for entry in text.split(ENTRY_DEL):
			if not entry:
				continue
			parts = entry.split(KEY_DEL)
			if len(parts) > 1:
				result[parts[0]] = parts[1]
		return result

	def _score_class(self, minimum_score: str) -> str:
		try:
			return self.SCORE_TO_CLASS[minimum_score]
		except KeyError:
			raise ValueError(
				f"minimum_score must be one of {list(self.SCORE_TO_CLASS.keys())}, got: {minimum_score}"
			)

	def search_genes(self, gene_symbols: str, minimum_score: str) -> MirDIPResponse:
		params = {
			"genesymbol": gene_symbols,
			"microrna": "",
			"scoreClass": self._score_class(minimum_score),
			"dbOccurrences": "1",
			"sources": "",
		}
		return self._post("/Http_U", params)

	def search_micro_rnas(self, micro_rnas: str, minimum_score: str) -> MirDIPResponse:
		params = {
			"genesymbol": "",
			"microrna": micro_rnas,
			"scoreClass": self._score_class(minimum_score),
			"dbOccurrences": "1",
			"sources": "",
		}
		return self._post("/Http_U", params)

	def search_bidirectional(
		self,
		gene_symbols: str,
		micro_rnas: str,
		minimum_score: str,
		sources: str,
		occurrences: str = "1",
	) -> MirDIPResponse:
		params = {
			"genesymbol": gene_symbols,
			"microrna": micro_rnas,
			"scoreClass": self._score_class(minimum_score),
			"dbOccurrences": occurrences,
			"sources": sources,
		}
		return self._post("/Http_B", params)

