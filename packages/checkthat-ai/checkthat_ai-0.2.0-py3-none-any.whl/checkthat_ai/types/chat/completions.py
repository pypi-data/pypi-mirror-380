from typing import Optional, List, Dict, Any, Union, Literal, TypeVar
from pydantic import BaseModel, Field
from enum import Enum
from openai.types.chat import ChatCompletion
from openai.types.chat.parsed_chat_completion import ParsedChatCompletion

# Type variable for response format matching OpenAI's pattern
ResponseFormatT = TypeVar("ResponseFormatT")


class EvaluationReport(BaseModel):
    """Structured report of evaluation metrics applied to the model's output.

    Args:
        metrics_used (List[str]): The evaluation metrics that were applied
        scores (Dict[str, float]): Scores for each metric (0.0 to 1.0 scale)
        detailed_results (Dict[str, Dict[str, Any]]): Detailed results for each metric
        timestamp (str): ISO timestamp when the evaluation was performed
        report_url (Optional[str]): URL to the full evaluation report if saved to cloud
        model_info (Optional[Dict[str, Any]]): Information about the model used
    Example:
        ```python   
        report = EvaluationReport(
            metrics_used=["accuracy", "f1_score"],  
            scores={"accuracy": 0.95, "f1_score": 0.92},
            detailed_results={
                "accuracy": {"true_positives": 95, "false_positives": 5, "true_negatives": 90, "false_negatives": 10},
                "f1_score": {"precision": 0.94, "recall": 0.90}
            },
            timestamp="2024-08-01T12:00:00Z",
            report_url="https://example.com/evaluation/report/12345",
            model_info={"name": "gpt-4o", "version": "2024-08-06"}
        )
    """
    metrics_used: List[str] = Field(description="The evaluation metrics that were applied")
    scores: Dict[str, float] = Field(description="Scores for each metric (0.0 to 1.0 scale)")
    detailed_results: Dict[str, Dict[str, Any]] = Field(description="Detailed results for each metric")
    timestamp: str = Field(description="ISO timestamp when the evaluation was performed")
    report_url: Optional[str] = Field(default=None, description="URL to the full evaluation report if saved to cloud")
    model_info: Optional[Dict[str, Any]] = Field(default=None, description="Information about the model used")

class ClaimType(str, Enum):
    ORIGINAL = "original"
    REFINED = "refined"
    FINAL = "final"

class RefinementHistory(BaseModel):
    """History entry for claim refinement process.

    Args:
        claim_type (ClaimType): The type of claim
        claim (Optional[str], optional): The claim. Defaults to None.
        score (float): Score for the claim (0.0 to 1.0 scale)
        feedback (Optional[str], optional): The feedback from the refinement. Defaults to None.
        
    Example:
        ```python
        history_entry = RefinementHistory(
            claim_type=ClaimType.REFINED,
            claim="The refined claim text.",
            score=0.85,
            feedback="Improved clarity and specificity."
        )
        ```
    """
    claim_type: ClaimType = Field(description="The type of claim")
    claim: Optional[str] = Field(default=None, description="The claim")
    score: float = Field(description="Score for the claim (0.0 to 1.0 scale)")
    feedback: Optional[str] = Field(default=None, description="The feedback from the refinement")
class RefinementMetadata(BaseModel):
    """
    Metadata about the claim refinement process.
    Args:
        metric_used (Optional[str]): The metric that was used for refinement
        threshold (Optional[float]): The threshold that was used for refinement
        refinement_model (Optional[str]): The model that was used for refinement
        refinement_history (List[RefinementHistory]): History of the refinement process
    Example:
        ```python
        metadata = RefinementMetadata(
            metric_used="f1_score",
            threshold=0.85, 
            refinement_model="gpt-4o",
            refinement_history=[
                RefinementHistory(  
                    claim_type=ClaimType.ORIGINAL,
                    claim="The original claim text.",
                    score=0.75,
                    feedback=None
                ),
                RefinementHistory(
                    claim_type=ClaimType.REFINED,
                    claim="The refined claim text.",
                    score=0.85,
                    feedback="Improved clarity and specificity."
                )
            ]
        )
        ```
    """
    metric_used: Optional[str] = Field(default=None, description="The metric that was used for refinement")
    threshold: Optional[float] = Field(default=None, description="The threshold that was used for refinement")
    refinement_model: Optional[str] = Field(default=None, description="The model that was used for refinement")
    refinement_history: List[RefinementHistory] = Field(description="History of the refinement process")


class CheckThatChatCompletion(ChatCompletion):
    """
    Extended ChatCompletion with CheckThat AI evaluation and refinement data.
    Args:
        evaluation_report (Optional[EvaluationReport]): Post-normalization evaluation results when requested
        refinement_metadata (Optional[RefinementMetadata]): Metadata about claim refinement process when applied
        checkthat_metadata (Optional[Dict[str, Any]]): Additional CheckThat AI-specific metadata
    Example:
        ```python
        response = CheckThatChatCompletion(
            id="chatcmpl-...",
            object="chat.completion",
            created=1691234567,
            model="gpt-4o-2024-08-06",
            choices=[...],
            usage={...},
            evaluation_report=EvaluationReport(...),
            refinement_metadata=RefinementMetadata(...),
            checkthat_metadata={"custom_key": "custom_value"}
        )
    """
    evaluation_report: Optional[EvaluationReport] = Field(
        default=None,
        description="Post-normalization evaluation results when requested"
    )
    refinement_metadata: Optional[RefinementMetadata] = Field(
        default=None,
        description="Metadata about claim refinement process when applied"
    )
    checkthat_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional CheckThat AI-specific metadata"
    )


class CheckThatParsedChatCompletion(ParsedChatCompletion[ResponseFormatT]):
    """
    Extended ParsedChatCompletion with CheckThat AI evaluation and refinement data.
    Args:
        evaluation_report (Optional[EvaluationReport]): Post-normalization evaluation results when requested
        refinement_metadata (Optional[RefinementMetadata]): Metadata about claim refinement process when applied
        checkthat_metadata (Optional[Dict[str, Any]]): Additional CheckThat AI-specific metadata
    Example:
        ```python
        response = CheckThatParsedChatCompletion(
            id="chatcmpl-...",
            object="chat.completion",
            created=1691234567,
            model="gpt-4o-2024-08-06",
            choices=[...],
            usage={...},
            parsed=[...],
            evaluation_report=EvaluationReport(...),
            refinement_metadata=RefinementMetadata(...),
            checkthat_metadata={"custom_key": "custom_value"}
        )
    """
    evaluation_report: Optional[EvaluationReport] = Field(
        default=None,
        description="Post-normalization evaluation results when requested"
    )
    refinement_metadata: Optional[RefinementMetadata] = Field(
        default=None,
        description="Metadata about claim refinement process when applied"
    )
    checkthat_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional CheckThat AI-specific metadata"
    )
