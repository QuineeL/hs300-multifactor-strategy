# Multi-Factor Stock Selection Strategy on CSI 300: Momentum, Fundamentals, and Industry Neutralization

## Research Question

Within the CSI 300 (HS300) constituent universe, can a multi-factor stock selection strategy, combining momentum and fundamental factors with industry neutralization and volatility risk control, generate a statistically significant, risk-adjusted excess return over the benchmark index?

## Key Findings

- H1 (Factor Effectiveness): The multi-factor portfolio generates an annualized Alpha of 5.54% relative to CSI 300, statistically significant (p = 0.019).
- H2 (Industry Neutralization): Industry-neutral stock selection improves the Information Ratio from 0.20 to 1.05, substantially enhancing the consistency of excess returns.
- H3 (Volatility Control): A volatility-targeting overlay (18% target) reduces maximum drawdown from -30.4% to -27.7% while further improving the Information Ratio.

## Methodological Highlights

- Rigorous point-in-time alignment to avoid look-ahead bias
- Back-adjusted prices to avoid momentum factor distortion from corporate actions
- Brinson attribution decomposing excess returns into allocation and selection effects
- Out-of-sample validation to mitigate overfitting risk

## Project Structure

Notobook_adj folder:
- 01_data_download_EN.ipynb: Data acquisition (Tushare Pro API)
- 02_data_clean_EN.ipynb: Data cleaning and monthly panel construction
- 03_factor_build_EN.ipynb: Factor construction (momentum, quality, value)
- 04_factor_analysis_EN.ipynb: Factor validation (Rank IC, ICIR, quintile backtests)
- 05_portfolio_construct_EN.ipynb: Portfolio construction and backtesting
- 06_risk_management_EN.ipynb: Risk management (Brinson attribution, volatility control)

report folder:
- 07_conclusion_and_limitations.md: Results summary, limitations, and future directions

## Data Source

Tushare Pro API (China A-share daily prices, financial statements, SW industry classification)

## Setup

1. Apply for a Tushare Pro token at tushare.pro
2. Copy config_template.py to config.py and fill in your token
3. Install dependencies: pip install pandas numpy scipy matplotlib tushare jupyter jupyterlab
4. Run notebooks in order (01 through 06)

## Limitations

See report/07_conclusion_and_limitations.md for a detailed discussion, including the treatment of survivorship bias, simplified transaction cost assumptions, and edge cases in point-in-time financial statement alignment.
