import os
import json

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

class AIHelper:
    
    def __init__(self):
        self.model = None
        self.api_key = None
        self._initialize_gemini()
    
    def _initialize_gemini(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        if not self.api_key and GEMINI_AVAILABLE:
            print("Cảnh báo: Không tìm thấy GEMINI_API_KEY. Tính năng AI sẽ không khả dụng.")
            return
        
        if GEMINI_AVAILABLE and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-pro')
            except Exception as e:
                print(f"Lỗi khi khởi tạo Gemini: {e}")
    
    def is_available(self):
        return self.model is not None
    
    def generate_questions(self, topic, count=5, grade_level="", language="Tiếng Việt"):
        if not self.is_available():
            return {
                'success': False,
                'error': 'AI không khả dụng. Vui lòng cấu hình GEMINI_API_KEY.'
            }
        
        prompt = f"""Tạo {count} câu hỏi trắc nghiệm về chủ đề: {topic}
        
Cấp độ: {grade_level if grade_level else "Phù hợp"}
Ngôn ngữ: {language}

Yêu cầu định dạng JSON như sau:
{{
  "questions": [
    {{
      "question": "Nội dung câu hỏi?",
      "options": ["Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D"],
      "correct_answer": 0
    }}
  ]
}}

Chú ý:
- correct_answer là chỉ số (0-3) của đáp án đúng
- Đảm bảo câu hỏi phù hợp với cấp độ
- Trả về CHÍNH XÁC định dạng JSON, không có text khác
"""
        
        try:
            response = self.model.generate_content(prompt)
            result_text = response.text.strip()
            
            if result_text.startswith('```json'):
                result_text = result_text[7:]
            if result_text.endswith('```'):
                result_text = result_text[:-3]
            result_text = result_text.strip()
            
            data = json.loads(result_text)
            
            return {
                'success': True,
                'questions': data.get('questions', [])
            }
            
        except json.JSONDecodeError as e:
            return {
                'success': False,
                'error': f'Lỗi phân tích JSON: {e}\nPhản hồi: {result_text[:200]}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Lỗi khi tạo câu hỏi: {str(e)}'
            }
