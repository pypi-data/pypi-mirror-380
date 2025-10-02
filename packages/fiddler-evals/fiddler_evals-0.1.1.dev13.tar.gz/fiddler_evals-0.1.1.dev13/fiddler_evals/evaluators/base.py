from __future__ import annotations

from abc import ABC, abstractmethod
from functools import cached_property
from typing import Any

from fiddler_evals.connection import get_connection
from fiddler_evals.constants import CONTENT_TYPE_HEADER_KEY, JSON_CONTENT_TYPE
from fiddler_evals.libs.http_client import RequestClient
from fiddler_evals.pydantic_models.evaluator import EvaluatorResponse
from fiddler_evals.pydantic_models.score import Score, ScoreStatus


class Evaluator(ABC):
    """Abstract base class for creating custom evaluators in Fiddler Evals.

    The Evaluator class provides a flexible framework for creating builtin and custom evaluators
    that can assess LLM outputs against various criteria. Each evaluator is
    responsible for a single, specific evaluation task (e.g., hallucination detection,
    answer relevance, exact match, etc.).


    Creating Custom Evaluators:
        To create a custom evaluator, inherit from this class and implement the `score` method
        with parameters specific to your evaluation needs:


        Example - Custom evaluator:
        class ExactMatchEvaluator(Evaluator):
            def score(self, outputs: dict, expected_outputs: dict) -> Score:
                actual = outputs.get('text', '')
                expected = expected_outputs.get('text', '')
                is_exact_match = actual.strip().lower() == expected.strip().lower()
                return Score(
                    name=self.name,
                    value=1.0 if is_exact_match else 0.0,
                    reasoning=f"Exact match: {is_exact_match}"
                )



    Note:
        The `score` method signature is intentionally flexible using `*args` and `**kwargs`
        to allow each evaluator to define its own parameter requirements. This design
        enables maximum flexibility while maintaining a consistent interface across
        all evaluators in the framework.
    """

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def score(self, *args: Any, **kwargs: Any) -> Score | list[Score]:
        """Evaluate inputs and return a score or list of scores.

        This method must be implemented by all concrete evaluator classes.
        Each evaluator can define its own parameter signature based on what
        it needs for evaluation.

        Common parameter patterns:
            - Output-only: score(self, output: str) -> Score
            - Input-Output: score(self, input: str, output: str) -> Score
            - Comparison: score(self, output: str, expected_output: str) -> Score
            - All parameters: score(self, input: str, output: str, context: list[str]) -> Score

        Args:
            *args: Positional arguments specific to the evaluator's needs.
            **kwargs: Keyword arguments specific to the evaluator's needs.

        Returns:
            Score | list[Score]: A single Score object or list of Score objects
                representing the evaluation results. Each Score should include:
                - name: The score name (e.g., "has_zipcode")
                - evaluator_name: The evaluator name (e.g., "RegexMatch")
                - value: The score value (typically 0.0 to 1.0)
                - status: SUCCESS, FAILED, or SKIPPED
                - reasoning: Optional explanation of the score
                - error: Optional error information if evaluation failed

        Raises:
            ValueError: If required parameters are missing or invalid.
            TypeError: If parameters have incorrect types.
            Exception: Any other evaluation-specific errors.

        """


class FiddlerEvaluator(Evaluator, ABC):
    """Base class for evaluators that use Fiddler's evaluator API."""

    @cached_property
    def _client(self) -> RequestClient:
        """Get the HTTP client for making API requests."""
        return get_connection().client

    def make_call(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Make a call to the evaluator API."""
        response = self._client.post(
            url="v3/evals/score",
            data=payload,
            headers={CONTENT_TYPE_HEADER_KEY: JSON_CONTENT_TYPE},
        )
        return response.json().get("data", {})

    def _parse_scores(self, data: dict[str, Any]) -> list[Score]:
        """Parse the scores from the API response.

        Args:
            data (dict[str, Any]): The API response data.

        Returns:
            Score | list[Score]: A single Score object or list of Score objects.
        """
        scores_response = EvaluatorResponse(**data)
        if not scores_response.scores:
            raise ValueError("No scores returned from Fiddler Evaluator")

        scores = []
        for score_response in scores_response.scores:
            if score_response.value is None and score_response.label is None:
                score = Score(
                    name=score_response.name,
                    evaluator_name=self.name,
                    status=ScoreStatus.FAILED,
                    error_reason="ValueError",
                    error_message=f"Score {score_response.name} has no value or label",
                    reasoning=score_response.reasoning,
                )
            else:
                score = Score(
                    name=score_response.name,
                    evaluator_name=self.name,
                    value=score_response.value,
                    label=score_response.label,
                    reasoning=score_response.reasoning,
                )

            scores.append(score)

        return scores
