import subprocess
import os
import json

class AgentTools:
    def __init__(self, workspace="/home/shpekoo/agent-workspace"):
        self.workspace = workspace
        os.makedirs(workspace, exist_ok=True)
    
    def execute_python(self, code):
        """Exécute du code Python"""
        try:
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=self.workspace
            )
            return {
                'success': True,
                'output': result.stdout,
                'error': result.stderr
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def execute_bash(self, command):
        """Exécute une commande bash"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10,
                cwd=self.workspace
            )
            return {
                'success': True,
                'output': result.stdout,
                'error': result.stderr
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def create_file(self, filename, content):
        """Crée un fichier"""
        try:
            filepath = os.path.join(self.workspace, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return {'success': True, 'path': filepath}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def read_file(self, filename):
        """Lit un fichier"""
        try:
            filepath = os.path.join(self.workspace, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return {'success': True, 'content': content}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def list_files(self):
        """Liste les fichiers du workspace"""
        try:
            files = os.listdir(self.workspace)
            return {'success': True, 'files': files}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def git_init(self):
        """Initialise un repo Git"""
        return self.execute_bash('git init')
    
    def git_add(self, files='.'):
        """Ajoute des fichiers à Git"""
        return self.execute_bash(f'git add {files}')
    
    def git_commit(self, message):
        """Commit les changements"""
        return self.execute_bash(f'git commit -m "{message}"')
    
    def install_package(self, package):
        """Installe un package Python"""
        return self.execute_bash(f'pip install {package}')
