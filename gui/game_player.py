from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from pathlib import Path

class GamePlayer(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        self.setLayout(layout)
    
    def load_game(self, html_path):
        file_path = Path(html_path).absolute()
        if file_path.exists():
            url = QUrl.fromLocalFile(str(file_path))
            self.web_view.load(url)
        else:
            self.show_error(f"Không tìm thấy file: {html_path}")
    
    def show_error(self, message):
        error_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: 'Segoe UI', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                }}
                .error-box {{
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                    text-align: center;
                }}
                h2 {{ color: #f44336; }}
                p {{ color: #666; }}
            </style>
        </head>
        <body>
            <div class="error-box">
                <h2>Lỗi</h2>
                <p>{message}</p>
            </div>
        </body>
        </html>
        """
        self.web_view.setHtml(error_html)
