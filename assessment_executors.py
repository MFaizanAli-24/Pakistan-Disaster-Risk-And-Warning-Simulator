

from risk_prediction_engine import calculate_flood_risk, calculate_drought_risk, calculate_earthquake_risk
from utils import generate_unique_id
from storage import save_assessment_results

def perform_drought_risk_assessment():
    temperature_c = float(input("Enter temperature in Celsius (b/w 0 and 50): "))
    rainfall_mm = float(input("Enter rainfall in mm (b/w 0 and 200): "))
    soil_moisture = float(input("Enter soil moisture percentage (b/w 0 and 100): "))

    score, reasons = calculate_drought_risk(temperature_c, rainfall_mm, soil_moisture)

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
    magnitude = float(input("Enter earthquake magnitude (b/w 0 and 10): "))
    depth_km = float(input("Enter earthquake depth in km (b/w 0 and 700): "))
    distance_from_epicenter_km = float(input("Enter distance from epicenter in km (b/w 0 and 1000): "))

    score, reasons = calculate_earthquake_risk(magnitude, depth_km, distance_from_epicenter_km)
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
    rainfall_mm = float(input("Enter rainfall in mm (b/w 0 and 300): "))
    river_level_m = float(input("Enter river level in meters (b/w 0 and 20): "))
    soil_saturation = float(input("Enter soil saturation percentage (b/w 0 and 100): "))

    score, reasons = calculate_flood_risk(rainfall_mm, river_level_m, soil_saturation)
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