import pandas as pd
import statsmodels.api as sm


def run_interaction_regression(df: pd.DataFrame):
    reg_data = df[[
        "HML_fwd_12",
        "growth_dom",
        "sentiment_lag"
    ]].dropna().copy()

    reg_data["interaction"] = (
        reg_data["growth_dom"] * reg_data["sentiment_lag"]
    )

    X = reg_data[["growth_dom", "sentiment_lag", "interaction"]]
    X = sm.add_constant(X)

    y = reg_data["HML_fwd_12"]

    model = sm.OLS(y, X).fit(
        cov_type="HAC",
        cov_kwds={"maxlags": 12}
    )

    return model


def run_regression_with_volatility(df: pd.DataFrame):
    reg_data = df[[
        "HML_fwd_12",
        "growth_dom",
        "sentiment_lag",
        "mkt_vol"
    ]].dropna().copy()

    reg_data["interaction"] = (
        reg_data["growth_dom"] * reg_data["sentiment_lag"]
    )

    X = reg_data[[
        "growth_dom",
        "sentiment_lag",
        "interaction",
        "mkt_vol"
    ]]
    X = sm.add_constant(X)

    y = reg_data["HML_fwd_12"]

    model = sm.OLS(y, X).fit(
        cov_type="HAC",
        cov_kwds={"maxlags": 12}
    )

    return model