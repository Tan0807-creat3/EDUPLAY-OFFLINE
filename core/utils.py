import os
from pathlib import Path
import json

def get_project_root():
    return Path(__file__).parent.parent

def get_data_dir():
    data_dir = get_project_root() / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def get_games_dir():
    games_dir = get_data_dir() / "games"
    games_dir.mkdir(exist_ok=True)
    return games_dir

def get_templates_dir():
    return get_project_root() / "templates"

def get_settings_path():
    return get_data_dir() / "settings.json"

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
