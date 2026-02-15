import json
import os

STATE_FILE = "state.json"

def load_state():
    default_state = {
        "objective": "Launch a new SaaS dashboard",
        "plan": ["Define feature specs", "Generate metrics", "Draft announcement"],
        "current_step_idx": 0,
        "memory": {},
        "decision_history": []
    }

    # 1. If file doesn't exist, return default
    if not os.path.exists(STATE_FILE):
        return default_state

    # 2. If file exists but is empty, return default
    if os.path.getsize(STATE_FILE) == 0:
        return default_state

    # 3. Try to load, but catch corruption errors
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Log: state.json was corrupted. Using default state.")
        return default_state

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)