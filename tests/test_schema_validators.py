"""Auto-grading: Lab 4 schema validators & consistency utils."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.schema_validators import validate_user_story_output, compute_compliance_rate
from utils.consistency_utils import extract_final_answer, majority_vote

class TestSchemaValidator:
    def test_valid(self):
        assert validate_user_story_output('{"actor":"a","action":"b","goal":"c"}')["valid"]
    def test_fences(self):
        assert validate_user_story_output('```json\n{"actor":"a","action":"b","goal":"c"}\n```')["valid"]
    def test_missing(self):
        assert not validate_user_story_output('{"actor":"a","action":"b"}')["valid"]
    def test_extra(self):
        assert not validate_user_story_output('{"actor":"a","action":"b","goal":"c","x":"d"}')["valid"]
    def test_invalid(self):
        assert not validate_user_story_output("not json")["valid"]
    def test_rate(self):
        assert compute_compliance_rate([{"valid":True},{"valid":True},{"valid":False}]) == pytest.approx(2/3)
    def test_rate_empty(self):
        assert compute_compliance_rate([]) == 0.0

class TestAnswerExtraction:
    def test_answer(self): assert extract_final_answer("blah\nANSWER: 8") == "8"
    def test_the_answer_is(self): assert extract_final_answer("the answer is 42.") == "42"
    def test_float(self): assert extract_final_answer("ANSWER: 0.75") == "0.75"
    def test_fallback(self): assert extract_final_answer("5 + 10 = 15") == "15"
    def test_none(self): assert extract_final_answer("no numbers") is None

class TestMajorityVote:
    def test_clear(self): assert majority_vote(["42","42","42","43","41"]) == "42"
    def test_all_none(self): assert majority_vote([None, None]) is None
    def test_skips_none(self): assert majority_vote(["42",None,"42",None,"43"]) == "42"
