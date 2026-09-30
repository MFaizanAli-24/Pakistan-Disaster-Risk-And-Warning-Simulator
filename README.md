# PakAlert
### Pakistan Disaster Risk & Warning Simulator

PakAlert is a Python-based educational disaster-risk simulator that converts environmental observations into simple, explainable risk assessments.

The project currently supports flood, drought, and earthquake-related assessments. Rather than using machine learning or presenting itself as a real forecasting system, PakAlert uses transparent rule-based algorithms so that every result can be traced back to the conditions that produced it.

## Why I Built It

Disaster warnings are often based on several environmental factors rather than a single measurement.

PakAlert explores how a computer program can take multiple inputs, apply a structured decision-making process, and produce an understandable result.

The main goal was to build a project where the logic remains visible instead of simply returning a prediction with no explanation.

## Current Features

- Flood risk assessment
- Drought risk assessment
- Earthquake impact assessment
- Rule-based scoring system
- Low, Moderate, High, and Critical risk classification
- Explanation of contributing risk factors
- District/location recording
- Automatic timestamps
- Unique assessment IDs
- JSON-based assessment history
- Ability to view previous assessments

## How It Works

Each assessment uses different environmental inputs.

For example, the flood assessment considers:

- Recent rainfall
- River level
- Soil saturation

Each condition is checked against predefined thresholds.

If a condition indicates greater risk, points are added to the total score.

Example:

```text
Rainfall: 300 mm
River Level: 20 m
Soil Saturation: 100%

Risk Score: 8
Risk Level: Critical

Reasons:
- Heavy rainfall
- High river level
- High soil saturation
