"""
Validation utilities for AgentDS Python client.
"""

import os
from typing import Any, Dict, List, Tuple, Optional

import pandas as pd
from ..exceptions import ValidationError
from ..config import MAX_SUBMISSION_MB


def validate_csv_response(file_path: str, expected_rows: int = 0) -> Tuple[bool, str]:
    """
    Backwards-compatible simple CSV validation for legacy flows.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return False, "CSV file is empty"
        if df.shape[1] < 2:
            return False, f"CSV must have at least 2 columns, found {df.shape[1]}"
        if expected_rows > 0 and df.shape[0] != expected_rows:
            return False, f"CSV must have exactly {expected_rows} data rows, found {df.shape[0]}"
        if df.isna().any().any():
            return False, "CSV contains missing values"
        return True, ""
    except pd.errors.EmptyDataError:
        return False, "CSV file is empty"
    except pd.errors.ParserError:
        return False, "Invalid CSV format"
    except Exception as e:
        return False, f"Error validating CSV: {str(e)}"


def _file_size_mb(path: str) -> float:
    try:
        size_bytes = os.path.getsize(path)
        return size_bytes / (1024 * 1024)
    except OSError:
        return 0.0


def _parse_submission_format(submission_format: str) -> List[str]:
    """
    Parse a submission format string like "ID,Prediction" or "UserID,ItemID,Prediction".
    Returns a list of column names in order.
    """
    return [c.strip() for c in submission_format.split(',') if c.strip()]


def validate_predictions_df(
    df: pd.DataFrame,
    expected_submission_format: Optional[str] = None,
    expected_rows: Optional[int] = None,
    numeric_prediction: Optional[bool] = None,
    probability_range: Optional[Tuple[float, float]] = None,
) -> List[str]:
    """
    Validate predictions DataFrame against stricter rules aligned with backend validators.

    Returns a list of validation error messages (empty if valid).
    """
    errors: List[str] = []

    if df.empty:
        return ["CSV file is empty"]

    if expected_rows is not None and expected_rows > 0 and df.shape[0] != expected_rows:
        errors.append(f"CSV must have exactly {expected_rows} data rows, found {df.shape[0]}")

    # Determine expected columns
    expected_columns: Optional[List[str]] = None
    if expected_submission_format:
        expected_columns = _parse_submission_format(expected_submission_format)
        if list(df.columns) != expected_columns:
            errors.append(
                f"Header mismatch: expected '{','.join(expected_columns)}' but found '{','.join([str(c) for c in df.columns])}'"
            )

    # Identify id columns and prediction column if format known
    id_columns: List[str] = []
    prediction_columns: List[str] = []
    if expected_columns:
        if len(expected_columns) < 2:
            errors.append("Submission format must include at least one ID column and one prediction column")
        else:
            id_columns = expected_columns[:-1]
            prediction_columns = [expected_columns[-1]]
    else:
        # Fallback: treat all but last as IDs
        if df.shape[1] >= 2:
            id_columns = list(df.columns[:-1])
            prediction_columns = [df.columns[-1]]
        else:
            errors.append("CSV must have at least 2 columns (IDs and Prediction)")

    # Missing values check
    if df.isna().any().any():
        errors.append("CSV contains missing values")

    # ID columns checks
    if id_columns:
        # Blank IDs
        for col in id_columns:
            if df[col].astype(str).str.strip().eq("").any():
                errors.append(f"ID column '{col}' contains blank values")
        # Composite uniqueness
        if df.duplicated(subset=id_columns, keep=False).any():
            errors.append("Duplicate ID rows detected across ID columns")

    # Prediction checks
    if prediction_columns:
        pred_col = prediction_columns[0]
        if numeric_prediction:
            # Ensure numeric type
            try:
                preds = pd.to_numeric(df[pred_col], errors='coerce')
            except Exception:
                preds = pd.Series([None] * len(df))
            if preds.isna().any():
                errors.append(f"Prediction column '{pred_col}' must be numeric")
            else:
                if probability_range is not None:
                    low, high = probability_range
                    if (preds < low).any() or (preds > high).any():
                        errors.append(
                            f"Prediction column '{pred_col}' must be within range [{low}, {high}]"
                        )

    return errors


def prevalidate_predictions_file(
    file_path: str,
    expected_submission_format: Optional[str] = None,
    expected_rows: Optional[int] = None,
    numeric_prediction: Optional[bool] = None,
    probability_range: Optional[Tuple[float, float]] = None,
    max_size_mb: int = MAX_SUBMISSION_MB,
) -> Tuple[pd.DataFrame, List[str]]:
    """
    Perform file-size and CSV validations before submission.
    Returns (dataframe, errors). Errors list is empty if valid.
    """
    size_mb = _file_size_mb(file_path)
    if size_mb > max_size_mb:
        return pd.DataFrame(), [f"Predictions file size {size_mb:.2f}MB exceeds limit of {max_size_mb}MB"]

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(), ["CSV file is empty"]
    except pd.errors.ParserError as e:
        return pd.DataFrame(), [f"Invalid CSV format: {str(e)}"]
    except Exception as e:
        return pd.DataFrame(), [f"Error reading CSV: {str(e)}"]

    errors = validate_predictions_df(
        df,
        expected_submission_format=expected_submission_format,
        expected_rows=expected_rows,
        numeric_prediction=numeric_prediction,
        probability_range=probability_range,
    )
    return df, errors


def validate_api_response(response_data: Dict[str, Any]) -> bool:
    """
    Validate API response structure.
    
    Args:
        response_data: Response data from API
        
    Returns:
        True if response is valid, False otherwise
    """
    if not isinstance(response_data, dict):
        return False
    
    required_fields = ["success"]
    return all(field in response_data for field in required_fields)


def validate_task_response(response: Any, expected_format: Dict[str, Any] = None) -> bool:
    """
    Validate a task response against expected format.
    
    Args:
        response: The response to validate
        expected_format: Expected format specification
        
    Returns:
        True if response is valid, False otherwise
    """
    if expected_format is None:
        return True
    
    try:
        if isinstance(expected_format, dict) and isinstance(response, dict):
            for key in expected_format:
                if key not in response:
                    return False
            return True
        else:
            return isinstance(response, type(expected_format))
    except Exception:
        return False


def validate_credentials(api_key: str, team_name: str) -> None:
    """
    Validate API credentials format.
    
    Args:
        api_key: API key to validate
        team_name: Team name to validate
        
    Raises:
        ValidationError: If credentials are invalid
    """
    if not api_key or not isinstance(api_key, str):
        raise ValidationError("API key must be a non-empty string")
    
    if not team_name or not isinstance(team_name, str):
        raise ValidationError("Team name must be a non-empty string")
    
    if len(api_key.strip()) < 10:
        raise ValidationError("API key appears to be too short")
    
    if len(team_name.strip()) < 2:
        raise ValidationError("Team name appears to be too short")


def validate_domain_name(domain_name: str) -> None:
    """
    Validate domain name format.
    
    Args:
        domain_name: Domain name to validate
        
    Raises:
        ValidationError: If domain name is invalid
    """
    if not domain_name or not isinstance(domain_name, str):
        raise ValidationError("Domain name must be a non-empty string")
    
    if not domain_name.strip():
        raise ValidationError("Domain name cannot be empty or whitespace only") 