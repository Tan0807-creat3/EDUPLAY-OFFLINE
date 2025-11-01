# Hướng dẫn phát triển EduPlay

## Kiến trúc hệ thống

### Tổng quan

EduPlay sử dụng kiến trúc MVC (Model-View-Controller):

- **Model**: `core/` - Logic nghiệp vụ, quản lý dữ liệu
- **View**: `gui/` - Giao diện PySide6
- **Controller**: Xử lý trong `gui/main_window.py`
- **Templates**: `templates/` - Game templates HTML/CSS/JS

### Cấu trúc thư mục

```
EduPlay_Offline/
├── main.py                     # Entry point
├── gui/                        # PySide6 UI components
│   ├── __init__.py
│   ├── main_window.py          # Main application window
│   ├── sidebar_widget.py       # Sidebar menu
│   ├── game_builder.py         # Game creation interface
│   ├── game_player.py          # QWebEngineView wrapper
│   └── settings_dialog.py      # Settings UI
├── core/                       # Business logic
│   ├── __init__.py
│   ├── file_manager.py         # JSON file operations
│   ├── exporter.py             # HTML export functionality
│   ├── ai_helper.py            # Gemini AI integration
│   ├── template_manager.py     # Template management
│   └── utils.py                # Utility functions
├── templates/                  # Game templates
│   └── quiz/                   # Quiz game template
│       ├── index.html
│       ├── style.css
│       └── script.js
└── data/                       # User data
    ├── games/                  # Saved games (JSON)
    └── settings.json           # App settings
```

## Core Modules

### file_manager.py

Quản lý lưu trữ và đọc file JSON.

```python
from core.file_manager import FileManager

fm = FileManager()

# Lưu game
game_data = {
    'title': 'My Quiz',
    'questions': [...]
}
filepath = fm.save_game(game_data)

# Đọc game
game_data = fm.load_game(filepath)

# List tất cả games
games = fm.list_games()
```

### exporter.py

Xuất game data ra file HTML độc lập.

```python
from core.exporter import GameExporter

exporter = GameExporter()
output_path = exporter.export_to_html(game_data, 'output.html')
```

**Cơ chế hoạt động:**
1. Đọc template HTML từ `templates/{game_type}/`
2. Đọc CSS và JS files
3. Inject game data JSON vào template
4. Replace placeholders: `{{GAME_DATA}}`, `{{CSS_CONTENT}}`, `{{JS_CONTENT}}`
5. Tạo file HTML hoàn chỉnh

### ai_helper.py

Tích hợp Gemini AI để sinh câu hỏi.

```python
from core.ai_helper import AIHelper

ai = AIHelper()

if ai.is_available():
    result = ai.generate_questions(
        topic="Toán lớp 3",
        count=5,
        grade_level="Lớp 3",
        language="Tiếng Việt"
    )
    
    if result['success']:
        questions = result['questions']
```

**Format câu hỏi trả về:**

```json
{
  "success": true,
  "questions": [
    {
      "question": "2 + 2 = ?",
      "options": ["3", "4", "5", "6"],
      "correct_answer": 1
    }
  ]
}
```

### template_manager.py

Quản lý các game templates.

```python
from core.template_manager import TemplateManager

tm = TemplateManager()
template_path = tm.get_template_path('quiz')
available = tm.get_available_templates()
```

## GUI Components

### main_window.py

Cửa sổ chính chứa:
- Sidebar navigation
- Stacked widget để switch giữa các pages
- Game builder, player, settings

**Signals và slots:**
```python
# Sidebar signals
sidebar.new_game_clicked.connect(self.show_new_game)
sidebar.open_game_clicked.connect(self.show_open_game)

# Game builder signals
game_builder.game_saved.connect(self.handle_game_save)
```

### game_builder.py

Form để tạo game với:
- Input fields cho title, description
- Dynamic QuestionWidget list
- AI generation button
- Save và Export buttons

**Cách thêm câu hỏi:**
```python
builder = GameBuilder()
builder.add_question()  # Thêm 1 câu
builder.add_ai_questions(questions)  # Thêm nhiều từ AI
```

### game_player.py

Wrapper cho QWebEngineView.

```python
player = GamePlayer()
player.load_game('/path/to/game.html')
```

## Thêm Game Template mới

### 1. Tạo thư mục template

```
templates/
└── matching/
    ├── index.html
    ├── style.css
    └── script.js
```

### 2. Tạo HTML template

```html
<!DOCTYPE html>
<html>
<head>
    <style>{{CSS_CONTENT}}</style>
</head>
<body>
    <div id="gameContainer"></div>
    
    <script>
        const GAME_DATA = {{GAME_DATA}};
    </script>
    <script>{{JS_CONTENT}}</script>
</body>
</html>
```

### 3. Update template_manager.py

```python
def get_template_path(self, game_type):
    template_map = {
        'quiz': 'quiz',
        'matching': 'matching',  # Thêm dòng này
        # ...
    }
```

### 4. Thêm vào UI

Update `game_builder.py`:
```python
self.type_combo.addItems(['Trắc nghiệm', 'Nối cặp'])
```

## Game Data Format

### Quiz Game

```json
{
  "title": "Kiểm tra Toán lớp 5",
  "description": "Ôn tập phép nhân, chia",
  "game_type": "quiz",
  "created": "2023-10-30T14:30:00",
  "questions": [
    {
      "question": "5 × 7 = ?",
      "options": ["30", "35", "40", "45"],
      "correct_answer": 1
    }
  ]
}
```

## Testing

### Chạy tests

```bash
python -m pytest tests/
```

### Test thủ công

```python
# test_core.py
from core.file_manager import FileManager

fm = FileManager()
game_data = {
    'title': 'Test Game',
    'game_type': 'quiz',
    'questions': []
}

path = fm.save_game(game_data)
loaded = fm.load_game(path)
assert loaded['title'] == 'Test Game'
```

## Deployment

### Tạo executable với PyInstaller

```bash
pip install pyinstaller

pyinstaller --name="EduPlay" \
            --windowed \
            --icon=icon.ico \
            --add-data "templates:templates" \
            main.py
```

### Build cho nhiều platform

**Windows:**
```bash
pyinstaller eduplay.spec
```

**Linux:**
```bash
pyinstaller --onefile main.py
```

**macOS:**
```bash
pyinstaller --windowed --onefile main.py
```

## Best Practices

### Code Style
- Follow PEP 8
- Type hints cho functions
- Docstrings cho public methods

### Error Handling
- Try-catch cho file I/O
- Validate user input
- Show user-friendly error messages

### Performance
- Lazy load templates
- Cache AI responses (optional)
- Optimize QWebEngineView loading

## Contributing

1. Fork repository
2. Tạo feature branch: `git checkout -b feature/new-game-type`
3. Commit changes: `git commit -am 'Add matching game'`
4. Push to branch: `git push origin feature/new-game-type`
5. Tạo Pull Request

## License

MIT License - Free for educational use

## Contact

- GitHub: [https://github.com/Tan0807-creat3/EDUPLAY-OFFLINE.gitL]
- Email: tanntfx37798@funix.edu.vn
