import io
import pandas as pd

from agentds.utils.validators import validate_predictions_df


def test_validate_predictions_header_and_uniqueness():
    df = pd.DataFrame({
        "UserID": [1, 2, 2],
        "ItemID": [10, 20, 20],
        "Prediction": [0.1, 0.2, 0.3],
    })
    errors = validate_predictions_df(df, expected_submission_format="UserID,ItemID,Prediction", expected_rows=None, numeric_prediction=True, probability_range=(0.0, 1.0))
    assert any("Duplicate ID rows" in e for e in errors)


def test_validate_predictions_numeric_range():
    df = pd.DataFrame({
        "ID": ["a", "b"],
        "Prediction": [1.2, -0.1],
    })
    errors = validate_predictions_df(df, expected_submission_format="ID,Prediction", expected_rows=2, numeric_prediction=True, probability_range=(0.0, 1.0))
    assert any("within range" in e for e in errors)


def test_validate_predictions_header_mismatch():
    df = pd.DataFrame({
        "IDX": ["a"],
        "Pred": [0.5],
    })
    errors = validate_predictions_df(df, expected_submission_format="ID,Prediction")
    assert any("Header mismatch" in e for e in errors)


