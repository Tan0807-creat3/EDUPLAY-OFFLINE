let currentIndex = 0;
let cards = [];

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
    document.getElementById('description').textContent = gameData.description || 'Nhấn vào thẻ để lật';
    document.title = gameData.title;
    
    cards = gameData.questions.map(q => ({
        front: q.question,
        back: q.options[0] || ''
    }));
    
    showCard(0);
}

function showCard(index) {
    currentIndex = index;
    const card = document.getElementById('card');
    card.classList.remove('flipped');
    
    document.getElementById('card-front').textContent = cards[index].front;
    document.getElementById('card-back').textContent = cards[index].back;
    document.getElementById('counter').textContent = `${index + 1} / ${cards.length}`;
}

document.getElementById('card').addEventListener('click', function() {
    this.classList.toggle('flipped');
});

document.getElementById('prev-btn').addEventListener('click', () => {
    if (currentIndex > 0) {
        showCard(currentIndex - 1);
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    if (currentIndex < cards.length - 1) {
        showCard(currentIndex + 1);
    }
});

document.getElementById('shuffle-btn').addEventListener('click', () => {
    cards = shuffleArray(cards);
    showCard(0);
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        document.getElementById('prev-btn').click();
    } else if (e.key === 'ArrowRight') {
        document.getElementById('next-btn').click();
    } else if (e.key === ' ') {
        e.preventDefault();
        document.getElementById('card').click();
    }
});

initGame();