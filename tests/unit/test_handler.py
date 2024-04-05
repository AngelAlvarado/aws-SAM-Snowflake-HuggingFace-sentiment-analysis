import json

import pytest

from sentiment_analysis import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "text": "I absolutely love this product! It has changed my life for the better."}'
    }


def test_lambda_handler(apigw_event):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert "positive" in data["message"]
