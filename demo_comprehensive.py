from core.file_manager import FileManager
from core.exporter import GameExporter
from core.ai_helper import AIHelper
from core.docx_importer import DocxImporter
from core.utils import get_games_dir
from datetime import datetime
from pathlib import Path

print("=" * 60)
print("🎮 EDUPLAY OFFLINE - DEMO COMPREHENSIVE")
print("=" * 60)
print()

fm = FileManager()
exporter = GameExporter()
ai_helper = AIHelper()
docx_importer = DocxImporter()

print("📝 Test 1: Tạo Quiz game cơ bản")
print("-" * 60)

quiz_game = {
    'title': 'Quiz Toán lớp 3',
    'description': 'Bài kiểm tra về phép tính cơ bản',
    'game_type': 'quiz',
    'created': datetime.now().isoformat(),
    'questions': [
        {
            'question': '5 + 3 = ?',
            'options': ['6', '7', '8', '9'],
            'correct_answer': 2
        },
        {
            'question': '10 - 4 = ?',
            'options': ['4', '5', '6', '7'],
            'correct_answer': 2
        }
    ]
}

filepath = fm.save_game(quiz_game)
print(f"✅ Đã lưu: {filepath}")

html_path = str(filepath).replace('.json', '.html')
exporter.export_to_html(quiz_game, html_path)
print(f"✅ Đã xuất HTML: {html_path}")
print()

print("🎯 Test 2: Tạo Matching game")
print("-" * 60)

matching_game = {
    'title': 'Nối từ tiếng Anh - Tiếng Việt',
    'description': 'Ghép từ tiếng Anh với nghĩa tiếng Việt',
    'game_type': 'matching',
    'created': datetime.now().isoformat(),
    'questions': [
        {
            'question': 'Apple',
            'options': ['Quả táo'],
            'correct_answer': 0
        },
        {
            'question': 'Book',
            'options': ['Quyển sách'],
            'correct_answer': 0
        },
        {
            'question': 'Cat',
            'options': ['Con mèo'],
            'correct_answer': 0
        }
    ]
}

filepath2 = fm.save_game(matching_game)
print(f"✅ Đã lưu: {filepath2}")

html_path2 = str(filepath2).replace('.json', '.html')
exporter.export_to_html(matching_game, html_path2)
print(f"✅ Đã xuất HTML: {html_path2}")
print()

print("📚 Test 3: Test DOCX import (simulation)")
print("-" * 60)

sample_text = """
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
"""

questions = docx_importer.parse_simple_format(sample_text)
print(f"✅ Đã parse được {len(questions)} câu hỏi từ text")
for i, q in enumerate(questions, 1):
    print(f"   {i}. {q['question'][:50]}...")
print()

print("🤖 Test 4: AI Helper status")
print("-" * 60)
if ai_helper.is_available():
    print("✅ AI đã được cấu hình và sẵn sàng sử dụng")
else:
    print("ℹ️  AI chưa được cấu hình (cần GEMINI_API_KEY)")
print()

print("📋 Test 5: List tất cả games đã tạo")
print("-" * 60)
games = fm.list_games()
print(f"✅ Tìm thấy {len(games)} game(s):")
for game in games[:5]:
    print(f"   • {game['title']} ({game['type']})")
print()

print("=" * 60)
print("🎉 TẤT CẢ TESTS HOÀN THÀNH!")
print("=" * 60)
print()
print("📁 Vị trí files:")
print(f"   • Games: {get_games_dir()}")
print()
print("💡 Các tính năng đã implement:")
print("   ✅ Tạo và lưu games (quiz, matching)")
print("   ✅ Export sang HTML")
print("   ✅ Import từ text/DOCX")
print("   ✅ AI helper (cần API key)")
print("   ✅ Logo cho UI")
print("   ✅ File manager")
print()
print("🚀 Chạy 'python main.py' để mở giao diện đồ họa!")
print("   (Cần desktop environment với PySide6)")
