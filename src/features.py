import pandas as pd


def compute_growth_dominance(df: pd.DataFrame, window: int = 24) -> pd.DataFrame:
    df = df.copy()
    df["growth_dom"] = (-df["HML"]).rolling(window).mean()
    return df


def compute_forward_returns(df: pd.DataFrame, horizon: int = 12) -> pd.DataFrame:
    df = df.copy()
    col_name = f"HML_fwd_{horizon}"

    df[col_name] = df["HML"].shift(-horizon).rolling(horizon).mean()
    return df


def compute_volatility(df: pd.DataFrame, window: int = 12) -> pd.DataFrame:
    df = df.copy()
    df["mkt_vol"] = df["Mkt-RF"].rolling(window).std()
    return df


def add_sentiment_lag(df: pd.DataFrame, lag: int = 1) -> pd.DataFrame:
    df = df.copy()
    df["sentiment_lag"] = df["sentiment"].shift(lag)
    return df