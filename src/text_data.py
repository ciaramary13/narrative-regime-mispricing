from pytrends.request import TrendReq
import pandas as pd


def fetch_google_trends_monthly(keywords, start="2004-01-01", end="2025-12-31"):
    pytrends = TrendReq(hl="en-US", tz=360)
    timeframe = f"{start} {end}"

    pytrends.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe=timeframe,
        geo="US",
        gprop=""
    )

    data = pytrends.interest_over_time()

    if "isPartial" in data.columns:
        data = data.drop(columns=["isPartial"])

    data = data.reset_index()
    data["date"] = pd.to_datetime(data["date"])
    data = data.set_index("date")

    return data


def build_trends_narrative_score():

    keywords = [
        "growth stocks",
        "tech stocks",
        "value investing",
        "value stocks"
    ]

    data = fetch_google_trends_monthly(keywords)

    df = pd.DataFrame(index=data.index)

    df["growth_attention"] = data[["growth stocks", "tech stocks"]].mean(axis=1)
    df["value_attention"] = data[["value investing", "value stocks"]].mean(axis=1)

    # FIXED score
    df["text_narrative_score"] = df["growth_attention"] - df["value_attention"]

    return df


def save_trends_data(df, path="data/processed/google_trends_narrative.csv"):
    import os
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(path)