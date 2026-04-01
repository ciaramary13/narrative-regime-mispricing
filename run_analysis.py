from src.data_loader import load_ff_factors, load_sentiment, merge_data
from src.features import (
    compute_growth_dominance,
    compute_forward_returns,
    compute_volatility,
    add_sentiment_lag
)
from src.regimes import assign_narrative_regimes, assign_sentiment_regimes
from src.regression import run_interaction_regression, run_regression_with_volatility
from src.plots import (
    plot_regime_returns,
    plot_sentiment_interaction,
    plot_text_validation
)
from src.text_data import build_trends_narrative_score, save_trends_data
from src.text_signals import assign_text_narrative_regimes
import matplotlib
matplotlib.use("Agg")


FF_PATH = "data/raw/F-F_Research_Data_Factors.csv"
SENT_PATH = "data/raw/SENTIMENT.xlsx"


def main():

    ff = load_ff_factors(FF_PATH)
    sent = load_sentiment(SENT_PATH)

    df = merge_data(ff, sent)

    df = compute_growth_dominance(df)
    df = compute_forward_returns(df, 12)
    df = compute_forward_returns(df, 6)
    df = compute_volatility(df)
    df = add_sentiment_lag(df)

    df = assign_narrative_regimes(df)
    df = assign_sentiment_regimes(df)

    trends_df = build_trends_narrative_score()
    save_trends_data(trends_df)

    df = df.merge(trends_df, left_index=True, right_index=True, how="left")

    df = assign_text_narrative_regimes(df)


    df = df.dropna(subset=[
        "HML_fwd_12",
        "growth_dom",
        "sentiment_lag",
        "text_narrative_score"
    ])

    print("\n--- Text Validation Correlation ---")
    print(df[["growth_dom", "text_narrative_score"]].corr())

    print("\n--- Text Narrative Regimes ---")
    print(df.groupby("text_narrative_regime")["HML_fwd_12"].mean())

    model1 = run_interaction_regression(df)
    model2 = run_regression_with_volatility(df)

    print("\n--- Regression Results ---")
    print(model1.summary())
    print(model2.summary())

    plot_regime_returns(df)
    plot_sentiment_interaction(df)
    plot_text_validation(df)

    latest = df.iloc[-1]

    print("\n--- Current Market State ---")
    print(f"Narrative Regime: {latest['narrative_regime']}")
    print(f"Sentiment Regime: {latest['sentiment_regime']}")
    print(f"Text Narrative Regime: {latest['text_narrative_regime']}")


if __name__ == "__main__":
    main()