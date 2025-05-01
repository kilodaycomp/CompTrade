# Thousand Day Compounding Growth
- 📈📈📈 CompTrade 📈📈📈
- A project tracking the power of daily compounding growth over 3 years, simulating a 0.31% daily growth rate.

## Overview
This project simulates and tracks a financial growth journey where:
- Timeline: May 1, 2025 - April 30, 2028
- Daily Growth Rate: 0.33% on working days
- Starting Amount: 10_46_810 ¥
- Target Amount: 13_719_308 ¥
- Growth time: 13_719_308/10_46_810 = 13.1 times
- Total Days: 1095
- Working Days: 781

## Key Features
- 📊 Daily compound growth calculations
- 📝 Automated audit report generation
- ✅ Actual vs Projected balance tracking
- 📈 CSV data export for analysis
- 🔄 Easy daily balance updates

## Purpose
This serves as a tracker to understand the impact of consistent compound growth. It's particularly useful for:
- Visualizing long-term compound growth effects
- Visualizing the power of consistent small gains
- Tracking personal growth goals


## Prerequisites
- Python 3.8+
- [Just](https://github.com/casey/just) command runner

## Setup
1. Clone the repository:

```bash
git clone https://github.com/kilodaycomp/KiloDayComp
cd KiloDayComp
```

2. Install dependencies:
```bash
just install
```

3. Run the program: check commands
```bash
just
```

## Usage
The program provides two main commands:
1. Generate an audit report:
```bash
just generate
```

2. Update today's balance:
```bash
just update
```


