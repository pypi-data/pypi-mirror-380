import os
from unittest.mock import patch

import requests

from agentds.client import BenchmarkClient


def test_client_builds_session():
    client = BenchmarkClient(dev_mode=True, api_key="k", team_name="t")
    assert hasattr(client, "_session")


@patch("requests.Session.post")
def test_submit_prediction_handles_400(mock_post):
    class MockResponse:
        status_code = 400

        def json(self):
            return {"error": "Bad request", "details": {"validation_errors": ["Header mismatch"]}}

    mock_post.return_value = MockResponse()

    client = BenchmarkClient(dev_mode=True, api_key="k", team_name="t")
    result = client.submit_prediction("D", 1, predictions_file=os.path.join(os.path.dirname(__file__), "tmp.csv"))
    # Build a valid small CSV on the fly
    import pandas as pd

    df = pd.DataFrame({"ID": [1], "Prediction": [0.5]})
    path = os.path.join(os.path.dirname(__file__), "tmp.csv")
    df.to_csv(path, index=False)

    result = client.submit_prediction("D", 1, path, submission_format="ID,Prediction")
    assert result["success"] is False
    assert any("Header" in e for e in result["details"]["validation_errors"]) or result["details"]["validation_errors"]


