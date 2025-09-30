"""Unit tests for steer configuration helpers."""

from __future__ import annotations

import pytest

from collinear.schemas.steer import SteerConfig


def test_combinations_count_and_contents() -> None:
    """Generate all combinations and validate counts and fields."""
    config = SteerConfig(
        ages=["18-24", "25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"], "skeptical": ["medium"]},
        tasks=["telecom"],
    )

    combos = config.combinations()

    expected_count = 2 * 1 * 1 * 1 * (1 + 1)
    assert len(combos) == expected_count

    assert {c.age for c in combos} == {"18-24", "25-34"}
    assert {c.trait for c in combos} == {"impatience", "skeptical"}
    assert {c.task for c in combos} == {"telecom"}

    assert all(c.intensity is not None for c in combos)
    assert {c.intensity for c in combos} == {"medium"}


def test_invalid_trait_level_raises() -> None:
    """Unknown trait levels should fail fast."""
    data = {
        "traits": {
            "impatience": ["very_high"],
        }
    }

    with pytest.raises(ValueError, match="invalid level"):
        SteerConfig.from_input(data)


def test_integer_trait_level_is_accepted() -> None:
    """Integer levels in [-2,2] are accepted alongside labels."""
    data = {
        "traits": {
            "impatience": [1],
        }
    }

    cfg = SteerConfig.from_input(data)
    assert cfg.traits == {"impatience": [1]}


def test_retired_combination_dropped_for_young_age() -> None:
    """Retired personas under 35-44 are excluded from combinations."""
    config = SteerConfig(
        ages=["25-34", "35-44"],
        genders=["female"],
        occupations=["Employed", "Retired"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
    )

    combos = config.combinations()
    combo_length = 3

    assert all(not (combo.occupation == "Retired" and combo.age == "25-34") for combo in combos)
    assert any(combo.occupation == "Retired" and combo.age == "35-44" for combo in combos)
    assert len(combos) == combo_length


def test_from_input_collects_task_fields() -> None:
    """Single and plural task keys are normalized into the config."""
    data = {
        "traits": {"impatience": ["medium"]},
        "task": "telecom",
        "tasks": ["retail", ""],
    }

    cfg = SteerConfig.from_input(data)
    assert cfg.tasks == ["retail", "telecom"]
