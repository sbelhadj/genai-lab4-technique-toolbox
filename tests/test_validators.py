"""
Auto-grading tests for Lab 4 — Validators and Consistency Utils
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils.schema_validators import validate_user_story_output, compute_compliance_rate
from utils.consistency_utils import extract_final_answer, majority_vote, compute_agreement_rate


class TestSchemaValidators:

    def test_valid_json(self):
        r = validate_user_story_output('{"actor": "dev", "action": "code", "goal": "ship"}')
        assert r["valid"] is True

    def test_valid_with_fences(self):
        text = '```json\n{"actor": "dev", "action": "code", "goal": "ship"}\n```'
        r = validate_user_story_output(text)
        assert r["valid"] is True

    def test_valid_with_prefix(self):
        text = 'Here is the result:\n{"actor": "dev", "action": "code", "goal": "ship"}'
        r = validate_user_story_output(text)
        assert r["valid"] is True

    def test_invalid_json(self):
        assert validate_user_story_output("not json")["valid"] is False

    def test_missing_field(self):
        assert validate_user_story_output('{"actor": "dev", "action": "code"}')["valid"] is False

    def test_extra_field(self):
        text = '{"actor": "dev", "action": "code", "goal": "x", "extra": "y"}'
        assert validate_user_story_output(text)["valid"] is False

    def test_empty_field(self):
        assert validate_user_story_output('{"actor": "", "action": "code", "goal": "x"}')["valid"] is False

    def test_compliance_rate(self):
        results = [{"valid": True}, {"valid": True}, {"valid": False}, {"valid": True}]
        assert compute_compliance_rate(results) == 0.75


class TestConsistencyUtils:

    def test_extract_answer_tag(self):
        assert extract_final_answer("Some reasoning\nANSWER: 42") == "42"

    def test_extract_answer_sentence(self):
        assert extract_final_answer("So the answer is 7.") == "7"

    def test_extract_answer_equals(self):
        assert extract_final_answer("Total = 150") == "150"

    def test_majority_vote_basic(self):
        assert majority_vote(["a", "b", "a", "a", "b"]) == "a"

    def test_majority_vote_with_none(self):
        assert majority_vote([None, "a", None, "a"]) == "a"

    def test_majority_vote_all_none(self):
        assert majority_vote([None, None]) is None

    def test_agreement_rate(self):
        rate = compute_agreement_rate(["a", "a", "b", "a", "a"])
        assert abs(rate - 0.8) < 0.01

    def test_agreement_all_same(self):
        assert compute_agreement_rate(["x", "x", "x"]) == 1.0
