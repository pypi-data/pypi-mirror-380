import re

from fiddler_evals.evaluators.regex import RegexMatch, RegexSearch
from fiddler_evals.pydantic_models.score import Score, ScoreStatus


class TestRegexSearch:
    """Test cases for RegexSearch evaluator."""

    def test_regex_search_with_string_pattern(self) -> None:
        """When creating RegexSearch with string pattern
        Then it should compile the pattern correctly
        And score should work as expected."""
        evaluator = RegexSearch(r"\d{4}")

        # Test matching case
        score = evaluator.score("The year is 2024")
        assert isinstance(score, Score)
        assert score.name == "regex_match"
        assert score.evaluator_name == "RegexSearch"
        assert score.value == 1.0
        assert score.status == ScoreStatus.SUCCESS
        assert score.reasoning == "Matched: 2024"

        # Test non-matching case
        score = evaluator.score("No numbers here")
        assert score.value == 0.0
        assert score.reasoning == "No match"

    def test_regex_search_with_compiled_pattern(self) -> None:
        """When creating RegexSearch with compiled regex pattern
        Then it should use the pattern directly
        And score should work correctly."""
        pattern = re.compile(r"[A-Z]{2,}")
        evaluator = RegexSearch(pattern)

        # Test matching case
        score = evaluator.score("HELLO world")
        assert score.value == 1.0
        assert score.reasoning == "Matched: HELLO"

        # Test non-matching case
        score = evaluator.score("hello world")
        assert score.value == 0.0
        assert score.reasoning == "No match"


class TestRegexMatch:
    """Test cases for RegexMatch evaluator."""

    def test_regex_match_with_string_pattern(self) -> None:
        """When creating RegexMatch with string pattern
        Then it should compile the pattern correctly
        And score should work as expected."""
        evaluator = RegexMatch(r"\d{4}")

        # Test matching at start
        score = evaluator.score("2024 is the year")
        assert isinstance(score, Score)
        assert score.name == "regex_match"
        assert score.evaluator_name == "RegexMatch"
        assert score.value == 1.0
        assert score.status == ScoreStatus.SUCCESS
        assert score.reasoning == "Matched: 2024"

        # Test non-matching at start
        score = evaluator.score("The year is 2024")
        assert score.value == 0.0
        assert score.reasoning == "No match"

    def test_regex_match_with_compiled_pattern(self) -> None:
        """When creating RegexMatch with compiled regex pattern
        Then it should use the pattern directly
        And score should work correctly."""
        pattern = re.compile(r"[A-Z]{2,}")
        evaluator = RegexMatch(pattern)

        # Test matching at start
        score = evaluator.score("HELLO world")
        assert score.value == 1.0
        assert score.reasoning == "Matched: HELLO"

        # Test non-matching at start
        score = evaluator.score("hello HELLO")
        assert score.value == 0.0
        assert score.reasoning == "No match"

    def test_regex_match_vs_search_difference(self) -> None:
        """When comparing RegexMatch vs RegexSearch
        Then RegexMatch should only match at string start
        And RegexSearch should match anywhere in string."""
        text = "Hello 123 world"

        # RegexMatch - should not match (number not at start)
        match_evaluator = RegexMatch(r"\d+")
        match_score = match_evaluator.score(text)
        assert match_score.value == 0.0

        # RegexSearch - should match (number anywhere)
        search_evaluator = RegexSearch(r"\d+")
        search_score = search_evaluator.score(text)
        assert search_score.value == 1.0

    def test_regex_match_at_start(self) -> None:
        """When text starts with matching pattern
        Then RegexMatch should return 1.0
        And should work correctly."""
        evaluator = RegexMatch(r"[A-Z][a-z]+")

        # Test matching at start
        score = evaluator.score("Hello world")
        assert score.value == 1.0

        # Test not matching at start
        score = evaluator.score("hello world")
        assert score.value == 0.0
