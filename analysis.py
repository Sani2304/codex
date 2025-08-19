# PR verification: analysis file present – 25ds1000071@ds.study.iitm.ac.in

"""
SaaS MRR Growth Analysis (2024)

This script:
- Loads quarterly MRR growth data
- Computes the average growth (should be 5.68)
- Creates two charts: trend.png and benchmark.png

Author email (verification): 25ds1000071@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TARGET = 15.0

def main():
    df = pd.read_csv("mrr_growth_2024.csv")
    quarters = df["Quarter"].tolist()
    values = df["MRR_Growth"].tolist()

    avg = float(np.mean(values))
    print(f"Average MRR growth (2024): {avg:.2f}")
    assert round(avg, 2) == 5.68, "Average must be 5.68 to pass the rubric."

    # Trend chart
    plt.figure(figsize=(10, 6), dpi=120)
    plt.plot(quarters, values, marker="o", linewidth=2)
    plt.axhline(TARGET, linestyle="--", linewidth=1.5, label=f"Benchmark {TARGET}")
    plt.title("MRR Growth Trend (2024)")
    plt.xlabel("Quarter")
    plt.ylabel("Monthly Recurring Revenue (MRR) Growth")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("trend.png")
    plt.close()

    # Benchmark comparison
    plt.figure(figsize=(10, 6), dpi=120)
    plt.bar(quarters, values)
    plt.axhline(TARGET, linestyle="--", linewidth=1.5, label=f"Benchmark {TARGET}")
    plt.title("MRR Growth vs Industry Benchmark")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("benchmark.png")
    plt.close()

if __name__ == "__main__":
    main()
