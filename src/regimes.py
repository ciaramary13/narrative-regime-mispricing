import pandas as pd


def assign_narrative_regimes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    high_thresh = df["growth_dom"].quantile(0.7)
    low_thresh = df["growth_dom"].quantile(0.3)

    df["narrative_regime"] = "Middle"
    df.loc[df["growth_dom"] > high_thresh, "narrative_regime"] = "High Narrative"
    df.loc[df["growth_dom"] < low_thresh, "narrative_regime"] = "Low Narrative"

    return df


def assign_sentiment_regimes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    high_thresh = df["sentiment_lag"].quantile(0.7)
    low_thresh = df["sentiment_lag"].quantile(0.3)

    df["sentiment_regime"] = "Middle"
    df.loc[df["sentiment_lag"] > high_thresh, "sentiment_regime"] = "High Sentiment"
    df.loc[df["sentiment_lag"] < low_thresh, "sentiment_regime"] = "Low Sentiment"

    return df