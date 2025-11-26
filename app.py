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
    stats_data['history_stats'] = ai.history.stats()
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

@app.route('/history', methods=['GET'])
def get_history():
    limit = request.args.get('limit', 50, type=int)
    return jsonify(ai.history.get_recent(limit))

@app.route('/history/search', methods=['POST'])
def search_history():
    data = request.json
    query = data.get('query', '')
    results = ai.history.search(query)
    return jsonify(results)

@app.route('/history/clear', methods=['POST'])
def clear_history():
    ai.history.clear()
    return jsonify({'status': 'success', 'message': 'Historique effacé'})

@app.route('/search-knowledge', methods=['POST'])
def search_knowledge():
    data = request.json
    query = data.get('query', '').lower()
    results = [k for k in ai.get_all_knowledge() if query in k['question'].lower() or query in k['answer'].lower()]
    return jsonify(results)

@app.route('/execute-code', methods=['POST'])
def execute_code():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    
    try:
        import subprocess
        import tempfile
        import os
        
        configs = {
            'python': {'ext': '.py', 'cmd': ['python3']},
            'javascript': {'ext': '.js', 'cmd': ['node']},
            'bash': {'ext': '.sh', 'cmd': ['bash']},
            'c': {'ext': '.c', 'cmd': ['gcc', '-o', '/tmp/prog'], 'run': ['/tmp/prog']},
            'cpp': {'ext': '.cpp', 'cmd': ['g++', '-o', '/tmp/prog'], 'run': ['/tmp/prog']},
            'java': {'ext': '.java', 'cmd': ['javac'], 'run': ['java']},
            'ruby': {'ext': '.rb', 'cmd': ['ruby']},
            'php': {'ext': '.php', 'cmd': ['php']},
            'go': {'ext': '.go', 'cmd': ['go', 'run']},
        }
        
        if language not in configs:
            return jsonify({'success': False, 'error': f'Langage non supporté'})
        
        config = configs[language]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix=config['ext'], delete=False, dir='/tmp') as f:
            f.write(code)
            temp_file = f.name
        
        if 'run' in config:
            compile_cmd = config['cmd'] + [temp_file]
            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
            if compile_result.returncode != 0:
                os.unlink(temp_file)
                return jsonify({'success': False, 'error': compile_result.stderr})
            
            if language == 'java':
                class_name = 'Main'
                run_cmd = config['run'] + ['-cp', '/tmp', class_name]
            else:
                run_cmd = config['run']
        else:
            run_cmd = config['cmd'] + [temp_file]
        
        result = subprocess.run(run_cmd, capture_output=True, text=True, timeout=5)
        
        os.unlink(temp_file)
        if 'run' in config and os.path.exists('/tmp/prog'):
            os.unlink('/tmp/prog')
        
        return jsonify({
            'success': True,
            'output': result.stdout,
            'error': result.stderr,
            'returncode': result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({'success': False, 'error': 'Timeout (5s)'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
