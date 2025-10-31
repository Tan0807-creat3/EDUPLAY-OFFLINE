import json
from pathlib import Path
from core.template_manager import TemplateManager
from core.utils import get_templates_dir

class GameExporter:
    
    def __init__(self):
        self.template_manager = TemplateManager()
    
    def export_to_html(self, game_data, output_path):
        game_type = game_data.get('game_type', 'quiz')
        template_path = self.template_manager.get_template_path(game_type)
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template không tồn tại: {template_path}")
        
        html_template = template_path / 'index.html'
        if not html_template.exists():
            raise FileNotFoundError(f"File index.html không tồn tại trong template {game_type}")
        
        with open(html_template, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        css_file = template_path / 'style.css'
        js_file = template_path / 'script.js'
        
        css_content = ""
        if css_file.exists():
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
        
        js_content = ""
        if js_file.exists():
            with open(js_file, 'r', encoding='utf-8') as f:
                js_content = f.read()
        
        game_data_json = json.dumps(game_data, ensure_ascii=False, indent=2)
        
        final_html = html_content.replace('{{GAME_DATA}}', game_data_json)
        final_html = final_html.replace('{{CSS_CONTENT}}', css_content)
        final_html = final_html.replace('{{JS_CONTENT}}', js_content)
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        return output_file
