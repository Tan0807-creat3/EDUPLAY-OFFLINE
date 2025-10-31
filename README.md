# EduPlay Offline - Phần mềm tạo trò chơi học tập

Phần mềm **miễn phí, chạy offline** giúp giáo viên dễ dàng tạo và chơi các trò chơi học tập mà không cần kỹ năng lập trình, có hỗ trợ AI miễn phí (Gemini).

## Tính năng chính

- **Giao diện thân thiện**: Dễ sử dụng, không cần kiến thức lập trình
- **Tạo trò chơi trắc nghiệm**: Thêm câu hỏi, đáp án một cách dễ dàng
- **Hỗ trợ AI**: Tự động sinh câu hỏi theo chủ đề bằng Gemini AI
- **Xuất HTML**: Tạo file HTML độc lập để chia sẻ và chơi offline
- **Chơi ngay trong app**: Xem trước và chơi game không cần trình duyệt
- **Lưu trữ dữ liệu**: Quản lý các trò chơi đã tạo

## Cài đặt

### Yêu cầu hệ thống

**Chung:**
- Python 3.11+
- Desktop environment (Windows 10/11, Ubuntu 20.04+, macOS 11+)

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-dev python3-pip
sudo apt-get install libgl1-mesa-glx libxcb-xinerama0
```

**macOS:**
```bash
brew install python@3.11
```

**Windows:**
- Tải Python từ python.org
- Đảm bảo "Add Python to PATH" được chọn khi cài đặt

### Cài đặt dependencies

**Sử dụng pip:**
```bash
pip install PySide6 google-generativeai
```

**Hoặc sử dụng uv (nhanh hơn):**
```bash
uv pip install PySide6 google-generativeai
```

### Lưu ý môi trường đặc biệt

**NixOS:**
Cần cài đặt thêm OpenGL libraries:
```bash
nix-env -iA nixpkgs.libglvnd nixpkgs.mesa
export LD_LIBRARY_PATH="/run/opengl-driver/lib:$LD_LIBRARY_PATH"
```

**Replit/Cloud environments:**
PySide6 cần desktop environment để hiển thị GUI. Trên môi trường cloud không có X11 server, bạn vẫn có thể:
- Sử dụng core modules để tạo/xuất game (xem test_demo.py)
- Chạy trên máy local để sử dụng đầy đủ GUI

## Sử dụng

### Chạy ứng dụng

```bash
python main.py
```

### Hướng dẫn nhanh

1. **Tạo trò chơi mới**: Nhấn "Tạo trò chơi mới" từ menu bên trái
2. **Nhập thông tin**: Điền tiêu đề, mô tả và các câu hỏi
3. **Sử dụng AI (tùy chọn)**: 
   - Vào "Cài đặt" để nhập Gemini API Key
   - Nhập chủ đề và nhấn "Sinh câu hỏi bằng AI"
4. **Lưu trò chơi**: Nhấn "Lưu trò chơi" để lưu vào data/games/
5. **Xuất HTML**: Nhấn "Xuất HTML" để tạo file độc lập
6. **Chơi**: Chọn "Chơi trò chơi" để chơi ngay

## Cấu hình AI

Để sử dụng tính năng AI sinh câu hỏi:

1. Đăng ký API Key miễn phí tại: https://makersuite.google.com/app/apikey
2. Vào "Cài đặt" trong ứng dụng
3. Nhập Gemini API Key
4. Lưu cài đặt

## Cấu trúc dự án

```
EduPlay_Offline/
├── main.py                 # File chính để chạy app
├── gui/                    # Giao diện PySide6
│   ├── main_window.py      # Cửa sổ chính
│   ├── sidebar_widget.py   # Menu bên trái
│   ├── game_builder.py     # Trình tạo trò chơi
│   ├── game_player.py      # Chơi game (QWebEngineView)
│   └── settings_dialog.py  # Cài đặt
├── core/                   # Logic xử lý
│   ├── file_manager.py     # Quản lý file JSON
│   ├── exporter.py         # Xuất game ra HTML
│   ├── ai_helper.py        # Tích hợp Gemini AI
│   ├── template_manager.py # Quản lý template
│   └── utils.py            # Hàm tiện ích
├── templates/              # Mẫu game HTML/CSS/JS
│   └── quiz/               # Template trắc nghiệm
├── data/                   # Dữ liệu người dùng
│   ├── games/              # Game đã tạo
│   └── settings.json       # Cấu hình
└── docs/                   # Tài liệu
```

## Giấy phép

Phần mềm mã nguồn mở, miễn phí 100%, dành cho giáo dục.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy tạo issue hoặc pull request.

## Hỗ trợ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub hoặc liên hệ qua email.
