import matplotlib.pyplot as plt
import pandas as pd


def plot_regime_returns(df: pd.DataFrame):
    grouped = df.groupby("narrative_regime")["HML_fwd_12"].mean()

    grouped.plot(
        kind="bar",
        title="Future Value Returns by Narrative Regime",
        figsize=(6, 4)
    )

    plt.ylabel("Average HML Return")
    plt.tight_layout()
    plt.show()


def plot_sentiment_interaction(df: pd.DataFrame):
    high_narr = df["narrative_regime"] == "High Narrative"
    high_sent = df["sentiment_regime"] == "High Sentiment"
    low_sent = df["sentiment_regime"] == "Low Sentiment"

    high_high = df.loc[high_narr & high_sent, "HML_fwd_12"].mean()
    high_low = df.loc[high_narr & low_sent, "HML_fwd_12"].mean()

    pd.Series({
        "High Narrative + High Sent": high_high,
        "High Narrative + Low Sent": high_low
    }).plot(kind="bar", figsize=(6, 4))

    plt.title("Narrative Dominance and Investor Sentiment")
    plt.ylabel("Average 12m HML Return")
    plt.tight_layout()
    plt.show()