let answers = [];

function initGame() {
    document.getElementById('title').textContent = gameData.title;
    document.getElementById('description').textContent = gameData.description;
    document.title = gameData.title;
    
    const container = document.getElementById('questions-container');
    container.innerHTML = '';
    answers = [];
    
    gameData.questions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';
        
        let questionText = q.question;
        const correctAnswer = q.options[q.correct_answer] || q.options[0] || '';
        answers.push(correctAnswer.toLowerCase().trim());
        
        questionText = questionText.replace(/____/g, `<input type="text" class="blank" data-index="${index}" />`);
        questionText = questionText.replace(/\[blank\]/gi, `<input type="text" class="blank" data-index="${index}" />`);
        questionText = questionText.replace(/\{blank\}/gi, `<input type="text" class="blank" data-index="${index}" />`);
        
        questionDiv.innerHTML = `<div class="question-text">${index + 1}. ${questionText}</div>`;
        container.appendChild(questionDiv);
    });
    
    document.getElementById('total').textContent = gameData.questions.length;
    document.getElementById('score-value').textContent = '0';
}

function checkAnswers() {
    const inputs = document.querySelectorAll('input.blank');
    let correct = 0;
    
    inputs.forEach((input, index) => {
        const userAnswer = input.value.toLowerCase().trim();
        const correctAnswer = answers[index];
        
        if (userAnswer === correctAnswer) {
            input.classList.add('correct');
            input.classList.remove('incorrect');
            correct++;
        } else {
            input.classList.add('incorrect');
            input.classList.remove('correct');
        }
    });
    
    document.getElementById('score-value').textContent = correct;
}

function resetGame() {
    const inputs = document.querySelectorAll('input.blank');
    inputs.forEach(input => {
        input.value = '';
        input.classList.remove('correct', 'incorrect');
    });
    document.getElementById('score-value').textContent = '0';
}

document.getElementById('check-btn').addEventListener('click', checkAnswers);
document.getElementById('reset-btn').addEventListener('click', resetGame);

initGame();