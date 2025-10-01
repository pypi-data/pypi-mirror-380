# QueueSim 📊

A Python library to **simulate and analyze Queueing Systems** (M/M/1, M/M/c, etc.)
with both **mathematical formulas** and **discrete-event simulation**.

## Features
- M/M/1 simulation
- Theoretical formulas
- Compare simulation vs theory
- Visualization (matplotlib)





## Install
```bash
pip install queuesim

from queuesim import compare_mm1

compare_mm1(arrival_rate=5, service_rate=8, max_customers=5000)