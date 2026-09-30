RISK_LEVELS = [
    (0,1,"Low"),
    (2,3,"Medium"),
    (4,5,"High"),
    (6,8,"Critical")
]

def classify_risk(score):
    for lower, upper, level in RISK_LEVELS:
        if lower <= score <= upper:
            return level
    return "Unknown"
