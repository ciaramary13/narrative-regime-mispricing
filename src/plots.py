import matplotlib.pyplot as plt
import pandas as pd


def plot_regime_returns(df: pd.DataFrame, save: bool = True):
    grouped = df.groupby("narrative_regime")["HML_fwd_12"].mean()

    plt.figure(figsize=(6, 4))
    grouped.plot(
        kind="bar",
        title="Future Value Returns by Narrative Regime"
    )

    plt.ylabel("Average HML Return")
    plt.tight_layout()

    plt.savefig("figures/figure1_narrative_hml.png", dpi=300)

    plt.show()


def plot_sentiment_interaction(df: pd.DataFrame, save: bool = True):
    high_narr = df["narrative_regime"] == "High Narrative"
    high_sent = df["sentiment_regime"] == "High Sentiment"
    low_sent = df["sentiment_regime"] == "Low Sentiment"

    high_high = df.loc[high_narr & high_sent, "HML_fwd_12"].mean()
    high_low = df.loc[high_narr & low_sent, "HML_fwd_12"].mean()

    plt.figure(figsize=(6, 4))
    pd.Series({
        "High Narrative + High Sent": high_high,
        "High Narrative + Low Sent": high_low
    }).plot(kind="bar")

    plt.title("Narrative Dominance and Investor Sentiment")
    plt.ylabel("Average 12m HML Return")
    plt.tight_layout()

    plt.savefig("figures/figure2_narrative_sentiment.png", dpi=300)

    plt.show()