# mirdip-client

Typed Python client and CLI for the mirDIP HTTP API.

[![CI](https://github.com/your-org/mirdip-client/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/mirdip-client/actions/workflows/ci.yml)

## Install

```bash
pip install .
```

## Usage (Python)

```python
from mirdip_client import MirDIPClient

client = MirDIPClient()
resp = client.search_genes("AKAP17A,AKR1C2,APP,ZZZ3,MARK4,C17orf51", "Very High")
print(resp.results_size)
print(resp.results)  # Tab-delimited
```

### Pandas helper
The `results` field is a tab-delimited string. To convert to a DataFrame:

```python
import pandas as pd
from io import StringIO

# results contains header row followed by rows
df = pd.read_csv(StringIO(resp.results), sep="\t")
```

## CLI

```bash
mirdip genes "AKAP17A,AKR1C2" "Very High"
mirdip micrornas "hsa-miR-603,hsa-let-7a-3p" "High"
mirdip bidirectional "AKAP17A,APP" "hsa-miR-603" "Medium" "TargetScan_v7_2" 2
```

## Notes
- Base URL defaults to `http://ophid.utoronto.ca/mirDIP`.
- Score classes: Very High, High, Medium, Low.
- Responses include raw text and parsed fields.

## Contributing
See `CONTRIBUTING.md` for development and release instructions.
