from utils import read_from_json, write_to_json
from pprint import pprint

DATA_PATH = "data/assessment_results.json"

def load_assessment_results():
    return read_from_json(DATA_PATH)

def save_assessment_results(record):
    write_to_json(record, DATA_PATH)

def view_all_assessment_results():
    results = load_assessment_results()

    if not results:
        print("No previous assessments found.")
        return

    pprint(results)
