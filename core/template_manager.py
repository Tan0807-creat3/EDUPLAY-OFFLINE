from pathlib import Path
from core.utils import get_templates_dir

class TemplateManager:
    
    def __init__(self):
        self.templates_dir = get_templates_dir()
    
    def get_template_path(self, game_type):
        template_map = {
            'quiz': 'quiz',
            'matching': 'matching',
            'dragdrop': 'dragdrop',
            'wordsearch': 'wordsearch'
        }
        
        template_name = template_map.get(game_type, 'quiz')
        return self.templates_dir / template_name
    
    def get_available_templates(self):
        return ['quiz', 'matching', 'dragdrop', 'wordsearch']
    
    def template_exists(self, game_type):
        template_path = self.get_template_path(game_type)
        index_file = template_path / 'index.html'
        return index_file.exists()
