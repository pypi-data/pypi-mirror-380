# Greenophy Client

Small Python helper package for calling the Greenophy substantiveness API.

## Installation

```bash
pip install .
```

## Usage

```python
from greenophy_client import SubstantivenessClient

client = SubstantivenessClient(
    base_url="https://greenophy-service-xyz.a.run.app",
    api_key="your-shared-token",  # optional
)

results = client.classify_text("We transitioned 70% of our fleet to EVs in 2023.\nWe value teamwork.")
for item in results:
    print(item.index, item.label_name, item.sentence)
```

The same client exposes `classify_sentences([...])` if you prefer passing your own sentence list.

Use `client.close()` when you are done (or create it with a context manager).
