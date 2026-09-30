from risk_prediction_engine import (
    calculate_flood_risk,
    calculate_drought_risk,
    calculate_earthquake_risk,
    classify_risk
)

from utils import generate_unique_id, get_valid_float
from storage import save_assessment_results

def perform_drought_risk_assessment():
    temperature_c = get_valid_float(
      "Enter temperature in Celsius (0-50): ",
      0,
      50
    )
    rainfall_mm = get_valid_float(
      "Enter rainfall in mm (0-200): ",
      0,
      200
    )
    soil_moisture = get_valid_float(
      "Enter soil moisture percentage (0-100): ",
      0,
      100
    )
    
    score, reasons = calculate_drought_risk(temperature_c, rainfall_mm, soil_moisture)
    risk_level = classify_risk(score)
    print(f"\nDrought Risk Score: {score}")
    print(f"Risk Level: {risk_level}")

    if score == 0  and not reasons:
        reasons.append("No significant drought risk factors detected.")
    
    print(f"Drought Risk Score: {score}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")

    record = {
        "type" : f"D-{generate_unique_id()}",
        "temperature_c": temperature_c,
        "rainfall_mm": rainfall_mm,
        "soil_moisture": soil_moisture,
        "score": score,
        "reasons": reasons
    }

    save_assessment_results(record)

def perform_earthquake_risk_assessment():
    magnitude = get_valid_float(
      "Enter earthquake magnitude (0-10): ",
      0,
      10
    )

    depth_km = get_valid_float(
      "Enter earthquake depth in km (0-700): ",
      0,
      700
    )

    distance_from_epicenter_km = get_valid_float(
      "Enter distance from epicenter in km (0-1000): ",
      0,
      1000
    )
    
    score, reasons = calculate_earthquake_risk(magnitude, depth_km, distance_from_epicenter_km)
    risk_level = classify_risk(score)
    print(f"Earthquake Risk Score: {score}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")

    if score == 0  and not reasons:
        reasons.append("No significant earthquake risk factors detected.")
    
    record = {
        "type" : f"E-{generate_unique_id()}",
        "magnitude": magnitude,
        "depth_km": depth_km,
        "distance_from_epicenter_km": distance_from_epicenter_km,
        "score": score,
        "reasons": reasons
    }

    save_assessment_results(record)

def perform_flood_risk_assessment():
    rainfall_mm = get_valid_float(
      "Enter rainfall in mm (0-300): ",
      0,
      300
    )

    river_level_m = get_valid_float(
      "Enter river level in meters (0-20): ",
      0,
      20
    )

    soil_saturation = get_valid_float(
      "Enter soil saturation percentage (0-100): ",
      0,
      100
    )

    score, reasons = calculate_flood_risk(
      rainfall_mm,
      river_level_m,
      soil_saturation
    )

risk_level = classify_risk(score)

    print(f"Flood Risk Score: {score}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")

    if score == 0  and not reasons:
        reasons.append("No significant flood risk factors detected.")

    record = {
        "type" : f"F-{generate_unique_id()}",
        "rainfall_mm": rainfall_mm,
        "river_level_m": river_level_m,
        "soil_saturation": soil_saturation,
        "score": score,
        "reasons": reasons
    }

    save_assessment_results(record)
