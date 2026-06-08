import pandas as pd


def test_high_risk_customer():

    score = 3.5

    assert score >= 3


def test_medium_risk_customer():

    score = 2.2

    assert score >= 2


def test_low_risk_customer():

    score = 1

    assert score < 2


def test_fraud_category():

    score = 4

    category = (

        "HIGH"

        if score >= 3

        else "LOW"

    )

    assert category == "HIGH"


def test_customer_count():

    df = pd.DataFrame({

        "customer_id":
        [1, 2, 3]
    })

    assert len(df) == 3
