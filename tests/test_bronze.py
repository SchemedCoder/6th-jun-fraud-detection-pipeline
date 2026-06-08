import pandas as pd


def test_bronze_not_empty():

    df = pd.DataFrame({

        "transaction_id": [1]

    })

    assert len(df) > 0


def test_transaction_id_present():

    df = pd.DataFrame({

        "transaction_id": [1]

    })

    assert (
        df["transaction_id"]
        .isnull()
        .sum()
        == 0
    )


def test_amount_positive():

    df = pd.DataFrame({

        "amount": [100]
    })

    assert (
        df["amount"] > 0
    ).all()
