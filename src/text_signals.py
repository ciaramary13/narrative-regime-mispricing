import pandas as pd


def assign_text_narrative_regimes(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    high_thresh = df["text_narrative_score"].quantile(0.7)
    low_thresh = df["text_narrative_score"].quantile(0.3)

    df["text_narrative_regime"] = "Middle"
    df.loc[df["text_narrative_score"] > high_thresh, "text_narrative_regime"] = "High Text Narrative"
    df.loc[df["text_narrative_score"] < low_thresh, "text_narrative_regime"] = "Low Text Narrative"

    return df