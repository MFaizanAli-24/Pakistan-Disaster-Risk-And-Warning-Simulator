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

Rainfall: 300 mm  
River Level: 20 m  
Soil Saturation: 100%

Risk Score: 8  
Risk Level: Critical

Reasons:
- Heavy rainfall
- High river level
- High soil saturation

This makes the result explainable because the user can see exactly which conditions affected the score.

## Project Architecture

PakAlert/
- main.py
- assessment_executors.py
- risk_prediction_engine.py
- risk_classifier.py
- storage.py
- utils.py
- data/
  - assessment_results.json

### main.py
Controls the main program menu.

### assessment_executors.py
Collects user inputs and creates assessment records.

### risk_prediction_engine.py
Contains the scoring rules for each assessment.

### risk_classifier.py
Converts numerical scores into understandable risk levels.

### storage.py
Handles saving and loading assessment records.

### utils.py
Contains reusable functions such as UUID generation and JSON handling.

## Data Storage

Completed assessments are stored in JSON format.

Example:

{
    "assessment_type": "Flood",
    "district": "Lahore",
    "rainfall_mm": 300,
    "river_level_m": 20,
    "soil_saturation": 100,
    "score": 8,
    "risk_level": "Critical"
}

## Design Approach

PakAlert intentionally uses a rule-based model rather than machine learning.

This keeps the project:

- Understandable
- Transparent
- Easy to test
- Appropriate for the current stage of development

The scoring thresholds are part of an educational simulation and should not be treated as scientifically validated forecasting thresholds.

## Limitations

PakAlert is not connected to live weather, river, seismic, or government warning data.

It should therefore not be used for real disaster prediction or emergency decisions.

The earthquake component evaluates conditions associated with an earthquake event rather than predicting when an earthquake will occur.

## Future Improvements

Possible future versions could include:

- Search assessments by district
- Search by assessment ID
- Sort assessments by date or risk level
- Graphical interface
- Real environmental datasets
- Weather or disaster-data APIs
- Improved scientifically sourced thresholds
- Visual risk dashboards

## Purpose

PakAlert was developed as an A-Level Computer Science passion project to explore how Python can be used to model real-world decision-making problems using transparent and explainable algorithms.
