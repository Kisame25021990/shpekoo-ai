import os
import json

class FolderLoader:
    def __init__(self, ai_brain):
        self.ai = ai_brain
        self.supported_extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.java', '.c', '.cpp']
    
    def load_folder(self, folder_path):
        """Charge tous les fichiers d'un dossier"""
        learned_count = 0
        files_processed = []
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()
                
                if ext in self.supported_extensions:
                    try:
                        result = self.load_file(file_path)
                        if result['success']:
                            learned_count += result['learned']
                            files_processed.append(file)
                    except Exception as e:
                        print(f"Erreur avec {file}: {e}")
        
        return {
            'success': True,
            'learned': learned_count,
            'files': len(files_processed),
            'message': f'{learned_count} connaissances apprises depuis {len(files_processed)} fichiers'
        }
    
    def load_file(self, file_path):
        """Charge un fichier spécifique"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_name = os.path.basename(file_path)
            ext = os.path.splitext(file_name)[1]
            
            # Pour les fichiers de code
            if ext in ['.py', '.js', '.java', '.c', '.cpp', '.html', '.css']:
                return self.learn_code_file(file_name, content, ext)
            
            # Pour les fichiers texte
            else:
                return self.learn_text_file(file_name, content)
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def learn_code_file(self, file_name, content, ext):
        """Apprend depuis un fichier de code"""
        language_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.java': 'Java',
            '.c': 'C',
            '.cpp': 'C++',
            '.html': 'HTML',
            '.css': 'CSS'
        }
        
        language = language_map.get(ext, 'Code')
        
        # Stocke le fichier complet
        question = f"Code de {file_name}"
        self.ai.learn(question, f"Fichier {language}: {file_name}\n\n{content}")
        
        # Extrait les fonctions/classes
        learned = 1
        
        if ext == '.py':
            learned += self.extract_python_elements(file_name, content)
        elif ext == '.js':
            learned += self.extract_js_elements(file_name, content)
        
        return {'success': True, 'learned': learned}
    
    def extract_python_elements(self, file_name, content):
        """Extrait les fonctions et classes Python"""
        import re
        learned = 0
        
        # Fonctions
        functions = re.findall(r'def\s+(\w+)\s*\([^)]*\):[^\n]*\n((?:    .*\n)*)', content)
        for func_name, func_body in functions:
            question = f"Fonction Python {func_name} dans {file_name}"
            answer = f"def {func_name}...\n{func_body[:500]}"
            self.ai.learn(question, answer)
            learned += 1
        
        # Classes
        classes = re.findall(r'class\s+(\w+)[^:]*:[^\n]*\n((?:    .*\n)*)', content)
        for class_name, class_body in classes:
            question = f"Classe Python {class_name} dans {file_name}"
            answer = f"class {class_name}...\n{class_body[:500]}"
            self.ai.learn(question, answer)
            learned += 1
        
        return learned
    
    def extract_js_elements(self, file_name, content):
        """Extrait les fonctions JavaScript"""
        import re
        learned = 0
        
        # Fonctions
        functions = re.findall(r'function\s+(\w+)\s*\([^)]*\)\s*{([^}]*)}', content)
        for func_name, func_body in functions:
            question = f"Fonction JavaScript {func_name} dans {file_name}"
            answer = f"function {func_name}...\n{func_body[:500]}"
            self.ai.learn(question, answer)
            learned += 1
        
        return learned
    
    def learn_text_file(self, file_name, content):
        """Apprend depuis un fichier texte"""
        # Découpe en sections
        sections = content.split('\n\n')
        learned = 0
        
        for i, section in enumerate(sections):
            if len(section.strip()) > 50:
                question = f"Section {i+1} de {file_name}"
                self.ai.learn(question, section.strip())
                learned += 1
        
        return {'success': True, 'learned': learned}
