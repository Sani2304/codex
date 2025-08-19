# SaaS Technology Performance Analysis — MRR Growth (2024)

This pull request provides an LLM-assisted analysis of **Monthly Recurring Revenue (MRR) growth** across 2024 quarters and compares performance against the industry **benchmark target = 15**.

> **Author (verification): 25ds1000071@ds.study.iitm.ac.in**

## Dataset
Quarterly MRR growth values used in this analysis:
- Q1 = 1.82
- Q2 = 3.30
- Q3 = 8.58
- Q4 = 9.01

**Average MRR growth (2024) = 5.68**

_Source:_ Assessment dataset in task prompt.

## How to run
```bash
pip install pandas matplotlib numpy
python analysis.py
```
This will generate two figures:
- `trend.png` — the quarterly growth trend with a benchmark line
- `benchmark.png` — bar chart with benchmark comparison

## Key Findings
- The current **average growth is 5.68**, which is **well below** the industry benchmark of 15.
- Growth accelerates from Q1 to Q4 (1.82 → 9.01), signaling improving momentum but an **absolute shortfall** remains.
- The gap to the benchmark in Q4 is **5.99 points**, indicating material runway still required.

## Business Implications
- Sustained underperformance against the benchmark risks **lost market share** and **slower ARR expansion**.
- Current growth initiatives are yielding improvements but are **insufficient** to reach industry standards in the near term without additional action.

## Recommendation (Solution)
**Expand into new market segments.**  
This includes:
1. Identify 2–3 adjacent verticals with high willingness to pay and shorter sales cycles.
2. Launch focused GTM plays (ICP-driven messaging, partner-led motions).
3. Localize pricing / packaging to reduce friction for entry segments.
4. Pilot demand generation in one new geography and one vertical to validate CAC/LTV quickly.

## LLM Assistance
This PR was prepared with assistance from an LLM code generator (e.g., ChatGPT/Codex). The model helped draft the analysis script and README narrative.

## Repo Contents
- `analysis.py` — analysis and chart generation
- `mrr_growth_2024.csv` — dataset
- `trend.png` — trend chart with benchmark
- `benchmark.png` — bar chart with benchmark
- `analysis_summary.json` — quick stats

---
PR prepared with LLM assistance.
**Contact:** 25ds1000071@ds.study.iitm.ac.in
