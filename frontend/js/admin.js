async function loadPending() {
    const container = document.getElementById('admin-list');
    const questions = await window.API.getUnverifiedQuestions();
    
    if (questions.length === 0) {
        container.innerHTML = "<p>All questions are verified! Good job.</p>";
        return;
    }

    container.innerHTML = questions.map(q => `
        <div class="admin-card" id="q-${q.id}">
            <div class="admin-meta">${q.domain_number} - ${q.difficulty.toUpperCase()}</div>
            <textarea class="edit-q">${q.question}</textarea>
            <div class="edit-options">
                ${q.options.map((opt, i) => `
                    <div class="opt-row ${i === q.correct_index ? 'is-correct' : ''}">
                        <input type="text" value="${opt}" data-idx="${i}">
                    </div>
                `).join('')}
            </div>
            <textarea class="edit-exp">${q.explanation}</textarea>
            <div class="admin-actions">
                <button class="approve-btn" onclick="verify('${q.id}')">Approve ✓</button>
                <button class="delete-btn" onclick="remove('${q.id}')">Delete ✗</button>
            </div>
        </div>
    `).join('');
}

async function verify(id) {
    const card = document.getElementById(`q-${id}`);
    const updatedData = {
        question: card.querySelector('.edit-q').value,
        explanation: card.querySelector('.edit-exp').value,
        verified: true
    };
    await window.API.updateQuestion(id, updatedData);
    card.remove();
}

async function remove(id) {
    if (confirm("Delete this question?")) {
        await window.API.deleteQuestion(id);
        document.getElementById(`q-${id}`).remove();
    }
}

document.addEventListener('DOMContentLoaded', loadPending);