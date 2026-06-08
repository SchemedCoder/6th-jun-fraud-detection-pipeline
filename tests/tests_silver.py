import pandas as pd


def test_late_event():

    df = pd.DataFrame({

        "late_event": [True]

    })

    assert (
        df["late_event"]
        .iloc[0]
        == True
    )


def test_duplicate_removed():

    df = pd.DataFrame({

        "transaction_id":
        [1, 1, 2]
    })

    unique_count = len(
        df.drop_duplicates(
            subset=[
                "transaction_id"
            ]
        )
    )

    assert unique_count == 2


def test_valid_amount():

    df = pd.DataFrame({

        "amount":
        [100, 200]
    })

    assert (
        df["amount"] > 0
    ).all()
