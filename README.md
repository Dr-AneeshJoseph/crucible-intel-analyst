# ⚗️ C.R.U.C.I.B.L.E. (Truth Engine)

> **The Epistemic Firewall for Intelligence Analysis.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## ⚠️ The Problem
LLMs treat all text as equal. They will happily mix a Peer-Reviewed Study (Tier 1) with a Conspiracy Blog (Tier 4) and present the average as "truth."

## 🛡️ The Solution
**C.R.U.C.I.B.L.E.** implements **Loop 1.5** of the Sledgehammer Protocol. It is a mathematical filter that assigns weight to evidence and "annihilates" weak claims when they contradict strong ones.

### The Algorithm
1.  **Tier Scoring:** T1 (1.0) -> T4 (0.2).
2.  **Time Decay:** $Score = Weight \times e^{-0.05t}$. Information degrades over time.
3.  **Annihilation:** If a claim is < 25% strength of the top claim, it is deleted.

## 🚀 Quick Start
```python
from crucible.analyst import CrucibleAnalyst
# See examples/vaccine_research.py

