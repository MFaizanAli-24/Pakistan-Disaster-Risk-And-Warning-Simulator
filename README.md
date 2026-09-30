# PakAlert

PakAlert is a Python-based educational disaster risk simulator that assesses flood, drought, and earthquake-related risk using simple environmental inputs.

The program uses a rule-based scoring system to identify important risk factors and explain why a certain score was given.

## Features

- Flood risk assessment
- Drought risk assessment
- Earthquake impact assessment
- Explainable scoring system
- Unique assessment IDs
- District/location input
- Automatic date and time recording
- JSON-based data storage
- View previous assessments

## How It Works

The user selects a type of assessment and enters the required environmental values.

For example, flood assessment uses:

- Rainfall
- River level
- Soil saturation

The program checks the values against predefined rules, calculates a score, assigns a risk level, and explains which factors contributed to the result.

## Project Structure

`main.py`  
Runs the main menu and connects the different parts of the program.

`assessment_executors.py`  
Collects user input and performs each assessment.

`risk_prediction_engine.py`  
Contains the scoring rules for flood, drought, and earthquake assessments.

`risk_classifier.py`  
Converts numerical scores into risk levels.

`storage.py`  
Handles saving and loading assessment records.

`utils.py`  
Contains reusable functions such as JSON handling and unique ID generation.

`data/assessment_results.json`  
Stores completed assessment records.

## Technologies Used

- Python
- JSON
- UUID
- File handling
- Functions and modules
- Lists and dictionaries
- Conditional statements

## Purpose

PakAlert was created as an A-Level Computer Science project to explore how software can use environmental inputs to produce simple and explainable risk assessments.

The project is intended for educational purposes only and should not be used as an official disaster forecasting or warning system.
