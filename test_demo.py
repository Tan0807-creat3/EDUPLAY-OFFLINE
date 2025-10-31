from core.file_manager import FileManager
from core.exporter import GameExporter
from core.utils import get_games_dir
from datetime import datetime

def test_file_operations():
    print("=== Testing File Operations ===\n")
    
    fm = FileManager()
    
    demo_game = {
        'title': 'Demo Quiz - Toán lớp 3',
        'description': 'Bài kiểm tra mẫu về phép cộng và trừ',
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
            },
            {
                'question': '7 + 2 = ?',
                'options': ['8', '9', '10', '11'],
                'correct_answer': 1
            }
        ]
    }
    
    print("1. Saving demo game...")
    filepath = fm.save_game(demo_game)
    print(f"   ✓ Saved to: {filepath}\n")
    
    print("2. Loading game back...")
    loaded_game = fm.load_game(filepath)
    print(f"   ✓ Loaded: {loaded_game['title']}")
    print(f"   ✓ Questions: {len(loaded_game['questions'])}\n")
    
    print("3. Listing all games...")
    games = fm.list_games()
    print(f"   ✓ Found {len(games)} game(s)")
    for game in games:
        print(f"     - {game['title']} ({game['type']})\n")
    
    print("4. Exporting to HTML...")
    exporter = GameExporter()
    html_path = str(filepath).replace('.json', '.html')
    exporter.export_to_html(demo_game, html_path)
    print(f"   ✓ Exported to: {html_path}\n")
    
    print("=== All tests passed! ===\n")
    print(f"Game files location: {get_games_dir()}\n")
    print("You can now:")
    print("1. Run 'python main.py' to start the GUI application")
    print("2. Open the exported HTML file in a browser to play the quiz")
    print("3. Check data/games/ folder for saved files\n")

if __name__ == "__main__":
    test_file_operations()
