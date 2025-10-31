from PySide6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
                               QStackedWidget, QLabel, QFileDialog, QMessageBox,
                               QListWidget, QListWidgetItem, QPushButton)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
import os
from pathlib import Path

from gui.sidebar_widget import SidebarWidget
from gui.game_builder import GameBuilder
from gui.game_player import GamePlayer
from gui.settings_dialog import SettingsDialog

from core.file_manager import FileManager
from core.exporter import GameExporter
from core.ai_helper import AIHelper
from core.utils import get_settings_path, load_json

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.file_manager = FileManager()
        self.exporter = GameExporter()
        self.ai_helper = AIHelper()
        self.current_game_data = None
        self.current_game_file = None
        
        self.load_app_settings()
        
        self.setWindowTitle("EduPlay Offline - Phần mềm tạo trò chơi học tập")
        self.setGeometry(100, 100, 1200, 800)
        
        self.init_ui()
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        self.sidebar = SidebarWidget()
        self.sidebar.new_game_clicked.connect(self.show_new_game)
        self.sidebar.open_game_clicked.connect(self.show_open_game)
        self.sidebar.play_game_clicked.connect(self.show_play_game)
        self.sidebar.settings_clicked.connect(self.show_settings)
        self.sidebar.help_clicked.connect(self.show_help)
        main_layout.addWidget(self.sidebar)
        
        self.content_stack = QStackedWidget()
        
        self.welcome_page = self.create_welcome_page()
        self.content_stack.addWidget(self.welcome_page)
        
        self.game_builder = GameBuilder()
        self.game_builder.game_saved.connect(self.handle_game_save)
        self.game_builder.ai_generate_btn.clicked.connect(self.generate_ai_questions)
        self.content_stack.addWidget(self.game_builder)
        
        self.open_game_page = self.create_open_game_page()
        self.content_stack.addWidget(self.open_game_page)
        
        self.game_player = GamePlayer()
        self.content_stack.addWidget(self.game_player)
        
        self.help_page = self.create_help_page()
        self.content_stack.addWidget(self.help_page)
        
        main_layout.addWidget(self.content_stack)
        
        self.content_stack.setCurrentWidget(self.welcome_page)
    
    def create_welcome_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Chào mừng đến với EduPlay")
        title.setFont(QFont("Arial", 32, QFont.Bold))
        title.setStyleSheet("color: #667eea;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Tạo trò chơi học tập dễ dàng, không cần lập trình")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setStyleSheet("color: #666; margin-top: 10px;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        layout.addSpacing(50)
        
        info = QLabel("Hãy bắt đầu bằng cách chọn một tùy chọn từ menu bên trái")
        info.setStyleSheet("color: #999;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        return page
    
    def create_open_game_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Mở trò chơi đã lưu")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #667eea;")
        layout.addWidget(title)
        
        self.games_list = QListWidget()
        self.games_list.itemDoubleClicked.connect(self.load_selected_game)
        layout.addWidget(self.games_list)
        
        buttons_layout = QHBoxLayout()
        
        refresh_btn = QPushButton("Làm mới")
        refresh_btn.clicked.connect(self.refresh_games_list)
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #667eea;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #5568d3; }
        """)
        buttons_layout.addWidget(refresh_btn)
        
        load_btn = QPushButton("Mở")
        load_btn.clicked.connect(self.load_selected_game)
        load_btn.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #45a049; }
        """)
        buttons_layout.addWidget(load_btn)
        
        delete_btn = QPushButton("Xóa")
        delete_btn.clicked.connect(self.delete_selected_game)
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #d32f2f; }
        """)
        buttons_layout.addWidget(delete_btn)
        
        buttons_layout.addStretch()
        layout.addLayout(buttons_layout)
        
        return page
    
    def create_help_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        
        title = QLabel("Hướng dẫn sử dụng EduPlay")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #667eea;")
        layout.addWidget(title)
        
        help_text = QLabel("""
        <h3>Cách sử dụng:</h3>
        <ol>
            <li><b>Tạo trò chơi mới:</b> Nhấn "Tạo trò chơi mới" để bắt đầu tạo một trò chơi trắc nghiệm mới.</li>
            <li><b>Nhập thông tin:</b> Điền tiêu đề, mô tả và các câu hỏi cho trò chơi của bạn.</li>
            <li><b>Sử dụng AI (tùy chọn):</b> Nhập chủ đề và nhấn "Sinh câu hỏi bằng AI" để tự động tạo câu hỏi.</li>
            <li><b>Lưu trò chơi:</b> Nhấn "Lưu trò chơi" để lưu vào thư mục data/games.</li>
            <li><b>Xuất HTML:</b> Nhấn "Xuất HTML" để tạo file HTML độc lập có thể chơi trên trình duyệt.</li>
            <li><b>Chơi trò chơi:</b> Chọn "Chơi trò chơi" để chơi ngay trong ứng dụng.</li>
        </ol>
        
        <h3>Cấu hình AI:</h3>
        <p>Để sử dụng tính năng AI sinh câu hỏi tự động:</p>
        <ol>
            <li>Vào mục "Cài đặt"</li>
            <li>Nhập Gemini API Key (lấy miễn phí tại Google AI Studio)</li>
            <li>Lưu cài đặt và bắt đầu sử dụng!</li>
        </ol>
        
        <h3>Lưu ý:</h3>
        <ul>
            <li>Phần mềm hoàn toàn miễn phí và chạy offline (trừ tính năng AI)</li>
            <li>Dữ liệu được lưu tại thư mục data/games</li>
            <li>File HTML xuất ra có thể chia sẻ và chạy độc lập</li>
        </ul>
        """)
        help_text.setWordWrap(True)
        help_text.setStyleSheet("font-size: 14px; line-height: 1.6;")
        layout.addWidget(help_text)
        
        layout.addStretch()
        
        return page
    
    def show_new_game(self):
        self.game_builder.title_input.clear()
        self.game_builder.desc_input.clear()
        self.current_game_file = None
        self.content_stack.setCurrentWidget(self.game_builder)
    
    def show_open_game(self):
        self.refresh_games_list()
        self.content_stack.setCurrentWidget(self.open_game_page)
    
    def show_play_game(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Chọn file HTML game để chơi",
            "",
            "HTML Files (*.html)"
        )
        
        if file_path:
            self.game_player.load_game(file_path)
            self.content_stack.setCurrentWidget(self.game_player)
    
    def show_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec():
            self.load_app_settings()
    
    def show_help(self):
        self.content_stack.setCurrentWidget(self.help_page)
    
    def handle_game_save(self, game_data):
        sender = self.sender()
        
        try:
            file_path = self.file_manager.save_game(game_data, self.current_game_file)
            self.current_game_file = file_path.name
            
            if sender == self.game_builder and sender.sender() == self.game_builder.findChild(QPushButton, ""):
                export_path = file_path.parent / f"{file_path.stem}.html"
                self.exporter.export_to_html(game_data, export_path)
                
                QMessageBox.information(
                    self,
                    "Thành công",
                    f"Đã lưu và xuất game thành công!\n\nFile JSON: {file_path}\nFile HTML: {export_path}"
                )
            else:
                QMessageBox.information(
                    self,
                    "Thành công",
                    f"Đã lưu game thành công vào:\n{file_path}"
                )
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lưu game:\n{str(e)}")
    
    def refresh_games_list(self):
        self.games_list.clear()
        games = self.file_manager.list_games()
        
        for game in games:
            item = QListWidgetItem(f"{game['title']} ({game['type']})")
            item.setData(Qt.UserRole, game['filepath'])
            self.games_list.addItem(item)
    
    def load_selected_game(self):
        current_item = self.games_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một game để mở!")
            return
        
        filepath = current_item.data(Qt.UserRole)
        
        try:
            game_data = self.file_manager.load_game(filepath)
            self.current_game_file = Path(filepath).name
            self.game_builder.load_game(game_data)
            self.content_stack.setCurrentWidget(self.game_builder)
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể mở game:\n{str(e)}")
    
    def delete_selected_game(self):
        current_item = self.games_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một game để xóa!")
            return
        
        filepath = current_item.data(Qt.UserRole)
        game_title = current_item.text()
        
        reply = QMessageBox.question(
            self,
            "Xác nhận xóa",
            f"Bạn có chắc muốn xóa game:\n{game_title}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                self.file_manager.delete_game(filepath)
                self.refresh_games_list()
                QMessageBox.information(self, "Thành công", "Đã xóa game!")
            except Exception as e:
                QMessageBox.critical(self, "Lỗi", f"Không thể xóa game:\n{str(e)}")
    
    def generate_ai_questions(self):
        topic = self.game_builder.ai_topic_input.text().strip()
        if not topic:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập chủ đề!")
            return
        
        if not self.ai_helper.is_available():
            QMessageBox.warning(
                self,
                "AI không khả dụng",
                "Vui lòng cấu hình Gemini API Key trong phần Cài đặt để sử dụng tính năng này."
            )
            return
        
        count = self.game_builder.ai_count_spin.value()
        
        self.game_builder.ai_generate_btn.setEnabled(False)
        self.game_builder.ai_generate_btn.setText("Đang tạo...")
        
        QTimer.singleShot(100, lambda: self._generate_ai_questions_async(topic, count))
    
    def _generate_ai_questions_async(self, topic, count):
        result = self.ai_helper.generate_questions(topic, count)
        
        self.game_builder.ai_generate_btn.setEnabled(True)
        self.game_builder.ai_generate_btn.setText("Sinh câu hỏi bằng AI")
        
        if result['success']:
            questions = result['questions']
            self.game_builder.add_ai_questions(questions)
            QMessageBox.information(
                self,
                "Thành công",
                f"Đã tạo {len(questions)} câu hỏi tự động!"
            )
        else:
            QMessageBox.critical(
                self,
                "Lỗi",
                f"Không thể tạo câu hỏi:\n{result.get('error', 'Lỗi không xác định')}"
            )
    
    def load_app_settings(self):
        settings = load_json(get_settings_path())
        if settings and settings.get('gemini_api_key'):
            os.environ['GEMINI_API_KEY'] = settings['gemini_api_key']
            self.ai_helper._initialize_gemini()
