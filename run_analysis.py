from src.data_loader import load_ff_factors, load_sentiment, merge_data
from src.features import (
    compute_growth_dominance,
    compute_forward_returns,
    compute_volatility,
    add_sentiment_lag
)
from src.regimes import assign_narrative_regimes, assign_sentiment_regimes
from src.regression import run_interaction_regression, run_regression_with_volatility
from src.plots import plot_regime_returns, plot_sentiment_interaction


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

    # regressions
    model1 = run_interaction_regression(df)
    model2 = run_regression_with_volatility(df)

    print(model1.summary())
    print(model2.summary())

    # plots
    plot_regime_returns(df)
    plot_sentiment_interaction(df)


if __name__ == "__main__":
    main()