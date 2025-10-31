# EduPlay Offline - Phần mềm tạo trò chơi học tập

Phần mềm **miễn phí, chạy offline** giúp giáo viên dễ dàng tạo và chơi các trò chơi học tập mà không cần kỹ năng lập trình, có hỗ trợ AI miễn phí (Gemini).

## ✨ Tính năng chính

- **🎨 Giao diện thân thiện**: Dễ sử dụng, không cần kiến thức lập trình, có logo đẹp mắt
- **🎮 Nhiều loại trò chơi**: 
  - ✅ **Trắc nghiệm (Quiz)** - Fully supported
  - ⚡ **Nối cặp (Matching Pairs)** - Template ready (sử dụng format quiz)
  - ⚡ **Thẻ ghi nhớ (Flash Cards)** - Template ready (câu hỏi = front, đáp án A = back)
  - ⚡ **Điền từ (Fill in the Blanks)** - Template ready (dùng ____ làm chỗ trống)
  - ⚡ **Kéo thả (Drag & Drop)** - Template ready (tương tự quiz)
  - ⚡ **Tìm từ (Word Search)** - Template ready (câu hỏi = từ cần tìm)
- **🤖 Chat AI thông minh**: Tạo game tự động bằng cách chat với AI (Gemini)
- **📄 Nhập từ Word**: Import câu hỏi từ file .docx với định dạng dễ dàng
- **🎯 AI sinh câu hỏi**: Tự động sinh câu hỏi theo chủ đề bằng Gemini AI
- **📦 Xuất HTML**: Tạo file HTML độc lập để chia sẻ và chơi offline
- **🎪 Chơi ngay trong app**: Xem trước và chơi game không cần trình duyệt
- **💾 Lưu trữ dữ liệu**: Quản lý các trò chơi đã tạo

### ⚠️ Lưu ý về phiên bản hiện tại

**Game Builder UI:**
- Hiện tại, giao diện tạo câu hỏi sử dụng format chung (câu hỏi + 4 đáp án) cho tất cả game types
- Mỗi loại game có **UI hints** hướng dẫn cách nhập dữ liệu phù hợp
- **Ví dụ**: Với Flash Cards, nhập câu hỏi làm mặt trước, đáp án A làm mặt sau
- Templates HTML đã sẵn sàng cho tất cả 6 loại game
- **Phiên bản tương lai**: Sẽ có dedicated UI riêng cho từng loại game

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

#### Cách 1: Tạo game thủ công
1. **Tạo trò chơi mới**: Nhấn "Tạo trò chơi mới" từ menu bên trái
2. **Chọn loại game**: Chọn từ 6 loại (xem UI hint để biết cách nhập cho mỗi loại):
   - **Trắc nghiệm**: Nhập câu hỏi + 4 đáp án, chọn đáp án đúng
   - **Nối cặp**: Câu hỏi = thuật ngữ, Đáp án A = định nghĩa
   - **Thẻ ghi nhớ**: Câu hỏi = mặt trước, Đáp án A = mặt sau
   - **Điền từ**: Câu hỏi có ____ làm chỗ trống, chọn đáp án đúng
   - **Kéo thả**: Tương tự trắc nghiệm (hiển thị dạng drag & drop)
   - **Tìm từ**: Câu hỏi = từ cần tìm, Đáp án A = gợi ý (tùy chọn)
3. **Nhập thông tin**: Điền tiêu đề, mô tả và các câu hỏi
4. **Lưu trò chơi**: Nhấn "Lưu trò chơi" để lưu vào data/games/
5. **Xuất HTML**: Nhấn "Xuất HTML" để tạo file độc lập
6. **Chơi**: Chọn "Chơi trò chơi" để chơi ngay

#### Cách 2: Chat với AI (Nhanh nhất! 🚀)
1. **Cấu hình AI**: Vào "Cài đặt" để nhập Gemini API Key (miễn phí)
2. **Mở Chat AI**: Nhấn "🤖 Chat AI" từ menu
3. **Mô tả game**: Nhập yêu cầu (VD: "Tạo quiz về lịch sử Việt Nam với 10 câu")
4. **Nhận game**: AI tự động tạo game hoàn chỉnh cho bạn!
5. **Chỉnh sửa**: Game sẽ được load vào editor để bạn tinh chỉnh

#### Cách 3: Nhập từ file Word
1. **Chuẩn bị file**: Tạo file Word với câu hỏi theo format:
   ```
   Q: Câu hỏi của bạn?
   A: Đáp án A
   B: Đáp án B  
   C: Đáp án đúng *
   D: Đáp án D
   ```
2. **Nhập file**: Nhấn "📄 Nhập file Word" và chọn file .docx
3. **Xem trước**: Kiểm tra câu hỏi đã được nhận diện đúng
4. **Import**: Nhấn "Nhập vào Editor" để chỉnh sửa hoặc lưu luôn

## Cấu hình AI

Để sử dụng tính năng AI sinh câu hỏi:

1. Đăng ký API Key miễn phí tại: [https://makersuite.google.com/app/apikey](https://aistudio.google.com/app/api-keys)
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

## 🎮 Các loại trò chơi

| Loại trò chơi | Mô tả | Phù hợp |
|---------------|-------|---------|
| **Trắc nghiệm** | Câu hỏi nhiều lựa chọn truyền thống | Kiểm tra kiến thức tổng quát |
| **Nối cặp** | Ghép các cặp từ - nghĩa, thuật ngữ - định nghĩa | Học từ vựng, khái niệm |
| **Thẻ ghi nhớ** | Lật thẻ để xem câu hỏi và đáp án | Ghi nhớ, ôn tập |
| **Điền từ** | Điền từ còn thiếu vào chỗ trống | Ngữ pháp, từ vựng |
| **Kéo thả** | Kéo và thả đối tượng vào đúng vị trí | Phân loại, sắp xếp |
| **Tìm từ** | Tìm các từ ẩn trong bảng chữ | Từ vựng, giải trí |

## 📝 Format file Word để nhập câu hỏi

### Cách 1: Dùng ký tự đặc biệt
```
Q: Thủ đô của Việt Nam là gì?
A: Hà Nội *
B: Sài Gòn
C: Đà Nẵng
D: Huế

Câu 2: Python là ngôn ngữ gì?
A. Ngôn ngữ lập trình *
B. Ngôn ngữ tự nhiên
C. Loài rắn
D. Không biết
```

### Cách 2: Đơn giản
```
Câu hỏi của bạn?
Đáp án sai 1
Đáp án sai 2
Đáp án đúng *
Đáp án sai 3
```

**Ghi chú**: Dùng dấu `*` hoặc `✓` để đánh dấu đáp án đúng

## 🆕 Tính năng mới (v2.0)

- ✅ **Logo đẹp mắt** cho ứng dụng
- ✅ **6 loại game** thay vì chỉ 1 loại trước đây
- ✅ **Chat AI tạo game tự động** - chỉ cần mô tả, AI làm hết!
- ✅ **Nhập từ Word** - không cần gõ lại câu hỏi
- ✅ **Templates HTML đẹp** cho mỗi loại game
- ✅ **Cải thiện UI/UX** toàn diện

## Giấy phép

Phần mềm mã nguồn mở (***LICENSE MIT***), miễn phí 100%, dành cho giáo dục.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy tạo issue hoặc pull request.

## Hỗ trợ

Nếu gặp vấn đề, vui lòng tạo issue trên GitHub hoặc liên hệ qua email.

#### Email: tanntfx37798@funix.edu.vn
