from docx import Document
from pathlib import Path
import re

class DocxImporter:
    
    def __init__(self):
        self.question_markers = ['Q:', 'Câu', 'Question:', '?']
        self.answer_markers = ['A:', 'B:', 'C:', 'D:', 'Đáp án:', 'Answer:']
        self.correct_markers = ['Đúng:', 'Correct:', 'ĐA:', '*']
    
    def import_from_docx(self, file_path):
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        
        questions = self._parse_questions(text)
        
        return {
            'title': Path(file_path).stem,
            'description': f'Nhập từ file {Path(file_path).name}',
            'game_type': 'quiz',
            'questions': questions
        }
    
    def _parse_questions(self, text):
        questions = []
        
        question_blocks = re.split(r'\n\s*\n', text)
        
        for block in question_blocks:
            lines = [l.strip() for l in block.split('\n') if l.strip()]
            if len(lines) < 2:
                continue
            
            question_text = ''
            options = []
            correct_index = 0
            
            for i, line in enumerate(lines):
                if any(marker in line for marker in self.question_markers):
                    question_text = line.split(':', 1)[-1].strip() if ':' in line else line.strip()
                
                elif re.match(r'^[A-D][:.)]', line):
                    option = re.sub(r'^[A-D][:.)]', '', line).strip()
                    if '*' in option or '✓' in option:
                        correct_index = len(options)
                        option = option.replace('*', '').replace('✓', '').strip()
                    options.append(option)
                
                elif any(marker in line for marker in self.correct_markers):
                    answer_key = line.split(':', 1)[-1].strip().upper()
                    if answer_key in ['A', 'B', 'C', 'D']:
                        correct_index = ord(answer_key) - ord('A')
            
            if question_text and len(options) >= 2:
                while len(options) < 4:
                    options.append('')
                
                questions.append({
                    'question': question_text,
                    'options': options[:4],
                    'correct_answer': min(correct_index, 3)
                })
        
        return questions
    
    def parse_simple_format(self, text):
        questions = []
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        
        i = 0
        while i < len(lines):
            if '?' in lines[i] or any(m in lines[i] for m in self.question_markers):
                question_text = lines[i]
                options = []
                correct_index = 0
                
                i += 1
                while i < len(lines) and len(options) < 4:
                    line = lines[i]
                    if '?' in line or any(m in line for m in self.question_markers):
                        break
                    
                    if line and not line.startswith('#'):
                        is_correct = '*' in line or '✓' in line
                        option = line.replace('*', '').replace('✓', '').strip()
                        
                        if option:
                            if is_correct:
                                correct_index = len(options)
                            options.append(option)
                    i += 1
                
                if len(options) >= 2:
                    while len(options) < 4:
                        options.append('')
                    
                    questions.append({
                        'question': question_text,
                        'options': options[:4],
                        'correct_answer': correct_index
                    })
            else:
                i += 1
        
        return questions
