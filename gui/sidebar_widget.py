from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                               QLabel, QFrame)
from PySide6.QtCore import Signal, Qt

class SidebarWidget(QWidget):
    new_game_clicked = Signal()
    open_game_clicked = Signal()
    play_game_clicked = Signal()
    settings_clicked = Signal()
    help_clicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setSpacing(10)
        
        title_label = QLabel("EduPlay")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #667eea;
                padding: 10px;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #e0e0e0;")
        layout.addWidget(separator)
        
        layout.addSpacing(20)
        
        self.new_game_btn = self.create_menu_button("Tạo trò chơi mới")
        self.new_game_btn.clicked.connect(self.new_game_clicked.emit)
        layout.addWidget(self.new_game_btn)
        
        self.open_game_btn = self.create_menu_button("Mở trò chơi")
        self.open_game_btn.clicked.connect(self.open_game_clicked.emit)
        layout.addWidget(self.open_game_btn)
        
        self.play_game_btn = self.create_menu_button("Chơi trò chơi")
        self.play_game_btn.clicked.connect(self.play_game_clicked.emit)
        layout.addWidget(self.play_game_btn)
        
        layout.addSpacing(20)
        
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setStyleSheet("background-color: #e0e0e0;")
        layout.addWidget(separator2)
        
        layout.addSpacing(10)
        
        self.settings_btn = self.create_menu_button("Cài đặt")
        self.settings_btn.clicked.connect(self.settings_clicked.emit)
        layout.addWidget(self.settings_btn)
        
        self.help_btn = self.create_menu_button("Hướng dẫn")
        self.help_btn.clicked.connect(self.help_clicked.emit)
        layout.addWidget(self.help_btn)
        
        layout.addStretch()
        
        self.setLayout(layout)
        self.setMaximumWidth(220)
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border-right: 1px solid #e0e0e0;
            }
        """)
    
    def create_menu_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 12px 20px;
                font-size: 14px;
                background-color: transparent;
                border: none;
                border-radius: 8px;
                color: #333;
            }
            QPushButton:hover {
                background-color: #667eea;
                color: white;
            }
            QPushButton:pressed {
                background-color: #5568d3;
            }
        """)
        return btn
