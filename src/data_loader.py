import pandas as pd


def load_ff_factors(path: str) -> pd.DataFrame:
    ff = pd.read_csv(path, skiprows=4)
    ff = ff.rename(columns={ff.columns[0]: "date"})
    ff = ff[ff["date"].astype(str).str.isnumeric()]

    ff["date"] = pd.to_datetime(ff["date"], format="%Y%m")

    for col in ["Mkt-RF", "SMB", "HML", "RF"]:
        ff[col] = ff[col].astype(float) / 100

    ff = ff.set_index("date")
    return ff


def load_sentiment(path: str) -> pd.DataFrame:
    sent = pd.read_excel(path, sheet_name="DATA")
    sent = sent[["yearmo", "SENT"]]

    sent = sent.rename(columns={
        "yearmo": "date",
        "SENT": "sentiment"
    })

    sent["date"] = pd.to_datetime(sent["date"], format="%Y%m")
    sent = sent.set_index("date")

    return sent


def merge_data(ff: pd.DataFrame, sent: pd.DataFrame) -> pd.DataFrame:
    return ff.merge(sent, left_index=True, right_index=True, how="inner")