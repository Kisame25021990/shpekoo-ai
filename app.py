from flask import Flask, render_template, request, jsonify
from brain import LearningAI
from document_loader import DocumentLoader
from folder_loader import FolderLoader
from self_learning import SelfLearning

app = Flask(__name__)
ai = LearningAI('memory.json')
loader = DocumentLoader(ai)
folder_loader = FolderLoader(ai)
self_learning = SelfLearning(ai)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    result = ai.ask(question)
    
    # Apprend de l'interaction
    if result.get('success'):
        if result.get('agent_result'):
            # Tâche agent réussie
            self_learning.learn_from_success(
                question,
                result.get('agent_result', {}).get('steps', []),
                result
            )
        elif result.get('error'):
            # Échec
            self_learning.learn_from_failure(question, result.get('error'))
    
    return jsonify(result)

@app.route('/learn', methods=['POST'])
def learn():
    data = request.json
    question = data.get('question', '')
    answer = data.get('answer', '')
    result = ai.learn(question, answer)
    return jsonify(result)

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
    app.run(debug=True, host='0.0.0.0', port=5000)
