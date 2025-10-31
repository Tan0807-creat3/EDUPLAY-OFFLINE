from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QPushButton, QFileDialog, QTextEdit, QMessageBox)
from PySide6.QtCore import Qt
from pathlib import Path

class DocxImportDialog(QDialog):
    
    def __init__(self, docx_importer, parent=None):
        super().__init__(parent)
        self.docx_importer = docx_importer
        self.setWindowTitle("Nhập câu hỏi từ file Word")
        self.setMinimumSize(700, 600)
        self.imported_game = None
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("📄 Nhập câu hỏi từ file Word")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #667eea;")
        layout.addWidget(title)
        
        info = QLabel("""
<b>Định dạng file Word hỗ trợ:</b><br>
<br>
<b>Cách 1: Dùng ký tự đặc biệt</b><br>
Q: Câu hỏi của bạn?<br>
A: Đáp án A<br>
B: Đáp án B<br>
C: Đáp án C *<br>
D: Đáp án D<br>
<br>
<b>Cách 2: Đơn giản</b><br>
Câu hỏi của bạn?<br>
Đáp án sai 1<br>
Đáp án sai 2<br>
Đáp án đúng *<br>
Đáp án sai 3<br>
<br>
<i>Ghi chú: Dùng dấu * hoặc ✓ để đánh dấu đáp án đúng</i>
        """)
        info.setStyleSheet("background: #f8f9fa; padding: 15px; border-radius: 8px; font-size: 12px;")
        info.setWordWrap(True)
        layout.addWidget(info)
        
        file_layout = QHBoxLayout()
        self.file_label = QLabel("Chưa chọn file")
        self.file_label.setStyleSheet("color: #999;")
        file_layout.addWidget(self.file_label)
        
        browse_btn = QPushButton("Chọn file Word")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #667eea;
                color: white;
                padding: 8px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #5568d3; }
        """)
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        
        layout.addLayout(file_layout)
        
        preview_label = QLabel("Xem trước câu hỏi:")
        preview_label.setStyleSheet("font-weight: bold; margin-top: 15px;")
        layout.addWidget(preview_label)
        
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setPlaceholderText("Chọn file để xem trước câu hỏi...")
        layout.addWidget(self.preview_text)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        import_btn = QPushButton("Nhập vào Editor")
        import_btn.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                padding: 10px 30px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #45a049; }
        """)
        import_btn.clicked.connect(self.import_questions)
        buttons_layout.addWidget(import_btn)
        
        cancel_btn = QPushButton("Hủy")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #999;
                color: white;
                padding: 10px 30px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #888; }
        """)
        cancel_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(cancel_btn)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
        self.current_file = None
    
    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Chọn file Word",
            "",
            "Word Documents (*.docx);;All Files (*)"
        )
        
        if file_path:
            self.current_file = file_path
            self.file_label.setText(Path(file_path).name)
            self.file_label.setStyleSheet("color: #4caf50; font-weight: bold;")
            
            try:
                game_data = self.docx_importer.import_from_docx(file_path)
                self.imported_game = game_data
                
                preview = f"<b>Đã tìm thấy {len(game_data['questions'])} câu hỏi:</b><br><br>"
                for i, q in enumerate(game_data['questions'][:5], 1):
                    preview += f"<b>{i}. {q['question']}</b><br>"
                    for j, opt in enumerate(q['options']):
                        marker = "✓" if j == q['correct_answer'] else " "
                        preview += f"   {chr(65+j)}. {opt} {marker}<br>"
                    preview += "<br>"
                
                if len(game_data['questions']) > 5:
                    preview += f"<i>... và {len(game_data['questions']) - 5} câu hỏi khác</i>"
                
                self.preview_text.setHtml(preview)
                
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Lỗi",
                    f"Không thể đọc file:\n{str(e)}"
                )
                self.current_file = None
                self.file_label.setText("Lỗi khi đọc file")
                self.file_label.setStyleSheet("color: #f44336;")
    
    def import_questions(self):
        if not self.imported_game:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                "Vui lòng chọn file Word trước!"
            )
            return
        
        if len(self.imported_game['questions']) == 0:
            QMessageBox.warning(
                self,
                "Cảnh báo",
                "Không tìm thấy câu hỏi nào trong file!"
            )
            return
        
        self.accept()
    
    def get_imported_game(self):
        return self.imported_game
