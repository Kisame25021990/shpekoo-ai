let currentQuestion = '';

// Tab Management
function showTab(tabName) {
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.menu-btn').forEach(btn => btn.classList.remove('active'));
    
    document.getElementById(`${tabName}-tab`).classList.add('active');
    event.target.classList.add('active');
    
    if (tabName === 'history') loadHistory();
    if (tabName === 'knowledge') loadKnowledge();
}

// Chat Functions
async function askQuestion() {
    const input = document.getElementById('question-input');
    const question = input.value.trim();
    
    if (!question) return;

    addMessage('Toi: ' + question, 'user');
    input.value = '';

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question})
    });

    const result = await response.json();

    if (result.found) {
        let source = '🤖 Modèle IA';
        if (result.source === 'memory') source = '💾 Mémoire';
        if (result.source === 'agent') source = '⚙️ Agent';
        
        const formattedAnswer = formatMarkdown(result.answer);
        addMessageHTML(`IA [${source}]: ${formattedAnswer}`, 'ai');
    } else {
        addMessage('IA: Je ne sais pas encore. Tu veux m\'apprendre ?', 'ai');
        currentQuestion = question;
        showTeachPrompt(question);
    }

    updateStats();
}

function showTeachPrompt(question) {
    const answer = prompt(`Apprends-moi la réponse à: "${question}"`);
    if (answer) {
        teachAI(question, answer);
    }
}

async function teachAI(question, answer) {
    const response = await fetch('/learn', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question, answer})
    });

    const result = await response.json();
    addMessage('IA: ' + result.message + ' ✅', 'ai success');
    updateStats();
}

function addMessage(text, className) {
    const chatBox = document.getElementById('chat-box');
    const msg = document.createElement('div');
    msg.className = 'message ' + className;
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addMessageHTML(html, className) {
    const chatBox = document.getElementById('chat-box');
    const msg = document.createElement('div');
    msg.className = 'message ' + className;
    msg.innerHTML = html;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function formatMarkdown(text) {
    text = text.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
    text = text.replace(/\n/g, '<br>');
    return text;
}

// History Functions
async function loadHistory() {
    const response = await fetch('/history?limit=50');
    const history = await response.json();
    
    const list = document.getElementById('history-list');
    list.innerHTML = '';
    
    if (history.length === 0) {
        list.innerHTML = '<p style="text-align:center; color:#999; padding:50px;">Aucun historique pour le moment</p>';
        return;
    }
    
    history.reverse().forEach(item => {
        const div = document.createElement('div');
        div.className = 'history-item';
        const date = new Date(item.timestamp).toLocaleString('fr-FR');
        div.innerHTML = `
            <strong>Q:</strong> ${item.question}<br>
            <strong>R:</strong> ${formatMarkdown(item.answer)}<br>
            <span class="timestamp">📅 ${date} | Source: ${item.source}</span>
        `;
        list.appendChild(div);
    });
}

async function searchHistory() {
    const query = document.getElementById('history-search').value.trim();
    
    if (!query) {
        loadHistory();
        return;
    }
    
    const response = await fetch('/history/search', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query})
    });
    
    const results = await response.json();
    const list = document.getElementById('history-list');
    list.innerHTML = '';
    
    if (results.length === 0) {
        list.innerHTML = '<p style="text-align:center; color:#999; padding:50px;">Aucun résultat trouvé</p>';
        return;
    }
    
    results.reverse().forEach(item => {
        const div = document.createElement('div');
        div.className = 'history-item';
        const date = new Date(item.timestamp).toLocaleString('fr-FR');
        div.innerHTML = `
            <strong>Q:</strong> ${item.question}<br>
            <strong>R:</strong> ${formatMarkdown(item.answer)}<br>
            <span class="timestamp">📅 ${date}</span>
        `;
        list.appendChild(div);
    });
}

async function clearHistory() {
    if (!confirm('Êtes-vous sûr de vouloir effacer tout l\'historique ?')) return;
    
    await fetch('/history/clear', {method: 'POST'});
    loadHistory();
    addMessage('✅ Historique effacé', 'ai success');
}

// Knowledge Functions
async function loadKnowledge() {
    const response = await fetch('/knowledge');
    const knowledge = await response.json();
    
    const list = document.getElementById('knowledge-list');
    list.innerHTML = '';
    
    if (knowledge.length === 0) {
        list.innerHTML = '<p style="text-align:center; color:#999; padding:50px;">Aucune connaissance pour le moment</p>';
        return;
    }
    
    knowledge.forEach(item => {
        const div = document.createElement('div');
        div.className = 'knowledge-item';
        div.innerHTML = `
            <strong>Q:</strong> ${item.question}<br>
            <strong>R:</strong> ${formatMarkdown(item.answer)}<br>
            <button onclick="forgetKnowledge('${item.question.replace(/'/g, "\\'")}')" class="danger-btn" style="margin-top:10px; padding:8px 15px; font-size:12px;">🗑️ Supprimer</button>
        `;
        list.appendChild(div);
    });
}

async function searchKnowledge() {
    const query = document.getElementById('knowledge-search').value.trim();
    
    if (!query) {
        loadKnowledge();
        return;
    }
    
    const response = await fetch('/search-knowledge', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query})
    });
    
    const results = await response.json();
    const list = document.getElementById('knowledge-list');
    list.innerHTML = '';
    
    if (results.length === 0) {
        list.innerHTML = '<p style="text-align:center; color:#999; padding:50px;">Aucun résultat trouvé</p>';
        return;
    }
    
    results.forEach(item => {
        const div = document.createElement('div');
        div.className = 'knowledge-item';
        div.innerHTML = `
            <strong>Q:</strong> ${item.question}<br>
            <strong>R:</strong> ${formatMarkdown(item.answer)}
        `;
        list.appendChild(div);
    });
}

async function forgetKnowledge(question) {
    if (!confirm('Supprimer cette connaissance ?')) return;
    
    await fetch('/forget', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question})
    });
    
    loadKnowledge();
    updateStats();
}

// Code Execution
async function executeCode() {
    const code = document.getElementById('code-input').value.trim();
    const language = document.getElementById('language-select').value;
    const output = document.getElementById('code-output');
    
    if (!code) {
        output.textContent = '❌ Aucun code à exécuter';
        return;
    }
    
    output.textContent = '⏳ Exécution en cours...';
    
    const response = await fetch('/execute-code', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({code, language})
    });
    
    const result = await response.json();
    
    if (result.success) {
        output.textContent = result.output || result.error || '✅ Code exécuté sans sortie';
    } else {
        output.textContent = '❌ Erreur: ' + result.error;
    }
}

// Document Loading
async function loadFromURL() {
    const input = document.getElementById('url-input');
    const url = input.value.trim();
    
    if (!url) return;

    addMessage('⏳ Chargement en cours...', 'ai');

    const response = await fetch('/load-url', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url})
    });

    const result = await response.json();

    if (result.success) {
        addMessage(`✅ ${result.message}`, 'ai success');
        input.value = '';
    } else {
        addMessage(`❌ Erreur: ${result.error}`, 'ai');
    }

    updateStats();
}

async function loadFromText() {
    const input = document.getElementById('text-input');
    const text = input.value.trim();
    
    if (!text) return;

    addMessage('⏳ Analyse du texte...', 'ai');

    const response = await fetch('/load-text', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
    });

    const result = await response.json();

    if (result.success) {
        addMessage(`✅ ${result.message}`, 'ai success');
        input.value = '';
    } else {
        addMessage(`❌ Erreur: ${result.error}`, 'ai');
    }

    updateStats();
}

async function loadFromFolder() {
    const input = document.getElementById('folder-input');
    const folder_path = input.value.trim();
    
    if (!folder_path) return;

    addMessage('⏳ Chargement du dossier...', 'ai');

    const response = await fetch('/load-folder', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({folder_path})
    });

    const result = await response.json();

    if (result.success) {
        addMessage(`✅ ${result.message}`, 'ai success');
        input.value = '';
    } else {
        addMessage(`❌ Erreur: ${result.error}`, 'ai');
    }

    updateStats();
}

// Stats & Agent
async function updateStats() {
    const response = await fetch('/stats');
    const stats = await response.json();
    document.getElementById('knowledge-count').textContent = stats.total_knowledge;
    
    const statusEl = document.getElementById('ai-status');
    if (stats.ai_model_available) {
        statusEl.innerHTML = '🟢 Modèle IA actif';
        statusEl.style.color = '#28a745';
    } else {
        statusEl.innerHTML = '🔴 Modèle IA non disponible';
        statusEl.style.color = '#dc3545';
    }
    
    const agentBtn = document.getElementById('agent-toggle');
    if (stats.agent_mode) {
        agentBtn.textContent = 'Mode Agent: ON';
        agentBtn.style.background = 'linear-gradient(135deg, #28a745 0%, #20c997 100%)';
    } else {
        agentBtn.textContent = 'Mode Agent: OFF';
        agentBtn.style.background = '#6e7681';
    }
}

async function toggleAgentMode() {
    const response = await fetch('/toggle-agent', {method: 'POST'});
    const result = await response.json();
    
    if (result.agent_mode) {
        addMessage('⚙️ Mode Agent activé - L\'IA peut maintenant exécuter des actions', 'ai success');
    } else {
        addMessage('🚫 Mode Agent désactivé - L\'IA ne fera que répondre', 'ai');
    }
    
    updateStats();
}

// Event Listeners
document.getElementById('question-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') askQuestion();
});

// Initialize
updateStats();
addMessage('👋 Bienvenue sur Shpekoo-AI ! Pose-moi une question.', 'ai');
