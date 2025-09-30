"""Tests covering optional languages/locations axes and payload contents."""

from __future__ import annotations

from typing import cast

from openai.types.chat import ChatCompletionMessageParam

from collinear.schemas.steer import SteerConfig
from collinear.simulate.runner import SimulationRunner


class CaptureRunner(SimulationRunner):
    """Capture steer payloads for language/location tests."""

    def __init__(self) -> None:
        """Initialize the capture runner."""
        super().__init__(
            assistant_model_url="https://example.test",
            assistant_model_api_key="k",
            assistant_model_name="gpt-test",
            steer_api_key="demo-001",
        )
        self.captured_payloads: list[list[dict[str, object]]] = []

    async def _call_batch_endpoint(
        self,
        payloads: list[dict[str, object]],
        *,
        headers: dict[str, str],
    ) -> list[str]:
        _ = headers
        self.captured_payloads.append(payloads)
        return ["ok" for _ in payloads]

    async def _call_with_retry(
        self,
        _messages: list[ChatCompletionMessageParam],
        _system_prompt: str,
    ) -> str:
        return "assistant"


def _make_runner() -> CaptureRunner:
    return CaptureRunner()


def test_single_trait_count_scales_with_languages_locations() -> None:
    """Combinations multiply by languages/locations when provided."""
    cfg = SteerConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium", "high"]},
        locations=["US"],
        languages=["English", "Spanish"],
    )

    combos = cfg.combinations()

    base = 1 * 1 * 1 * 1 * 1 * 2
    assert len(combos) == base * 2


def test_mixed_trait_count_with_new_axes() -> None:
    """mix_traits=True scales by new axes as expected."""
    cfg = SteerConfig(
        traits={
            "confusion": ["low"],
            "impatience": ["medium", "high"],
            "skeptical": ["medium"],
        },
        locations=["US", "CA"],
        languages=["en", "es"],
    )

    combos = cfg.combinations(mix_traits=True)
    base = 1 * 1 * 1 * 1 * 2 * 2
    pair_products = 2 + 1 + 2
    assert len(combos) == base * pair_products


def test_payload_includes_location_and_language() -> None:
    """Payload forwards location/language inside user_characteristics."""
    runner = _make_runner()
    cfg = SteerConfig(
        ages=["35-44"],
        genders=["male"],
        occupations=["Employed"],
        intents=["cancel"],
        traits={"impatience": ["medium"]},
        locations=["US"],
        languages=["Spanish"],
        tasks=["education"],
    )

    runner.run(config=cfg, k=1, num_exchanges=1, batch_delay=0.0, progress=False)
    assert runner.captured_payloads
    payload = runner.captured_payloads[-1][0]

    user_characteristics = cast("dict[str, object]", payload["user_characteristics"])
    assert user_characteristics == {
        "age": "35-44",
        "gender": "male",
        "occupation": "Employed",
        "intent": "cancel",
        "location": "US",
        "language": "Spanish",
        "task": "education",
    }
