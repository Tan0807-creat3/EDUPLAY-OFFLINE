let words = [];
let grid = [];
const gridSize = 10;
let foundWords = 0;

function initGame() {
    document.getElementById('title').textContent = gameData.title;
    document.getElementById('description').textContent = gameData.description || 'Tìm các từ trong bảng chữ cái';
    document.title = gameData.title;
    
    words = gameData.questions.map(q => q.question.toUpperCase());
    
    generateGrid();
    renderGrid();
    renderWordList();
    
    document.getElementById('total').textContent = words.length;
    document.getElementById('score-value').textContent = '0';
    foundWords = 0;
}

function generateGrid() {
    grid = Array(gridSize).fill().map(() => Array(gridSize).fill(''));
    
    words.forEach(word => {
        placeWord(word);
    });
    
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            if (grid[i][j] === '') {
                grid[i][j] = String.fromCharCode(65 + Math.floor(Math.random() * 26));
            }
        }
    }
}

function placeWord(word) {
    const directions = [
        [0, 1],
        [1, 0],
        [1, 1]
    ];
    
    let placed = false;
    let attempts = 0;
    
    while (!placed && attempts < 50) {
        const dir = directions[Math.floor(Math.random() * directions.length)];
        const row = Math.floor(Math.random() * gridSize);
        const col = Math.floor(Math.random() * gridSize);
        
        if (canPlaceWord(word, row, col, dir)) {
            for (let i = 0; i < word.length; i++) {
                grid[row + i * dir[0]][col + i * dir[1]] = word[i];
            }
            placed = true;
        }
        
        attempts++;
    }
}

function canPlaceWord(word, row, col, dir) {
    for (let i = 0; i < word.length; i++) {
        const newRow = row + i * dir[0];
        const newCol = col + i * dir[1];
        
        if (newRow >= gridSize || newCol >= gridSize) {
            return false;
        }
        
        if (grid[newRow][newCol] !== '' && grid[newRow][newCol] !== word[i]) {
            return false;
        }
    }
    
    return true;
}

function renderGrid() {
    const gridEl = document.getElementById('grid');
    gridEl.innerHTML = '';
    
    for (let i = 0; i < gridSize; i++) {
        for (let j = 0; j < gridSize; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.textContent = grid[i][j];
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener('click', handleCellClick);
            gridEl.appendChild(cell);
        }
    }
}

function renderWordList() {
    const list = document.getElementById('words-list');
    list.innerHTML = '';
    
    words.forEach(word => {
        const li = document.createElement('li');
        li.textContent = word;
        li.dataset.word = word;
        list.appendChild(li);
    });
}

function handleCellClick(e) {
    e.target.classList.toggle('selected');
}

function checkWord() {
    foundWords++;
    document.getElementById('score-value').textContent = foundWords;
}

document.getElementById('reset-btn').addEventListener('click', initGame);

initGame();