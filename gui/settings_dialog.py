from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QComboBox, QFileDialog,
                               QGroupBox, QMessageBox)
from PySide6.QtCore import Qt
import os
from core.utils import get_settings_path, load_json, save_json

class SettingsDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cài đặt")
        self.setModal(True)
        self.resize(600, 400)
        self.init_ui()
        self.load_settings()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("Cài đặt ứng dụng")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #667eea;")
        layout.addWidget(title)
        
        ai_group = QGroupBox("Cấu hình AI")
        ai_layout = QVBoxLayout()
        
        api_key_layout = QHBoxLayout()
        api_key_label = QLabel("Gemini API Key:")
        api_key_label.setMinimumWidth(150)
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Nhập API Key (tùy chọn)")
        self.api_key_input.setEchoMode(QLineEdit.Password)
        api_key_layout.addWidget(api_key_label)
        api_key_layout.addWidget(self.api_key_input)
        ai_layout.addLayout(api_key_layout)
        
        api_info = QLabel("Lấy API Key miễn phí tại: https://makersuite.google.com/app/apikey")
        api_info.setStyleSheet("color: #666; font-size: 12px;")
        api_info.setWordWrap(True)
        ai_layout.addWidget(api_info)
        
        ai_group.setLayout(ai_layout)
        layout.addWidget(ai_group)
        
        appearance_group = QGroupBox("Giao diện")
        appearance_layout = QVBoxLayout()
        
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        theme_label.setMinimumWidth(150)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(['Sáng', 'Tối'])
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        appearance_layout.addLayout(theme_layout)
        
        appearance_group.setLayout(appearance_layout)
        layout.addWidget(appearance_group)
        
        path_group = QGroupBox("Đường dẫn")
        path_layout = QVBoxLayout()
        
        save_path_layout = QHBoxLayout()
        save_path_label = QLabel("Thư mục lưu:")
        save_path_label.setMinimumWidth(150)
        self.save_path_input = QLineEdit()
        browse_btn = QPushButton("Duyệt...")
        browse_btn.clicked.connect(self.browse_folder)
        save_path_layout.addWidget(save_path_label)
        save_path_layout.addWidget(self.save_path_input)
        save_path_layout.addWidget(browse_btn)
        path_layout.addLayout(save_path_layout)
        
        path_group.setLayout(path_layout)
        layout.addWidget(path_group)
        
        layout.addStretch()
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        save_btn = QPushButton("Lưu")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #667eea;
                color: white;
                padding: 10px 30px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #5568d3; }
        """)
        save_btn.clicked.connect(self.save_settings)
        buttons_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Hủy")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                color: #333;
                padding: 10px 30px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #d0d0d0; }
        """)
        cancel_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(cancel_btn)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục lưu game")
        if folder:
            self.save_path_input.setText(folder)
    
    def load_settings(self):
        settings = load_json(get_settings_path())
        if settings:
            self.api_key_input.setText(settings.get('gemini_api_key', ''))
            
            theme = settings.get('theme', 'Sáng')
            index = self.theme_combo.findText(theme)
            if index >= 0:
                self.theme_combo.setCurrentIndex(index)
            
            self.save_path_input.setText(settings.get('save_path', ''))
    
    def save_settings(self):
        settings = {
            'gemini_api_key': self.api_key_input.text().strip(),
            'theme': self.theme_combo.currentText(),
            'save_path': self.save_path_input.text().strip()
        }
        
        save_json(get_settings_path(), settings)
        
        if settings['gemini_api_key']:
            os.environ['GEMINI_API_KEY'] = settings['gemini_api_key']
        
        QMessageBox.information(self, "Thành công", "Đã lưu cài đặt!")
        self.accept()
