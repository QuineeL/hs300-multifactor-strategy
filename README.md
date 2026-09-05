\# Multi-Factor Stock Selection Strategy on CSI 300: Momentum, Fundamentals, and Industry Neutralization



\## Research Question

Within the CSI 300 (HS300) constituent universe, can a multi-factor stock

selection strategy—combining momentum and fundamental factors with industry

neutralization and volatility risk control—generate a statistically significant,

risk-adjusted excess return over the benchmark index?



\## Key Findings

\- \*\*H1 (Factor Effectiveness)\*\*: The multi-factor portfolio generates an

&#x20; annualized Alpha of 5.54% relative to CSI 300, statistically significant

&#x20; (p = 0.019).

\- \*\*H2 (Industry Neutralization)\*\*: Industry-neutral stock selection improves

&#x20; the Information Ratio from 0.20 to 1.05, substantially enhancing the

&#x20; consistency of excess returns.

\- \*\*H3 (Volatility Control)\*\*: A volatility-targeting overlay (18% target)

&#x20; reduces maximum drawdown from -30.4% to -27.7% while further improving the

&#x20; Information Ratio.



\## Methodological Highlights

\- Rigorous point-in-time alignment to avoid look-ahead bias (financial report

&#x20; disclosure dates, historical index constituent snapshots)

\- Back-adjusted (post-dividend) prices to avoid momentum factor distortion

&#x20; from corporate actions

\- Brinson attribution decomposing excess returns into allocation and selection

&#x20; effects

\- Out-of-sample validation to mitigate overfitting risk



\## Project Structure

Notobook\_adj/

├── 01\_data\_download\_EN.ipynb Data acquisition (Tushare Pro API)

├── 02\_data\_clean\_EN.ipynb Data cleaning \& monthly panel construction

├── 03\_factor\_build\_EN.ipynb Factor construction (momentum/quality/value)

├── 04\_factor\_analysis\_EN.ipynb Factor validation (Rank IC/ICIR/quintile backtests)

├── 05\_portfolio\_construct\_EN.ipynb Portfolio construction \& backtesting

└── 06\_risk\_management\_EN.ipynb Risk management (Brinson attribution/volatility control)



\## Data Source

Tushare Pro API (China A-share daily prices, financial statements, SW industry classification)



\## Setup

1\. Apply for a \[Tushare Pro](https://tushare.pro) token

2\. Copy `config\_template.py` to `config.py` and fill in your token

3\. Install dependencies: `pip install pandas numpy scipy matplotlib tushare jupyter jupyterlab`

4\. Run notebooks in order (01 → 06)



\## Limitations

See the "Conclusion and Limitations" section of the full report for a

detailed discussion, including the treatment of survivorship bias,

simplified transaction cost assumptions, and edge cases in point-in-time

financial statement alignment.

