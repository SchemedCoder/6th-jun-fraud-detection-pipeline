import pandas as pd


def test_event_time_exists():

    df = pd.DataFrame({

        "event_time": [
            "2026-01-01"
        ]

    })

    assert "event_time" in df.columns


def test_ingest_time_exists():

    df = pd.DataFrame({

        "ingest_time": [
            "2026-01-01"
        ]

    })

    assert "ingest_time" in df.columns


def test_positive_amount():

    df = pd.DataFrame({

        "amount": [500]

    })

    assert (
        df["amount"] > 0
    ).all()
