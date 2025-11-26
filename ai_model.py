import requests
import json

class AIModel:
    def __init__(self, model_name="llama3.2:3b", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
    
    def is_available(self):
        """Vérifie si Ollama est disponible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def generate(self, prompt, context=""):
        """Génère une réponse avec le modèle"""
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": full_prompt,
                    "stream": False
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'answer': result.get('response', '').strip()
                }
            else:
                return {'success': False, 'error': 'Erreur du modèle'}
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def chat(self, question, memory_context=""):
        """Mode chat avec contexte de mémoire"""
        system_prompt = """Tu es un assistant IA intelligent et utile. 
Tu réponds en français de manière claire et concise.
Si on te demande du code, tu fournis des exemples fonctionnels."""
        
        if memory_context:
            system_prompt += f"\n\nContexte de ta mémoire:\n{memory_context}"
        
        full_prompt = f"{system_prompt}\n\nQuestion: {question}\n\nRéponse:"
        
        return self.generate(full_prompt)
