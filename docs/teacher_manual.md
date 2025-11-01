# Hướng dẫn sử dụng EduPlay cho Giáo viên

## Giới thiệu

EduPlay là phần mềm miễn phí giúp giáo viên tạo trò chơi học tập một cách dễ dàng, không cần kiến thức lập trình.

## Cài đặt

### Yêu cầu hệ thống
- Windows 10/11, Linux hoặc macOS
- Python 3.11 trở lên

### Cài đặt phần mềm

1. Tải về source code
2. Mở terminal/command prompt
3. Cài đặt dependencies:
   ```bash
   pip install PySide6 google-generativeai
   ```
4. Chạy ứng dụng:
   ```bash
   python main.py
   ```

## Hướng dẫn sử dụng

### 1. Tạo trò chơi mới

1. Nhấn **"Tạo trò chơi mới"** từ menu bên trái
2. Điền các thông tin:
   - **Tiêu đề**: Tên trò chơi (VD: "Kiểm tra Toán lớp 5")
   - **Mô tả**: Mô tả ngắn về nội dung
   - **Loại trò chơi**: Hiện tại hỗ trợ Trắc nghiệm

### 2. Nhập câu hỏi thủ công

1. Nhấn **"+ Thêm câu hỏi"** để thêm câu hỏi mới
2. Với mỗi câu hỏi:
   - Nhập nội dung câu hỏi
   - Nhập 4 đáp án (A, B, C, D)
   - Chọn đáp án đúng từ dropdown
3. Nhấn nút **"Xóa"** để xóa câu hỏi không cần thiết

### 3. Sử dụng AI để tạo câu hỏi (Tùy chọn)

#### Cấu hình API Key lần đầu:

1. Truy cập [AIstudio] (https://makersuite.google.com/app/apikey)
2. Đăng nhập bằng tài khoản Google
3. Nhấn **"Create API Key"** để tạo key miễn phí
4. Copy API Key
5. Trong EduPlay, vào **"Cài đặt"**
6. Dán API Key vào ô **"Gemini API Key"**
7. Nhấn **"Lưu"**

#### Sinh câu hỏi tự động:

1. Nhập chủ đề vào ô (VD: "Toán lớp 3 - Phép nhân")
2. Chọn số lượng câu hỏi (1-20)
3. Nhấn **"Sinh câu hỏi bằng AI"**
4. Đợi vài giây, câu hỏi sẽ được thêm tự động
5. Kiểm tra và chỉnh sửa nếu cần

### 4. Lưu trò chơi

1. Nhấn **"Lưu trò chơi"**
2. File JSON sẽ được lưu tự động trong thư mục `data/games/`
3. Tên file có dạng: `TenTroChoi_20231030_143000.json`

### 5. Xuất ra file HTML

1. Sau khi tạo xong, nhấn **"Xuất HTML"**
2. File HTML độc lập sẽ được tạo cùng thư mục với file JSON
3. File HTML này có thể:
   - Chạy trực tiếp trên trình duyệt
   - Chia sẻ qua email, USB
   - Chạy offline hoàn toàn

### 6. Chơi trò chơi

**Cách 1: Chơi trong ứng dụng**
1. Nhấn **"Chơi trò chơi"** từ menu
2. Chọn file HTML đã xuất
3. Trò chơi sẽ hiển thị ngay trong ứng dụng

**Cách 2: Chơi trên trình duyệt**
1. Mở file HTML bằng trình duyệt (Chrome, Firefox, Edge...)
2. Chơi như một trang web bình thường
3. Không cần kết nối Internet

### 7. Mở lại trò chơi đã lưu

1. Nhấn **"Mở trò chơi"** từ menu
2. Chọn game từ danh sách
3. Nhấn đúp hoặc nhấn **"Mở"**
4. Chỉnh sửa và lưu lại

### 8. Xóa trò chơi

1. Vào **"Mở trò chơi"**
2. Chọn game cần xóa
3. Nhấn **"Xóa"**
4. Xác nhận

## Mẹo sử dụng

### Tạo câu hỏi chất lượng
- Câu hỏi rõ ràng, ngắn gọn
- Các đáp án có độ dài tương đương
- Tránh đáp án "Tất cả các đáp án trên"
- Đảm bảo chỉ có 1 đáp án đúng duy nhất

### Sử dụng AI hiệu quả
- Nhập chủ đề cụ thể (VD: "Địa lý Việt Nam - Sông ngòi")
- Có thể nhập cấp độ (VD: "Toán lớp 3")
- Luôn kiểm tra lại câu hỏi AI tạo ra
- Chỉnh sửa cho phù hợp với học sinh

### Chia sẻ trò chơi
- File HTML có thể gửi qua email
- Upload lên Google Drive/OneDrive
- Copy vào USB cho học sinh
- Đăng lên website/LMS của trường

## Khắc phục sự cố

### AI không hoạt động
- Kiểm tra kết nối Internet
- Đảm bảo đã nhập đúng API Key
- Thử lại sau vài phút (có thể do giới hạn API)

### Không thấy file đã lưu
- Kiểm tra thư mục `data/games/`
- Nhấn **"Làm mới"** trong màn hình "Mở trò chơi"

### Trò chơi không hiển thị đúng
- Đảm bảo dùng trình duyệt hiện đại (Chrome, Firefox, Edge)
- Xóa cache trình duyệt
- Thử xuất lại file HTML

## Hỗ trợ

Nếu gặp vấn đề, vui lòng liên hệ qua:
- Email: support@eduplay.example
- GitHub Issues: [link repository]

---

**Chúc bạn tạo được nhiều trò chơi học tập thú vị!**
