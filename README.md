# Narrative Dominance and Mispricing in Equity Markets

This project investigates how dominant market narratives influence asset pricing and whether investor sentiment amplifies mispricing dynamics.

The repository replicates and extends results from:

> *“When Beliefs Become Entrenched: Narrative Dominance and Mispricing in Equity Markets”*

---

## Research Question

Do periods of narrative dominance lead to systematic mispricing in equity markets?

And does investor sentiment condition the magnitude of this effect?

---

## Core Idea

Markets are not only driven by fundamentals, but also by shared beliefs.

This project studies periods in which a single market narrative becomes entrenched — specifically, the belief that **value investing is obsolete** — and examines whether this leads to predictable reversals in value returns.

---

## Construct

Narrative dominance is proxied by sustained growth outperformance:

```
growth_dominance_t = rolling_mean(-HML_t, window=24)
```

- High values → persistent growth dominance  
- Interpreted as a **belief environment**, not mispricing itself  

Forward value returns are measured over:
- 6-month horizon  
- 12-month horizon  

---

## Empirical Design

The analysis includes:

- Regime-based comparisons (top vs bottom 30%)  
- Welch t-tests for mean differences  
- HAC (Newey–West) regressions for overlapping returns  
- Interaction effects with investor sentiment  
- Controls for market volatility  
- Robustness across alternative windows  

---

## Key Findings

- Periods of strong narrative dominance are followed by higher future value returns  
- Effects:
  - Appear in **future**, not contemporaneous returns  
  - Strengthen at longer horizons  
  - Persist after controlling for volatility  

- Investor sentiment **amplifies the effect**:
  - Mispricing is strongest in high-sentiment environments  
  - Consistent with limits to arbitrage and behavioral amplification  

---

## Project Structure

```
src/
data_loader.py # data ingestion and cleaning
features.py # signal construction
regimes.py # regime definitions
regression.py # HAC regression models
plots.py # figure generation

data/raw/ # input datasets
figures/ # output figures
paper/ # working paper

run_analysis.py # end-to-end pipeline
```

---

## Data

- Fama–French factor data (monthly)
- Baker–Wurgler investor sentiment index

---

## How to Run

```
pip install -r requirements.txt
python run_analysis.py
```

---
## Why This Matters

This project highlights how **belief dynamics and investor sentiment jointly shape mispricing in financial markets**.

Rather than treating factor performance as purely risk-based or stable through time, it shows that periods of entrenched narratives can allow mispricing to accumulate, with sentiment determining the extent of that distortion.

This provides a behavioral perspective on return predictability that complements traditional risk-based explanations.

**TL;DR:**  
Value strategies perform best following periods of extreme growth dominance, especially when investor sentiment is elevated.