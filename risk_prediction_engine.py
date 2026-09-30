def calculate_flood_risk(rainfall_mm, river_level_m, soil_saturation):
    score = 0
    reasons = []

    if rainfall_mm >= 120:
        score += 3
        reasons.append("Heavy rainfall")

    if river_level_m >= 7:
        score += 3
        reasons.append("High river level")

    if soil_saturation >= 80:
        score += 2
        reasons.append("High soil saturation")

    return score, reasons


def calculate_drought_risk(temperature_c, rainfall_mm, soil_moisture):
    score = 0
    reasons = []

    if temperature_c >= 35:
        score += 3
        reasons.append("High temperature")

    if rainfall_mm <= 20:
        score += 3
        reasons.append("Low rainfall")

    if soil_moisture <= 30:
        score += 2
        reasons.append("Low soil moisture")

    return score, reasons

def calculate_earthquake_risk(magnitude, depth_km, distance_from_epicenter_km):
    score = 0
    reasons = []

    if magnitude >= 7:
        score += 3
        reasons.append("High magnitude")

    if depth_km <= 10:
        score += 2
        reasons.append("Shallow depth")

    if distance_from_epicenter_km <= 50:
        score += 3
        reasons.append("Close to epicenter")

    return score, reasons