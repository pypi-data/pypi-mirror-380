# Collinear Python SDK

Persona‑driven chat simulation for OpenAI‑compatible endpoints.

Requires Python 3.10+.

## Install (uv)

```bash
uv venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add collinear
uv sync
```

## Quickstart

```python
import os
from collinear.client import Client

client = Client(
    assistant_model_url="https://api.openai.com/v1",
    assistant_model_api_key=os.environ["OPENAI_API_KEY"],
    assistant_model_name="gpt-4o-mini",
    steer_api_key=os.environ.get("STEER_API_KEY"),
)

steer_config = {
    "ages": ["25-34"],
    "genders": ["woman"],
    "occupations": ["Employed"],
    "intents": ["Resolve billing issue"],
    "traits": {"impatience": ["low", "medium", "high"]},
    "locations": ["United States"],
    "languages": ["English"],
    "tasks": ["telecom support"],
}

results = client.simulate(
    steer_config,
    k=1,
    num_exchanges=2,
    steer_temperature=0.7,
    steer_max_tokens=256,
)

assessment = client.assess(results)
for row in assessment.evaluation_result:
    for score in row.values():
        print("score=", score.score, "rationale=", score.rationale)
```
