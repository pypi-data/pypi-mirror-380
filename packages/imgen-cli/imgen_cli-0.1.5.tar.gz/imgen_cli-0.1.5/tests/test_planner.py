from __future__ import annotations

import json

import pytest

from imagemcp.planner import (
    CollectContextPayload,
    PlanConstraints,
    PlanPayload,
    collect_context_questions,
    normalize_collect_context_payload,
    normalize_plan_payload,
    plan_image_job,
)


def test_collect_context_questions_identifies_missing_fields():
    payload = CollectContextPayload(requestText="Need homepage hero")
    result = collect_context_questions(payload)
    missing_fields = {item["field"] for item in result["missing"]}
    assert "slot" in missing_fields
    assert "projectRoot" in missing_fields
    defaults = result["defaults"]
    assert defaults["count"] == 3
    assert defaults["provider"] == "openrouter"
    assert defaults["model"] == "google/gemini-2.5-flash-image-preview"
    assert "size" not in defaults
    assert defaults["projectRoot"] == "."


def test_plan_image_job_respects_constraints():
    constraints = PlanConstraints(
        width=800,
        height=600,
        guidance="Use electric blues",
        provider="mock",
        model="mock-diffusion-v1",
    )
    payload = PlanPayload(
        slot="hero",
        requestText="Generate 2 bold hero illustrations",
        constraints=constraints,
        count=2,
        projectRoot="/tmp/project",
    )
    result = plan_image_job(payload)
    plan = result["plan"]
    assert plan["size"] == "800x600"
    assert plan["aspectRatio"] is None
    assert plan["n"] == 2
    command = result["cli"]["command"]
    assert "--size" in command
    assert "imgen" == command[0]
    assert command.count("--slot") == 1
    assert "--provider" in command
    assert "--model" in command
    assert plan["provider"] == "mock"
    assert result["cli"]["stdin"]["provider"] == "mock"
    assert result["cli"]["stdin"]["prompt"].startswith("Generate 2 bold hero illustrations")
    assert result["project"]["projectRoot"] == "/tmp/project"
    assert result["cli"]["projectRoot"] == "/tmp/project"
    assert any("auto-initialize" in note or "auto" in note for note in result["notes"])
    requirements = result["cli"]["requirements"]
    assert requirements["command"] == "imgen"
    assert requirements["minimumVersion"] == "0.1.0"
    assert requirements["setupResource"] == "setup://imgen-cli"
    assert requirements["installCommand"] == "pipx install imgen-cli"
    assert requirements["upgradeCommand"] == "pipx upgrade imgen-cli"
    assert requirements["pipxInstallCommand"] == "brew install pipx"
    assert any("setup://imgen-cli" in note for note in result["notes"])
    assert any("`pip install`" in note for note in result["notes"])
    assert any("brew install pipx" in note for note in result["notes"])
    assert any("setup://imgen-parameters" in note for note in result["notes"])


def test_plan_image_job_requires_geometry():
    payload = PlanPayload(
        slot="hero",
        requestText="Make something nice",
        constraints=PlanConstraints(),
    )
    with pytest.raises(ValueError):
        plan_image_job(payload)


def test_plan_image_job_defaults_provider_and_model_with_aspect_ratio():
    payload = PlanPayload(
        slot="hero",
        requestText="Create warm hero variations",
        constraints=PlanConstraints(aspectRatio="4:3"),
        projectRoot="/tmp/project",
    )
    result = plan_image_job(payload)
    plan = result["plan"]
    assert plan["size"] is None
    assert plan["aspectRatio"] == "4:3"
    assert plan["provider"] == "openrouter"
    assert plan["model"] == "google/gemini-2.5-flash-image-preview"
    command = result["cli"]["command"]
    assert "--aspect-ratio" in command
    assert "--provider" not in command
    assert "--project-root" in command
    assert "--model" not in command
    assert "model" not in result["cli"]["stdin"]
    assert "provider" not in result["cli"]["stdin"]


def test_normalize_plan_payload_accepts_string():
    raw = json.dumps(
        {
            "slot": "hero",
            "requestText": "String payload",
            "constraints": {
                "width": 512,
                "height": 512,
            },
        }
    )
    payload = normalize_plan_payload(raw)
    assert isinstance(payload, PlanPayload)
    assert payload.slot == "hero"
    assert payload.constraints.width == 512
    assert payload.constraints.height == 512


def test_normalize_collect_context_payload_accepts_string():
    raw = json.dumps(
        {
            "requestText": "Need hero",
            "known": {
                "slot": "hero",
                "constraints": {"aspectRatio": "16:9"},
            },
        }
    )
    payload = normalize_collect_context_payload(raw)
    assert isinstance(payload, CollectContextPayload)
    assert payload.known.slot == "hero"
    assert payload.known.constraints is not None
    assert payload.known.constraints.aspectRatio == "16:9"
