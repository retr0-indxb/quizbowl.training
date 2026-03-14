// Game State
let gameState = {
    level: "Varsity",
    topic: "History",
    questions: [],
    currentQuestionIndex: 0,
    score: 0,
    stats: {
        correct: 0,
        incorrect: 0,
        passed: 0,
        powers: 0
    },
    isReading: false,
    isBuzzed: false,
    readInterval: null,
    timerInterval: null,
    words: [],
    currentWordIndex: 0,
    currentPointValue: 30
};

// DOM Elements
const screens = {
    setup: document.getElementById('setup-screen'),
    game: document.getElementById('game-screen'),
    results: document.getElementById('results-screen')
};

const setupControls = {
    levels: document.querySelectorAll('#level-options .option-btn'),
    topics: document.querySelectorAll('#topic-options .option-btn'),
    startBtn: document.getElementById('start-btn')
};

const gameControls = {
    levelBadge: document.getElementById('current-level'),
    topicBadge: document.getElementById('current-topic'),
    scoreValue: document.getElementById('score-value'),
    qCurrent: document.getElementById('q-current'),
    qTotal: document.getElementById('q-total'),
    questionText: document.getElementById('question-text'),
    buzzBtn: document.getElementById('buzz-btn'),
    buzzControls: document.getElementById('buzz-controls'),
    answerInput: document.getElementById('answer-input'),
    submitBtn: document.getElementById('submit-btn'),
    answerTimer: document.getElementById('answer-timer'),
    feedbackOverlay: document.getElementById('feedback-overlay'),
    feedbackMsg: document.getElementById('feedback-msg'),
    feedbackPoints: document.getElementById('feedback-points'),
    correctAnswerReveal: document.getElementById('correct-answer-reveal'),
    actualAnswer: document.getElementById('actual-answer'),
    nextQBtn: document.getElementById('next-q-btn')
};

const resultControls = {
    finalScore: document.getElementById('final-score'),
    correctCount: document.getElementById('correct-count'),
    incorrectCount: document.getElementById('incorrect-count'),
    passedCount: document.getElementById('passed-count'),
    powersCount: document.getElementById('powers-count'),
    playAgainBtn: document.getElementById('play-again-btn')
};

// --- Initialization & Event Listeners ---

function init() {
    // Setup Selection Listeners
    setupControls.levels.forEach(btn => {
        btn.addEventListener('click', () => {
            setupControls.levels.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            gameState.level = btn.dataset.value;
        });
    });

    setupControls.topics.forEach(btn => {
        btn.addEventListener('click', () => {
            setupControls.topics.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            gameState.topic = btn.dataset.value;
        });
    });

    setupControls.startBtn.addEventListener('click', startGame);

    // Game Actions
    gameControls.buzzBtn.addEventListener('click', buzzIn);
    gameControls.submitBtn.addEventListener('click', checkAnswer);
    gameControls.answerInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') checkAnswer();
    });
    gameControls.nextQBtn.addEventListener('click', nextQuestion);

    // Results Action
    resultControls.playAgainBtn.addEventListener('click', resetToSetup);

    // Global Keybindings
    document.addEventListener('keydown', (e) => {
        if (screens.setup.classList.contains('active') && e.key === 'Enter') {
            startGame();
        } else if (screens.game.classList.contains('active')) {
            if (e.code === 'Space' && gameState.isReading && !gameState.isBuzzed && screens.game.classList.contains('active')) {
                e.preventDefault(); // Prevent scrolling
                buzzIn();
            } else if (e.key === 'Enter' && !gameControls.feedbackOverlay.classList.contains('hidden')) {
                nextQuestion();
            }
        }
    });
}

// --- Screen Transitions ---

function showScreen(screenName) {
    Object.values(screens).forEach(screen => {
        screen.classList.remove('active');
        screen.classList.add('hidden');
    });
    
    // Add small delay for DOM to apply hidden class before removing it
    setTimeout(() => {
        screens[screenName].classList.remove('hidden');
        screens[screenName].classList.add('active');
    }, 50);
}

// --- Game Logic ---

function startGame() {
    // Filter questions
    let filteredQuestions = window.questionsDB.filter(q => q.level === gameState.level);
    if (gameState.topic !== "All") {
        filteredQuestions = filteredQuestions.filter(q => q.topic === gameState.topic);
    }

    if (filteredQuestions.length === 0) {
        alert("No questions found for this Level and Topic combination! Try another.");
        return;
    }

    // Shuffle and pick up to 10 questions
    gameState.questions = filteredQuestions.sort(() => 0.5 - Math.random()).slice(0, 10);
    
    // Reset state
    gameState.currentQuestionIndex = 0;
    gameState.score = 0;
    gameState.stats = { correct: 0, incorrect: 0, passed: 0, powers: 0 };
    
    // Update UI headers
    gameControls.levelBadge.textContent = gameState.level;
    gameControls.topicBadge.textContent = gameState.topic === "All" ? "Mixed" : gameState.topic;
    gameControls.qTotal.textContent = gameState.questions.length;
    updateScoreUI();

    showScreen('game');
    loadQuestion();
}

function loadQuestion() {
    const question = gameState.questions[gameState.currentQuestionIndex];
    gameControls.qCurrent.textContent = gameState.currentQuestionIndex + 1;
    
    // Reset point value
    gameState.currentPointValue = 30;
    
    // Prepare words
    // Split by spaces, but keep formatting marks if any.
    gameState.words = question.text.split(' ').map(w => w.trim()).filter(w => w.length > 0);
    gameState.currentWordIndex = 0;
    
    // Clear display
    gameControls.questionText.innerHTML = '';
    
    // Add words to DOM as hidden spans
    gameState.words.forEach((word, index) => {
        const span = document.createElement('span');
        span.className = 'question-word';
        span.id = `word-${index}`;
        
        if (word === '(*)') {
            span.classList.add('marker');
            span.textContent = '(*)';
        } else if (word === '(+)') {
            span.classList.add('marker');
            span.textContent = '(+)';
        } else {
            span.textContent = word;
        }
        
        gameControls.questionText.appendChild(span);
        // Add space
        gameControls.questionText.appendChild(document.createTextNode(' '));
    });

    // Setup UI states
    gameControls.buzzBtn.classList.remove('hidden');
    gameControls.buzzControls.classList.add('hidden');
    gameControls.feedbackOverlay.classList.add('hidden');
    gameControls.correctAnswerReveal.classList.add('hidden');
    gameControls.answerInput.value = '';
    
    // Start reading
    gameState.isReading = true;
    gameState.isBuzzed = false;
    
    // Words reveal speed (e.g. 200ms per word = roughly 300 words per minute)
    gameState.readInterval = setInterval(revealNextWord, 200);
}

function revealNextWord() {
    if (gameState.currentWordIndex >= gameState.words.length) {
        // Finished reading
        clearInterval(gameState.readInterval);
        gameState.isReading = false;
        
        // Give 5 seconds to buzz at the end
        autoPassTimer = setTimeout(() => {
            if (!gameState.isBuzzed) handlePass();
        }, 5000);
        return;
    }

    const word = gameState.words[gameState.currentWordIndex];
    const wordSpan = document.getElementById(`word-${gameState.currentWordIndex}`);
    
    // Check for power markers to downgrade points
    if (word === '(*)') {
        gameState.currentPointValue = 20;
    } else if (word === '(+)') {
        gameState.currentPointValue = 10;
    }
    
    if (wordSpan) {
        wordSpan.classList.add('revealed');
    }
    
    gameState.currentWordIndex++;
}

let autoPassTimer = null;

function buzzIn() {
    if (!gameState.isReading && gameState.currentWordIndex >= gameState.words.length) {
        clearTimeout(autoPassTimer);
    }
    
    gameState.isBuzzed = true;
    clearInterval(gameState.readInterval);
    
    // Update UI
    gameControls.buzzBtn.classList.add('hidden');
    gameControls.buzzControls.classList.remove('hidden');
    gameControls.answerInput.focus();
    
    // Start 8s answer timer
    gameControls.answerTimer.style.transition = 'none';
    gameControls.answerTimer.style.transform = 'scaleX(1)';
    
    // Trigger reflow
    void gameControls.answerTimer.offsetWidth;
    
    gameControls.answerTimer.style.transition = 'transform 8s linear';
    gameControls.answerTimer.style.transform = 'scaleX(0)';
    
    let timeLeft = 8000;
    gameState.timerInterval = setTimeout(() => {
        handleTimeout();
    }, timeLeft);
}

function cleanString(str) {
    let cleaned = str.toLowerCase().replace(/[^\w\s]/g, '').trim();
    // Remove leading articles
    cleaned = cleaned.replace(/^(a|an|the)\s+/, '');
    return cleaned;
}

function checkAnswer() {
    if (!gameState.isBuzzed) return;
    
    clearTimeout(gameState.timerInterval);
    gameControls.answerTimer.style.transition = 'none';
    
    const userAnswer = cleanString(gameControls.answerInput.value);
    const currentQ = gameState.questions[gameState.currentQuestionIndex];
    
    // Check if user answer matches any of the acceptable answers
    const isCorrect = currentQ.answers.some(ans => {
        const cleanAns = cleanString(ans);
        return cleanAns === userAnswer;
    });

    if (isCorrect) {
        handleCorrect();
    } else {
        handleIncorrect();
    }
}

function handleCorrect() {
    gameState.score += gameState.currentPointValue;
    gameState.stats.correct++;
    
    if (gameState.currentPointValue > 10) {
        gameState.stats.powers++;
    }
    
    updateScoreUI();
    showFeedback(`CORRECT!`, `+${gameState.currentPointValue} POINTS`, 'correct', false);
}

function handleIncorrect() {
    gameState.stats.incorrect++;
    const currentQ = gameState.questions[gameState.currentQuestionIndex];
    // Reveal correct answer
    gameControls.actualAnswer.textContent = currentQ.answers[0].toUpperCase();
    showFeedback(`INCORRECT`, `0 POINTS`, 'incorrect', true);
}

function handleTimeout() {
    gameState.stats.incorrect++;
    const currentQ = gameState.questions[gameState.currentQuestionIndex];
    gameControls.actualAnswer.textContent = currentQ.answers[0].toUpperCase();
    showFeedback(`TIME'S UP`, `0 POINTS`, 'incorrect', true);
}

function handlePass() {
    gameState.stats.passed++;
    const currentQ = gameState.questions[gameState.currentQuestionIndex];
    gameControls.actualAnswer.textContent = currentQ.answers[0].toUpperCase();
    showFeedback(`PASSED`, `0 POINTS`, 'neutral', true);
}

function showFeedback(msg, points, typeClass, showAnswer) {
    gameControls.feedbackOverlay.className = `feedback-overlay ${typeClass}`;
    gameControls.feedbackMsg.textContent = msg;
    gameControls.feedbackPoints.textContent = points;
    
    if (showAnswer) {
        gameControls.correctAnswerReveal.classList.remove('hidden');
    } else {
        gameControls.correctAnswerReveal.classList.add('hidden');
    }
    
    // Reveal remainder of the question text
    document.querySelectorAll('.question-word').forEach(span => span.classList.add('revealed'));
    
    // Hide inputs
    gameControls.buzzControls.classList.add('hidden');
}

function nextQuestion() {
    gameState.currentQuestionIndex++;
    
    if (gameState.currentQuestionIndex >= gameState.questions.length) {
        showResults();
    } else {
        loadQuestion();
    }
}

function updateScoreUI() {
    gameControls.scoreValue.textContent = gameState.score;
}

// --- Results Logic ---

function showResults() {
    resultControls.finalScore.textContent = gameState.score;
    resultControls.correctCount.textContent = gameState.stats.correct;
    resultControls.incorrectCount.textContent = gameState.stats.incorrect;
    resultControls.passedCount.textContent = gameState.stats.passed;
    resultControls.powersCount.textContent = gameState.stats.powers;
    
    showScreen('results');
}

function resetToSetup() {
    showScreen('setup');
}

// Initialize on load
document.addEventListener('DOMContentLoaded', init);
