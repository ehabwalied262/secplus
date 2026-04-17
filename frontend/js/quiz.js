class QuizEngine {
    constructor() {
        this.questions = [];
        this.currentIndex = 0;
        this.score = 0;
        this.objectiveId = new URLSearchParams(window.location.search).get('obj');
        this.init();
    }

    async init() {
        if (!this.objectiveId) {
            window.location.href = 'index.html';
            return;
        }
        
        const data = await window.API.getQuestions(this.objectiveId);
        this.questions = this.shuffle(data);
        this.renderQuestion();
    }

    shuffle(array) {
        return array.sort(() => Math.random() - 0.5);
    }

    renderQuestion() {
        const container = document.getElementById('quiz-container');
        if (this.currentIndex >= this.questions.length) {
            this.showResults();
            return;
        }

        const q = this.questions[this.currentIndex];
        container.innerHTML = `
            <div class="quiz-card">
                <div class="quiz-header">
                    <span>Objective ${q.domain_number}</span>
                    <span>${this.currentIndex + 1} / ${this.questions.length}</span>
                </div>
                <h2 class="question-text">${q.question}</h2>
                <div class="options-grid">
                    ${q.options.map((opt, i) => `
                        <button class="option-btn" onclick="quiz.handleAnswer(${i})">${opt}</button>
                    `).join('')}
                </div>
                <div id="feedback" class="hidden">
                    <p id="feedback-text"></p>
                    <p class="explanation">${q.explanation}</p>
                    <button class="primary-btn" onclick="quiz.nextQuestion()">Next Question</button>
                </div>
            </div>
        `;
    }

    handleAnswer(index) {
        const q = this.questions[this.currentIndex];
        const buttons = document.querySelectorAll('.option-btn');
        const feedback = document.getElementById('feedback');
        const feedbackText = document.getElementById('feedback-text');

        buttons.forEach(btn => btn.disabled = true);
        
        if (index === q.correct_index) {
            this.score++;
            buttons[index].classList.add('correct');
            feedbackText.innerText = "Correct! 🎉";
        } else {
            buttons[index].classList.add('wrong');
            buttons[q.correct_index].classList.add('correct');
            feedbackText.innerText = "Incorrect.";
        }

        feedback.classList.remove('hidden');
    }

    nextQuestion() {
        this.currentIndex++;
        this.renderQuestion();
    }

    showResults() {
        const percentage = Math.round((this.score / this.questions.length) * 100);
        const container = document.getElementById('quiz-container');
        
        // Save progress
        const stats = JSON.parse(localStorage.getItem('secplus_stats') || '{}');
        stats[this.objectiveId] = { score: this.score, total: this.questions.length, date: new Date() };
        localStorage.setItem('secplus_stats', JSON.stringify(stats));

        container.innerHTML = `
            <div class="results-card">
                <h1>Quiz Complete!</h1>
                <div class="score-circle">${percentage}%</div>
                <p>You got ${this.score} out of ${this.questions.length} correct.</p>
                <button class="primary-btn" onclick="window.location.href='index.html'">Back to Objectives</button>
            </div>
        `;
    }
}

const quiz = new QuizEngine();
window.quiz = quiz;