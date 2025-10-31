let selectedLeft = null;
let selectedRight = null;
let matches = [];
let score = 0;

function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

function initGame() {
    document.getElementById('title').textContent = gameData.title;
    document.getElementById('description').textContent = gameData.description;
    document.title = gameData.title;
    
    const leftColumn = document.getElementById('left-column');
    const rightColumn = document.getElementById('right-column');
    leftColumn.innerHTML = '';
    rightColumn.innerHTML = '';
    
    const questions = gameData.questions.map((q, i) => ({
        id: i,
        term: q.question,
        definition: q.options[0]
    }));
    
    const rightShuffled = shuffleArray(questions);
    
    questions.forEach((item, i) => {
        const leftItem = document.createElement('div');
        leftItem.className = 'match-item';
        leftItem.dataset.id = item.id;
        leftItem.textContent = item.term;
        leftItem.addEventListener('click', () => selectLeft(leftItem));
        leftColumn.appendChild(leftItem);
    });
    
    rightShuffled.forEach((item, i) => {
        const rightItem = document.createElement('div');
        rightItem.className = 'match-item';
        rightItem.dataset.id = item.id;
        rightItem.textContent = item.definition;
        rightItem.addEventListener('click', () => selectRight(rightItem));
        rightColumn.appendChild(rightItem);
    });
    
    matches = [];
    score = 0;
    updateScore();
}

function selectLeft(item) {
    if (item.classList.contains('matched')) return;
    
    document.querySelectorAll('#left-column .match-item').forEach(i => 
        i.classList.remove('selected'));
    item.classList.add('selected');
    selectedLeft = item;
    
    if (selectedLeft && selectedRight) {
        checkMatch();
    }
}

function selectRight(item) {
    if (item.classList.contains('matched')) return;
    
    document.querySelectorAll('#right-column .match-item').forEach(i => 
        i.classList.remove('selected'));
    item.classList.add('selected');
    selectedRight = item;
    
    if (selectedLeft && selectedRight) {
        checkMatch();
    }
}

function checkMatch() {
    if (selectedLeft.dataset.id === selectedRight.dataset.id) {
        selectedLeft.classList.add('matched');
        selectedRight.classList.add('matched');
        selectedLeft.classList.remove('selected');
        selectedRight.classList.remove('selected');
        
        matches.push({
            left: selectedLeft.dataset.id,
            right: selectedRight.dataset.id
        });
        
        score += 10;
        updateScore();
        
        if (matches.length === gameData.questions.length) {
            showResult('Hoàn thành! Điểm: ' + score, 'success');
        }
    }
    
    selectedLeft = null;
    selectedRight = null;
}

function updateScore() {
    document.getElementById('score-value').textContent = score;
}

function showResult(message, type) {
    const result = document.getElementById('result');
    result.textContent = message;
    result.className = `show ${type}`;
}

document.getElementById('check-btn').addEventListener('click', () => {
    const totalMatches = document.querySelectorAll('.matched').length / 2;
    if (totalMatches === gameData.questions.length) {
        showResult('Chính xác! Bạn đã hoàn thành!', 'success');
    } else {
        showResult(`Đã nối đúng ${totalMatches}/${gameData.questions.length} cặp`, 'error');
    }
});

document.getElementById('reset-btn').addEventListener('click', () => {
    selectedLeft = null;
    selectedRight = null;
    document.getElementById('result').classList.remove('show');
    initGame();
});

initGame();