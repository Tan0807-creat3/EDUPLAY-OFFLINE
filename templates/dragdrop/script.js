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
        
        const correctAnswer = q.options[q.correct_answer] || q.options[0] || '';
        answers.push(correctAnswer.toLowerCase().trim());
        
        questionDiv.innerHTML = `
            <div class="question-text">${index + 1}. ${q.question}</div>
            <div class="drop-zone" data-index="${index}">Thả đáp án vào đây</div>
        `;
        
        container.appendChild(questionDiv);
    });
    
    const dragItemsDiv = document.createElement('div');
    dragItemsDiv.className = 'drag-items';
    
    const shuffledAnswers = shuffleArray([...answers]);
    shuffledAnswers.forEach((answer, i) => {
        const dragItem = document.createElement('div');
        dragItem.className = 'drag-item';
        dragItem.textContent = answer;
        dragItem.draggable = true;
        dragItem.dataset.answer = answer.toLowerCase().trim();
        
        dragItem.addEventListener('dragstart', handleDragStart);
        dragItemsDiv.appendChild(dragItem);
    });
    
    container.appendChild(dragItemsDiv);
    
    document.querySelectorAll('.drop-zone').forEach(zone => {
        zone.addEventListener('dragover', handleDragOver);
        zone.addEventListener('drop', handleDrop);
    });
    
    document.getElementById('total').textContent = gameData.questions.length;
    document.getElementById('score-value').textContent = '0';
}

function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

function handleDragStart(e) {
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', e.target.outerHTML);
    e.dataTransfer.setData('answer', e.target.dataset.answer);
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault();
    }
    e.dataTransfer.dropEffect = 'move';
    return false;
}

function handleDrop(e) {
    if (e.stopPropagation) {
        e.stopPropagation();
    }
    
    const answer = e.dataTransfer.getData('answer');
    const html = e.dataTransfer.getData('text/html');
    
    e.target.innerHTML = html;
    
    const newItem = e.target.querySelector('.drag-item');
    if (newItem) {
        newItem.draggable = false;
    }
    
    return false;
}

function checkAnswers() {
    let correct = 0;
    
    document.querySelectorAll('.drop-zone').forEach(zone => {
        const index = parseInt(zone.dataset.index);
        const dragItem = zone.querySelector('.drag-item');
        
        if (dragItem) {
            const userAnswer = dragItem.dataset.answer;
            const correctAnswer = answers[index];
            
            if (userAnswer === correctAnswer) {
                dragItem.classList.add('correct');
                dragItem.classList.remove('incorrect');
                correct++;
            } else {
                dragItem.classList.add('incorrect');
                dragItem.classList.remove('correct');
            }
        }
    });
    
    document.getElementById('score-value').textContent = correct;
}

function resetGame() {
    initGame();
}

document.getElementById('check-btn').addEventListener('click', checkAnswers);
document.getElementById('reset-btn').addEventListener('click', resetGame);

initGame();