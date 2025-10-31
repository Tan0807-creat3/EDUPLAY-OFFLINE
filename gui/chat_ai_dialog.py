from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QTextEdit, QPushButton, QLineEdit, QMessageBox)
from PySide6.QtCore import Qt

class ChatAIDialog(QDialog):
    
    def __init__(self, ai_helper, parent=None):
        super().__init__(parent)
        self.ai_helper = ai_helper
        self.setWindowTitle("Chat AI - Tạo game tự động")
        self.setMinimumSize(600, 500)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("💬 Chat với AI để tạo game")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #667eea;")
        layout.addWidget(title)
        
        info = QLabel("Mô tả game bạn muốn tạo (ví dụ: 'Tạo quiz về lịch sử Việt Nam với 10 câu hỏi')")
        info.setStyleSheet("color: #666; margin-bottom: 15px;")
        info.setWordWrap(True)
        layout.addWidget(info)
        
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setPlaceholderText("Lịch sử chat sẽ hiển thị ở đây...")
        layout.addWidget(self.chat_display)
        
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Nhập yêu cầu của bạn...")
        self.input_field.returnPressed.connect(self.send_message)
        input_layout.addWidget(self.input_field)
        
        send_btn = QPushButton("Gửi")
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #667eea;
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #5568d3; }
        """)
        send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(send_btn)
        
        layout.addLayout(input_layout)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        reset_btn = QPushButton("Làm mới chat")
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #999;
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #888; }
        """)
        reset_btn.clicked.connect(self.reset_chat)
        buttons_layout.addWidget(reset_btn)
        
        close_btn = QPushButton("Đóng")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #d32f2f; }
        """)
        close_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(close_btn)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
        self.generated_game = None
    
    def send_message(self):
        user_message = self.input_field.text().strip()
        if not user_message:
            return
        
        if not self.ai_helper.is_available():
            QMessageBox.warning(
                self,
                "AI không khả dụng",
                "Vui lòng cấu hình Gemini API Key trong phần Cài đặt."
            )
            return
        
        self.chat_display.append(f"<b>Bạn:</b> {user_message}")
        self.input_field.clear()
        self.input_field.setEnabled(False)
        
        result = self.ai_helper.chat_generate_game(user_message)
        
        self.input_field.setEnabled(True)
        
        if result['success']:
            game_data = result['game_data']
            self.generated_game = game_data
            
            self.chat_display.append(f"<b>AI:</b> Đã tạo game: <b>{game_data.get('title', 'Untitled')}</b>")
            self.chat_display.append(f"   • Loại: {game_data.get('game_type', 'unknown')}")
            self.chat_display.append(f"   • Số câu hỏi: {len(game_data.get('questions', []))}")
            self.chat_display.append("<i>Game đã được tạo! Đóng hộp thoại này để sử dụng.</i>")
            
            reply = QMessageBox.question(
                self,
                "Tạo game thành công",
                f"Đã tạo game '{game_data.get('title')}' với {len(game_data.get('questions', []))} câu hỏi.\n\nBạn có muốn sử dụng game này không?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                self.accept()
        else:
            error_msg = result.get('error', 'Lỗi không xác định')
            self.chat_display.append(f"<b style='color: red;'>Lỗi:</b> {error_msg}")
    
    def reset_chat(self):
        self.chat_display.clear()
        self.ai_helper.reset_chat()
        self.generated_game = None
        self.chat_display.append("<i>Đã làm mới chat. Bắt đầu cuộc trò chuyện mới!</i>")
    
    def get_generated_game(self):
        return self.generated_game
