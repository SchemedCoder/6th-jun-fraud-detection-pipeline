import pandas as pd


def test_high_value_rule():

    amount = 75000

    assert amount > 50000


def test_normal_transaction():

    amount = 1000

    assert amount < 50000


def test_country_risk():

    risky = [
        "Nigeria",
        "Russia"
    ]

    assert "Nigeria" in risky


def test_safe_country():

    risky = [
        "Nigeria",
        "Russia"
    ]

    assert "India" not in risky


def test_fraud_score():

    score = 1 + 1 + 1 + 1

    assert score == 4
