# Changelog

All notable changes to EduPlay Offline will be documented in this file.

## [0.1.0] - 2024-10-30

### Added

#### Core Features
- Desktop application với PySide6
- Sidebar navigation với 5 menu chính
- Game Builder interface cho trò chơi trắc nghiệm
- Quản lý file JSON (save/load/delete)
- HTML export functionality
- QWebEngineView game player
- Settings dialog với API key management

#### Game Templates
- Quiz Master template (HTML/CSS/JS)
  - 4-option multiple choice
  - Progress bar
  - Score tracking
  - Detailed results page
  - Restart functionality

#### AI Integration
- Gemini AI integration cho sinh câu hỏi tự động
- Support cho topic, count, grade level
- Error handling và user feedback
- API key management trong settings

#### File System
- Auto-create `data/games/` directory
- JSON storage cho game data
- Settings persistence trong `data/settings.json`
- .gitignore cho user data

#### Documentation
- README.md - Quick start guide
- teacher_manual.md - Hướng dẫn chi tiết cho giáo viên
- developer_guide.md - Technical documentation
- features.md - Feature specifications
- changelog.md - Lịch sử phiên bản

#### Project Structure
```
├── main.py
├── gui/ (5 modules)
├── core/ (5 modules)
├── templates/quiz/
├── data/
└── docs/ (4 files)
```

### Technical Details

**Dependencies:**
- PySide6 6.10.0
- google-generativeai (latest)
- Python 3.11+

**Code Statistics:**
- ~1500 lines of Python
- ~300 lines of HTML/CSS/JS
- 10 Python modules
- 1 complete game template

## [Unreleased]

### Planned for 0.2.0
- Matching Pairs game template
- Drag & Drop game template
- Word Search game template
- Flash Cards template
- Offline AI support (Ollama)
- Text-to-Speech integration
- Theme system (Light/Dark)

### Planned for 0.3.0
- SQLite database migration
- Advanced analytics
- PDF export
- Cloud sync (optional)
- Collaborative features

### Planned for 1.0.0
- Complete documentation
- PyInstaller build scripts
- Multi-platform testing
- Performance optimization
- Production-ready stability
- Installer packages

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version: Incompatible API changes
- MINOR version: New features (backward compatible)
- PATCH version: Bug fixes

## Links

- [GitHub Repository](#)
- [Documentation](#)
- [Issue Tracker](#)
- [Releases](#)
