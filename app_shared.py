"""
Version de app.py avec apprentissage collectif intégré
"""

from flask import Flask, render_template, request, jsonify
from brain import LearningAI
from document_loader import DocumentLoader
from folder_loader import FolderLoader
from self_learning import SelfLearning
from shared_learning import SharedLearning
import os

app = Flask(__name__)
ai = LearningAI('memory.json')
loader = DocumentLoader(ai)
folder_loader = FolderLoader(ai)
self_learning = SelfLearning(ai)

# APPRENTISSAGE COLLECTIF
shared_folder = os.getenv('SHARED_AI_FOLDER', '/home/shpekoo/shared-ai')
shared = SharedLearning(shared_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    result = ai.ask(question)
    
    # PARTAGE AUTOMATIQUE avec les collègues
    if result.get('found') and len(result.get('answer', '')) > 50:
        try:
            shared.log_interaction(question, result.get('answer'))
        except:
            pass  # Ignore si dossier partagé non accessible
    
    # Apprentissage de l'interaction
    if result.get('success'):
        if result.get('agent_result'):
            self_learning.learn_from_success(
                question,
                result.get('agent_result', {}).get('steps', []),
                result
            )
        elif result.get('error'):
            self_learning.learn_from_failure(question, result.get('error'))
    
    return jsonify(result)

@app.route('/learn', methods=['POST'])
def learn():
    data = request.json
    question = data.get('question', '')
    answer = data.get('answer', '')
    result = ai.learn(question, answer)
    
    # Partage avec les collègues
    if result.get('success'):
        try:
            shared.log_interaction(question, answer)
        except:
            pass
    
    return jsonify(result)

@app.route('/sync-colleagues', methods=['POST'])
def sync_colleagues():
    """Synchronise avec les connaissances des collègues"""
    try:
        learned = shared.sync_from_colleagues()
        return jsonify({'success': True, 'learned': learned})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/forget', methods=['POST'])
def forget():
    data = request.json
    question = data.get('question', '')
    result = ai.forget(question)
    return jsonify(result)

@app.route('/knowledge', methods=['GET'])
def knowledge():
    return jsonify(ai.get_all_knowledge())

@app.route('/stats', methods=['GET'])
def stats():
    stats_data = ai.stats()
    stats_data['agent_mode'] = ai.agent_mode
    stats_data['learning_stats'] = self_learning.get_stats()
    stats_data['shared_folder'] = shared_folder
    return jsonify(stats_data)

@app.route('/toggle-agent', methods=['POST'])
def toggle_agent():
    ai.agent_mode = not ai.agent_mode
    return jsonify({'agent_mode': ai.agent_mode})

@app.route('/load-url', methods=['POST'])
def load_url():
    data = request.json
    url = data.get('url', '')
    result = loader.load_from_url(url)
    return jsonify(result)

@app.route('/load-text', methods=['POST'])
def load_text():
    data = request.json
    text = data.get('text', '')
    result = loader.load_from_text(text)
    return jsonify(result)

@app.route('/load-folder', methods=['POST'])
def load_folder():
    data = request.json
    folder_path = data.get('folder_path', '')
    result = folder_loader.load_folder(folder_path)
    return jsonify(result)

@app.route('/learning-stats', methods=['GET'])
def learning_stats():
    return jsonify(self_learning.get_stats())

if __name__ == '__main__':
    print("🤝 SHPEKOO-AI avec APPRENTISSAGE COLLECTIF")
    print(f"📁 Dossier partagé: {shared_folder}")
    print(f"🌐 Interface: http://127.0.0.1:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
