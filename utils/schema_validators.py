"""
Schema Validators for Lab 4 — Structured Output Sprint
"""

import json
import jsonschema

USER_STORY_SCHEMA = {
    "type": "object",
    "properties": {
        "actor": {"type": "string", "minLength": 1},
        "action": {"type": "string", "minLength": 1},
        "goal": {"type": "string", "minLength": 1},
    },
    "required": ["actor", "action", "goal"],
    "additionalProperties": False,
}


def validate_user_story_output(model_output, schema=None):
    """
    Validate model output against the user story extraction schema.

    Returns:
        dict: {valid: bool, data: dict|None, error: str|None}
    """
    if schema is None:
        schema = USER_STORY_SCHEMA

    text = model_output.strip()
    # Remove markdown code fences
    for prefix in ("```json", "```"):
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Parse JSON
    parsed = None
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                parsed = json.loads(text[start:end])
            except json.JSONDecodeError:
                pass

    if parsed is None:
        return {"valid": False, "data": None, "error": "Invalid JSON"}

    # Validate schema
    try:
        jsonschema.validate(parsed, schema)
        return {"valid": True, "data": parsed, "error": None}
    except jsonschema.ValidationError as e:
        return {"valid": False, "data": parsed, "error": f"Schema: {e.message}"}


def compute_compliance_rate(results):
    """Compute format compliance rate from a list of validation results."""
    if not results:
        return 0.0
    return sum(1 for r in results if r.get("valid")) / len(results)
