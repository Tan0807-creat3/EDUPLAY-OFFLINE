let currentQuestionIndex = 0;
let score = 0;
let userAnswers = [];
let questions = [];

function initGame() {
    if (!GAME_DATA || !GAME_DATA.questions) {
        alert('Lỗi: Không tìm thấy dữ liệu câu hỏi!');
        return;
    }
    
    questions = GAME_DATA.questions;
    userAnswers = new Array(questions.length).fill(null);
    
    document.getElementById('gameTitle').textContent = GAME_DATA.title || 'Quiz Master';
    document.getElementById('gameDescription').textContent = GAME_DATA.description || '';
    document.getElementById('totalQuestions').textContent = questions.length;
    
    showQuestion(0);
}

function showQuestion(index) {
    currentQuestionIndex = index;
    const question = questions[index];
    
    document.getElementById('currentQuestion').textContent = index + 1;
    document.getElementById('questionText').textContent = question.question;
    
    const optionsContainer = document.getElementById('optionsContainer');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, i) => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'option';
        optionDiv.textContent = option;
        optionDiv.onclick = () => selectOption(i);
        
        if (userAnswers[index] === i) {
            optionDiv.classList.add('selected');
        }
        
        optionsContainer.appendChild(optionDiv);
    });
    
    updateProgress();
    updateButtons();
}

function selectOption(optionIndex) {
    userAnswers[currentQuestionIndex] = optionIndex;
    
    const options = document.querySelectorAll('.option');
    options.forEach((opt, i) => {
        opt.classList.remove('selected');
        if (i === optionIndex) {
            opt.classList.add('selected');
        }
    });
}

function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        showQuestion(currentQuestionIndex + 1);
    }
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        showQuestion(currentQuestionIndex - 1);
    }
}

function updateButtons() {
    document.getElementById('prevBtn').disabled = currentQuestionIndex === 0;
    
    if (currentQuestionIndex === questions.length - 1) {
        document.getElementById('nextBtn').style.display = 'none';
        document.getElementById('submitBtn').style.display = 'block';
    } else {
        document.getElementById('nextBtn').style.display = 'block';
        document.getElementById('submitBtn').style.display = 'none';
    }
}

function updateProgress() {
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
}

function submitQuiz() {
    const unanswered = userAnswers.filter(a => a === null).length;
    
    if (unanswered > 0) {
        if (!confirm(`Bạn còn ${unanswered} câu chưa trả lời. Bạn có chắc muốn nộp bài?`)) {
            return;
        }
    }
    
    calculateScore();
    showResults();
}

function calculateScore() {
    score = 0;
    questions.forEach((q, i) => {
        if (userAnswers[i] === q.correct_answer) {
            score++;
        }
    });
}

function showResults() {
    document.getElementById('quizContent').style.display = 'none';
    document.querySelector('.quiz-footer').style.display = 'none';
    
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.style.display = 'block';
    
    const percentage = Math.round((score / questions.length) * 100);
    document.getElementById('finalScore').textContent = `${score}/${questions.length} (${percentage}%)`;
    
    const resultDetails = document.getElementById('resultDetails');
    resultDetails.innerHTML = '';
    
    questions.forEach((q, i) => {
        const isCorrect = userAnswers[i] === q.correct_answer;
        const resultItem = document.createElement('div');
        resultItem.className = `result-item ${isCorrect ? 'correct' : 'incorrect'}`;
        
        resultItem.innerHTML = `
            <h4>Câu ${i + 1}: ${q.question}</h4>
            <p><strong>Đáp án của bạn:</strong> ${userAnswers[i] !== null ? q.options[userAnswers[i]] : 'Không trả lời'}</p>
            <p><strong>Đáp án đúng:</strong> ${q.options[q.correct_answer]}</p>
            <p><strong>${isCorrect ? '✓ Chính xác' : '✗ Sai'}</strong></p>
        `;
        
        resultDetails.appendChild(resultItem);
    });
}

function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    userAnswers = new Array(questions.length).fill(null);
    
    document.getElementById('quizContent').style.display = 'block';
    document.querySelector('.quiz-footer').style.display = 'flex';
    document.getElementById('resultContainer').style.display = 'none';
    document.getElementById('score').textContent = '0';
    
    showQuestion(0);
}

window.onload = initGame;
