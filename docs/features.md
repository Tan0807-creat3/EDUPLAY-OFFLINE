# Tính năng EduPlay

## MVP Features (Phiên bản hiện tại)

### 1. Giao diện Desktop

- **Framework**: PySide6 (Qt for Python)
- **Layout**: Sidebar + Content area
- **Style**: Modern, clean, thân thiện với người dùng

**Components:**
- Sidebar menu với 5 mục chính
- Welcome page
- Stacked widget cho navigation
- Responsive design

### 2. Game Builder (Trình tạo trò chơi)

**Inputs:**
- Tiêu đề trò chơi
- Mô tả ngắn
- Loại trò chơi (Quiz)
- Danh sách câu hỏi

**Features:**
- Thêm/xóa câu hỏi động
- 4 lựa chọn cho mỗi câu
- Chọn đáp án đúng
- Validation input

**Buttons:**
- Lưu trò chơi (JSON)
- Xuất HTML
- Sinh câu hỏi bằng AI

### 3. AI Integration (Gemini)

**Capabilities:**
- Sinh câu hỏi tự động theo chủ đề
- Hỗ trợ tiếng Việt
- Customizable: số lượng câu, cấp độ

**Configuration:**
- API Key management trong Settings
- Environment variable support
- Error handling & user feedback

**Format output:**
```json
{
  "questions": [
    {
      "question": "...",
      "options": ["A", "B", "C", "D"],
      "correct_answer": 0
    }
  ]
}
```

### 4. File Management

**Save formats:**
- JSON: Dữ liệu game
- HTML: Standalone game files

**Operations:**
- Save game
- Load game
- List games
- Delete game

**Storage:**
- `data/games/` - Game files
- `data/settings.json` - App settings
- Auto-create directories

### 5. HTML Export

**Features:**
- Single-file HTML export
- Embedded CSS & JavaScript
- Self-contained, no external dependencies
- Works offline

**Process:**
1. Load template (HTML/CSS/JS)
2. Inject game data JSON
3. Combine into single file
4. Save to disk

### 6. Game Player

**Engine**: QWebEngineView (Chromium-based)

**Features:**
- Play games within app
- Full browser features
- Supports HTML5/CSS3/ES6

**Supported files:**
- Local HTML files
- Exported game files

### 7. Quiz Master Template

**UI Features:**
- Progress bar
- Question counter
- Score display
- 4-option buttons
- Navigation (Previous/Next)
- Submit quiz button

**Gameplay:**
- Click to select answer
- Review all questions
- Submit when ready
- See detailed results

**Results page:**
- Final score & percentage
- Question-by-question breakdown
- Correct vs incorrect indicators
- Restart option

### 8. Settings

**Configurable:**
- Gemini API Key
- Theme (Light/Dark) - prepared
- Save path
- UI language - prepared

**Storage:** `data/settings.json`

### 9. Documentation

**Included:**
- README.md - Quick start
- teacher_manual.md - Hướng dẫn giáo viên
- developer_guide.md - Hướng dẫn lập trình viên
- features.md - Tài liệu này

## Roadmap Features (Tương lai)

### Game Templates

**Matching Pairs**
- Drag & drop interface
- Match terms with definitions
- Timed mode

**Drag & Drop**
- Custom zones
- Image support
- Multiple correct positions

**Word Search**
- Grid generator
- Word highlighting
- Hints system

**Flash Cards**
- Flip animation
- Study mode
- Shuffle option

**Quick Test**
- 5 questions / 1 minute
- Rapid-fire quiz
- Leaderboard

### Advanced AI Features

**Offline AI:**
- Ollama integration
- Local Gemma/LLaMA models
- No internet required

**AI Enhancements:**
- Generate from uploaded documents
- Image-based questions
- Difficulty adjustment

### Text-to-Speech

**Features:**
- Read questions aloud
- Accessibility support
- Multiple voices
- Speed control

**Library:** pyttsx3

### Enhanced UI

**Themes:**
- Light theme (default)
- Dark theme
- High contrast
- Custom colors

**Localization:**
- English interface
- Vietnamese (default)
- Support for other languages

### Export Options

**Additional formats:**
- PDF quiz sheets
- SCORM packages (for LMS)
- PowerPoint slides
- Word documents

### Collaborative Features

**Cloud sync (optional):**
- Google Drive integration
- Share via link
- Collaborative editing

### Analytics

**Track:**
- Student performance
- Question difficulty
- Time spent
- Completion rates

### Deployment

**Package formats:**
- Windows .exe (PyInstaller)
- Linux AppImage
- macOS .app
- Portable version

### Database

**Upgrade from JSON to SQLite:**
- Better performance
- Query capabilities
- Relationships
- Version control

## Technical Specs

### Requirements

**Minimum:**
- Python 3.11+
- 512MB RAM
- 100MB disk space

**Recommended:**
- Python 3.12+
- 2GB RAM
- 500MB disk space

### Dependencies

**Python packages:**
- PySide6 >= 6.10.0
- google-generativeai (for AI)

**System libraries:**
- OpenGL (for Qt)
- X11 (Linux)
- WebEngine components

### Performance

**Metrics:**
- App startup: < 3 seconds
- Game load: < 1 second
- AI generation: 5-15 seconds
- HTML export: < 1 second

### Compatibility

**Operating Systems:**
- Windows 10/11
- Ubuntu 20.04+
- macOS 11+
- Other Linux distros

**Browsers (for HTML games):**
- Chrome 90+
- Firefox 88+
- Edge 90+
- Safari 14+

## Limitations (Current Version)

1. **Single game type**: Only Quiz/Multiple choice
2. **No database**: JSON file storage only
3. **AI requires internet**: Gemini API needs connection
4. **No multiplayer**: Single-player games only
5. **Basic analytics**: No tracking/reporting
6. **Limited export**: HTML only

## Future Considerations

- WebAssembly for better game performance
- Progressive Web App (PWA) version
- Mobile app (React Native/Flutter)
- Plugin system for custom game types
- API for third-party integrations
