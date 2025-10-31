# EduPlay Offline - Replit Project

## Tổng quan dự án

Phần mềm desktop Python chạy offline giúp giáo viên tạo trò chơi học tập không cần lập trình. Sử dụng PySide6 cho GUI và tích hợp Gemini AI để tự động sinh câu hỏi.

## Công nghệ

- **GUI Framework**: PySide6 (Qt for Python)
- **WebEngine**: PySide6.QtWebEngineWidgets (hiển thị HTML game)
- **AI**: Google Gemini API (tùy chọn, cần API key)
- **Lưu trữ**: JSON files trong data/games/
- **Templates**: HTML/CSS/JS thuần (không framework)

## Cấu trúc

```
├── main.py                 # Entry point
├── gui/                    # PySide6 UI components
├── core/                   # Business logic
├── templates/              # Game templates (HTML/CSS/JS)
├── data/                   # User data (games, settings)
└── docs/                   # Documentation
```

## Tính năng MVP

1. Giao diện desktop với sidebar menu
2. Game Builder: tạo quiz trắc nghiệm
3. Lưu/mở game (JSON format)
4. Xuất game ra HTML độc lập
5. QWebEngineView để chơi game
6. Tích hợp Gemini AI sinh câu hỏi
7. Settings: theme, paths, API key

## Chạy ứng dụng

```bash
python main.py
```

## Phát triển tiếp

- Thêm game templates: Matching, Drag&Drop, Word Search
- Offline AI với Ollama
- Text-to-Speech
- Đóng gói .exe với PyInstaller

## Lưu ý

- App chạy hoàn toàn offline (trừ AI feature cần internet)
- Dữ liệu lưu local trong data/
- HTML export có thể chia sẻ độc lập
