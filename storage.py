import json
import os
from config import DATA_FILE

def load_data():
    """Loads transaction data from the JSON file."""
    # Check if the file exists first to avoid errors
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Handles the error if the file is empty or damaged
        return []

def save_data(data):
    """Saves transaction data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
