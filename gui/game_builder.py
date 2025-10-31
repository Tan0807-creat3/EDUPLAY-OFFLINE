from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QTextEdit, QPushButton, QComboBox,
                               QScrollArea, QFrame, QMessageBox, QSpinBox)
from PySide6.QtCore import Signal, Qt
from datetime import datetime

class QuestionWidget(QWidget):
    
    remove_requested = Signal(object)
    
    def __init__(self, question_number=1, parent=None):
        super().__init__(parent)
        self.question_number = question_number
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        
        header = QHBoxLayout()
        question_label = QLabel(f"Câu hỏi {self.question_number}")
        question_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #667eea;")
        header.addWidget(question_label)
        header.addStretch()
        
        remove_btn = QPushButton("Xóa")
        remove_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 6px 15px;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #d32f2f; }
        """)
        remove_btn.clicked.connect(lambda: self.remove_requested.emit(self))
        header.addWidget(remove_btn)
        layout.addLayout(header)
        
        self.question_input = QTextEdit()
        self.question_input.setPlaceholderText("Nhập câu hỏi...")
        self.question_input.setMaximumHeight(80)
        layout.addWidget(self.question_input)
        
        options_label = QLabel("Các lựa chọn:")
        options_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(options_label)
        
        self.option_inputs = []
        for i in range(4):
            option_input = QLineEdit()
            option_input.setPlaceholderText(f"Đáp án {chr(65+i)}")
            self.option_inputs.append(option_input)
            layout.addWidget(option_input)
        
        correct_layout = QHBoxLayout()
        correct_label = QLabel("Đáp án đúng:")
        self.correct_combo = QComboBox()
        self.correct_combo.addItems(['A', 'B', 'C', 'D'])
        correct_layout.addWidget(correct_label)
        correct_layout.addWidget(self.correct_combo)
        correct_layout.addStretch()
        layout.addLayout(correct_layout)
        
        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
            }
            QTextEdit, QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        """)
    
    def get_data(self):
        return {
            'question': self.question_input.toPlainText().strip(),
            'options': [opt.text().strip() for opt in self.option_inputs],
            'correct_answer': self.correct_combo.currentIndex()
        }
    
    def set_data(self, data):
        self.question_input.setPlainText(data.get('question', ''))
        options = data.get('options', ['', '', '', ''])
        for i, opt in enumerate(options[:4]):
            self.option_inputs[i].setText(opt)
        self.correct_combo.setCurrentIndex(data.get('correct_answer', 0))


class GameBuilder(QWidget):
    
    game_saved = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.question_widgets = []
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Trình tạo trò chơi")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #667eea;")
        main_layout.addWidget(title)
        
        form_layout = QVBoxLayout()
        
        title_label = QLabel("Tiêu đề trò chơi:")
        title_label.setStyleSheet("font-weight: bold;")
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Ví dụ: Kiểm tra Toán lớp 5")
        form_layout.addWidget(title_label)
        form_layout.addWidget(self.title_input)
        
        desc_label = QLabel("Mô tả:")
        desc_label.setStyleSheet("font-weight: bold;")
        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Mô tả ngắn về trò chơi...")
        self.desc_input.setMaximumHeight(80)
        form_layout.addWidget(desc_label)
        form_layout.addWidget(self.desc_input)
        
        type_layout = QHBoxLayout()
        type_label = QLabel("Loại trò chơi:")
        type_label.setStyleSheet("font-weight: bold;")
        self.type_combo = QComboBox()
        self.type_combo.addItems(['Trắc nghiệm', 'Nối cặp', 'Thẻ ghi nhớ', 'Điền từ', 'Kéo thả', 'Tìm từ'])
        self.type_combo.currentIndexChanged.connect(self.on_type_changed)
        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combo)
        type_layout.addStretch()
        form_layout.addLayout(type_layout)
        
        self.type_hint = QLabel()
        self.type_hint.setWordWrap(True)
        self.type_hint.setStyleSheet("color: #666; font-size: 12px; padding: 10px; background: #f8f9fa; border-radius: 5px;")
        form_layout.addWidget(self.type_hint)
        self.update_type_hint()
        
        main_layout.addLayout(form_layout)
        
        ai_section = QHBoxLayout()
        ai_label = QLabel("Sử dụng AI:")
        ai_section.addWidget(ai_label)
        
        self.ai_topic_input = QLineEdit()
        self.ai_topic_input.setPlaceholderText("Nhập chủ đề (VD: Toán lớp 3)")
        ai_section.addWidget(self.ai_topic_input)
        
        self.ai_count_spin = QSpinBox()
        self.ai_count_spin.setMinimum(1)
        self.ai_count_spin.setMaximum(20)
        self.ai_count_spin.setValue(5)
        self.ai_count_spin.setPrefix("Số câu: ")
        ai_section.addWidget(self.ai_count_spin)
        
        self.ai_generate_btn = QPushButton("Sinh câu hỏi bằng AI")
        self.ai_generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #9c27b0;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #7b1fa2; }
        """)
        ai_section.addWidget(self.ai_generate_btn)
        main_layout.addLayout(ai_section)
        
        questions_header = QHBoxLayout()
        questions_label = QLabel("Danh sách câu hỏi:")
        questions_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        questions_header.addWidget(questions_label)
        questions_header.addStretch()
        
        add_question_btn = QPushButton("+ Thêm câu hỏi")
        add_question_btn.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #45a049; }
        """)
        add_question_btn.clicked.connect(self.add_question)
        questions_header.addWidget(add_question_btn)
        main_layout.addLayout(questions_header)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        scroll_widget = QWidget()
        self.questions_layout = QVBoxLayout(scroll_widget)
        self.questions_layout.setSpacing(15)
        scroll.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        save_btn = QPushButton("Lưu trò chơi")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #667eea;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #5568d3; }
        """)
        save_btn.clicked.connect(self.save_game)
        buttons_layout.addWidget(save_btn)
        
        export_btn = QPushButton("Xuất HTML")
        export_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #e68900; }
        """)
        export_btn.clicked.connect(self.export_game)
        buttons_layout.addWidget(export_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.setLayout(main_layout)
        
        self.add_question()
    
    def add_question(self):
        question_widget = QuestionWidget(len(self.question_widgets) + 1)
        question_widget.remove_requested.connect(self.remove_question)
        self.questions_layout.addWidget(question_widget)
        self.question_widgets.append(question_widget)
    
    def remove_question(self, widget):
        if len(self.question_widgets) <= 1:
            QMessageBox.warning(self, "Cảnh báo", "Phải có ít nhất 1 câu hỏi!")
            return
        
        self.question_widgets.remove(widget)
        widget.deleteLater()
        
        for i, qw in enumerate(self.question_widgets):
            qw.question_number = i + 1
            qw.findChild(QLabel).setText(f"Câu hỏi {i + 1}")
    
    def on_type_changed(self):
        self.update_type_hint()
    
    def update_type_hint(self):
        type_index = self.type_combo.currentIndex()
        hints = {
            0: "Trắc nghiệm: Mỗi câu hỏi có 4 đáp án, chọn 1 đáp án đúng",
            1: "Nối cặp: Câu hỏi là thuật ngữ, Đáp án A là định nghĩa (chỉ cần điền A)",
            2: "Thẻ ghi nhớ: Câu hỏi là mặt trước, Đáp án A là mặt sau (chỉ cần điền A)",
            3: "Điền từ: Câu hỏi có ____ làm chỗ trống, đáp án đúng là từ cần điền",
            4: "Kéo thả: Tương tự trắc nghiệm, sẽ được hiển thị dạng kéo thả",
            5: "Tìm từ: Câu hỏi là từ cần tìm, đáp án A là gợi ý (không bắt buộc)"
        }
        self.type_hint.setText(f"💡 {hints.get(type_index, '')}")
    
    def get_game_data(self):
        questions = []
        for qw in self.question_widgets:
            q_data = qw.get_data()
            if q_data['question']:
                questions.append(q_data)
        
        type_map = {
            0: 'quiz',
            1: 'matching',
            2: 'flashcard',
            3: 'fillinblank',
            4: 'dragdrop',
            5: 'wordsearch'
        }
        
        return {
            'title': self.title_input.text().strip(),
            'description': self.desc_input.toPlainText().strip(),
            'game_type': type_map.get(self.type_combo.currentIndex(), 'quiz'),
            'questions': questions,
            'created': datetime.now().isoformat()
        }
    
    def save_game(self):
        data = self.get_game_data()
        
        if not data['title']:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tiêu đề trò chơi!")
            return
        
        if len(data['questions']) == 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng thêm ít nhất 1 câu hỏi!")
            return
        
        self.game_saved.emit(data)
    
    def export_game(self):
        data = self.get_game_data()
        
        if not data['title']:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tiêu đề trò chơi!")
            return
        
        if len(data['questions']) == 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng thêm ít nhất 1 câu hỏi!")
            return
        
        self.game_saved.emit(data)
    
    def load_game(self, game_data):
        self.title_input.setText(game_data.get('title', ''))
        self.desc_input.setPlainText(game_data.get('description', ''))
        
        game_type = game_data.get('game_type', 'quiz')
        type_map_reverse = {
            'quiz': 0,
            'matching': 1,
            'flashcard': 2,
            'fillinblank': 3,
            'dragdrop': 4,
            'wordsearch': 5
        }
        self.type_combo.setCurrentIndex(type_map_reverse.get(game_type, 0))
        
        for qw in self.question_widgets:
            qw.deleteLater()
        self.question_widgets.clear()
        
        questions = game_data.get('questions', [])
        if not questions:
            self.add_question()
        else:
            for q_data in questions:
                question_widget = QuestionWidget(len(self.question_widgets) + 1)
                question_widget.remove_requested.connect(self.remove_question)
                question_widget.set_data(q_data)
                self.questions_layout.addWidget(question_widget)
                self.question_widgets.append(question_widget)
    
    def add_ai_questions(self, questions):
        for q_data in questions:
            question_widget = QuestionWidget(len(self.question_widgets) + 1)
            question_widget.remove_requested.connect(self.remove_question)
            question_widget.set_data(q_data)
            self.questions_layout.addWidget(question_widget)
            self.question_widgets.append(question_widget)
