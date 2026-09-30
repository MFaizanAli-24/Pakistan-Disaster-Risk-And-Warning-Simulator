RISK_LEVELS = [
    (0,2,"Low"),
    (3,5,"Medium"),
    (6,8,"High"),
    (9,100,"Critical")
]

def classify_risk(score):
    for lower, upper, level in RISK_LEVELS:
        if lower <= score <= upper:
            return level
    return "Unknown"