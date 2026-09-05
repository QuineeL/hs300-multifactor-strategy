# Conclusion and Limitations



## Results Summary



| Hypothesis | Result | Evidence |

|---|---|---|

| Multi-factor selection generates excess return | **Confirmed** | Annualized Alpha = 5.54% vs CSI 300, statistically significant (p = 0.019) |

| Industry-neutral selection improves consistency | **Confirmed** | Information Ratio improved from 0.20 to 1.05 |

| Volatility targeting improves risk-adjusted return | **Confirmed** | Max drawdown reduced from -30.4% to -27.7%, IR further improved to 0.974 |



Brinson attribution shows that **stock selection, not sector timing**, drives

80-83% of the portfolio's excess return. Industry neutralization improves

the stability of returns but does not by itself increase the magnitude of

alpha -the value in this strategy comes from picking better stocks within

each sector, not from betting on which sectors to overweight.



## Known Data Issues and How They Were Resolved



Two data issues surfaced during development and are worth flagging, since

they materially affected early-stage results before being caught:



**Incomplete historical index constituents.** An initial data pull only

returned 10 months of CSI 300 constituent history instead of the full

2015-2024 period, due to an undocumented limit on Tushare's `index\_weight`

API for single large date-range requests. This was caught by a sanity check

on the number of unique months in the dataset, and fixed by switching to

year-by-year batched requests.



**Unadjusted price data.** Stock prices were initially pulled without

back-adjustment for dividends and stock splits, which caused the momentum

factor to register false crashes for stocks that had large distributions.

This was caught by comparing factor-based backtest results against sanity

expectations, and fixed by switching to back-adjusted (`hfq`) pricing via

Tushare's `pro\_bar` endpoint.



Both are included here as part of the standard data-QA process for this

project, not as caveats on the final results â€” both were identified and

corrected before the reported numbers were finalized.



## Practical Limitations



- **Delisted stock returns** use the last traded price before suspension,

&#x20; which may understate losses for stocks that were suspended ahead of very

&#x20; sharp declines.

- **Transaction costs** are modeled as a flat 0.25% on monthly turnover

&#x20; (commission + stamp duty), without market impact or bid-ask spread. This

&#x20; is reasonable for a 30-50 stock CSI 300 portfolio but would need revisiting

&#x20; at larger AUM.

- **PE and PB are moderately correlated** (cross-sectional ρ = 0.49, IC

&#x20; series ρ = 0.70). Both are kept in the composite score rather than

&#x20; orthogonalized, since the correlation isn't severe enough to require it and

&#x20; the two metrics behave differently across sectors (e.g. asset-heavy

&#x20; financials).



## How Overfitting Was Controlled



- Momentum window (12 months) follows the standard academic convention

&#x20; (Jegadeesh \& Titman, 1993) rather than being tuned on this dataset.

- Portfolio size (N=50) was chosen from a stable region of Sharpe/IR across

&#x20; a sweep from N=10 to N=100 -not a single best-performing point.

- The volatility target (18%) was tested as one pre-specified value and

&#x20; validated on a 2021-2024 out-of-sample window, not grid-searched.



## What I'd Do Next



- Combine ATR-based stop-loss with inverse-volatility weighting to see if

&#x20; they're complementary or redundant.

- Test ICIR-weighted factor synthesis against the current equal-weighted

&#x20; composite, with a proper train/test split.

- Extend to rolling out-of-sample validation across the full sample period

&#x20; instead of a single split.


