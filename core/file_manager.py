import json
from pathlib import Path
from datetime import datetime
from core.utils import get_games_dir, load_json, save_json

class FileManager:
    
    def save_game(self, game_data, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            title = game_data.get('title', 'untitled').replace(' ', '_')
            filename = f"{title}_{timestamp}.json"
        
        filepath = get_games_dir() / filename
        save_json(filepath, game_data)
        return filepath
    
    def load_game(self, filepath):
        data = load_json(filepath)
        if data:
            return data
        raise FileNotFoundError(f"Không thể tải game từ {filepath}")
    
    def list_games(self):
        games_dir = get_games_dir()
        game_files = list(games_dir.glob("*.json"))
        
        games = []
        for file_path in game_files:
            data = load_json(file_path)
            if data:
                games.append({
                    'filename': file_path.name,
                    'filepath': str(file_path),
                    'title': data.get('title', 'Không có tiêu đề'),
                    'type': data.get('game_type', 'unknown'),
                    'created': data.get('created', '')
                })
        
        return sorted(games, key=lambda x: x.get('created', ''), reverse=True)
    
    def delete_game(self, filepath):
        Path(filepath).unlink(missing_ok=True)
