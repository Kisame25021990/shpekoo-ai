import requests
from bs4 import BeautifulSoup
import re

class DocumentLoader:
    def __init__(self, ai_brain):
        self.ai = ai_brain
    
    def load_from_url(self, url):
        """Charge et apprend depuis une URL"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Supprime scripts et styles
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Extrait le texte
            text = soup.get_text()
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            text = '\n'.join(lines)
            
            # Découpe en sections
            sections = self.chunk_text(text)
            
            # Apprend chaque section
            learned_count = 0
            for section in sections:
                if len(section) > 50:  # Ignore les sections trop courtes
                    question = self.generate_question(section)
                    if question:
                        self.ai.learn(question, section)
                        learned_count += 1
            
            return {
                'success': True,
                'learned': learned_count,
                'message': f'{learned_count} connaissances apprises depuis {url}'
            }
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def load_from_text(self, text):
        """Charge depuis du texte brut"""
        sections = self.chunk_text(text)
        learned_count = 0
        
        for section in sections:
            if len(section) > 50:
                question = self.generate_question(section)
                if question:
                    self.ai.learn(question, section)
                    learned_count += 1
        
        return {
            'success': True,
            'learned': learned_count,
            'message': f'{learned_count} connaissances apprises'
        }
    
    def chunk_text(self, text, max_length=500):
        """Découpe le texte en morceaux"""
        # Découpe par paragraphes
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            if len(current_chunk) + len(para) < max_length:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def generate_question(self, text):
        """Génère une question depuis le texte"""
        # Cherche les titres ou premières phrases
        lines = text.split('\n')
        first_line = lines[0] if lines else ""
        
        # Si c'est un titre court
        if len(first_line) < 100 and first_line:
            # Détecte les patterns de définition
            if any(word in first_line.lower() for word in ['définition', 'qu\'est-ce', 'c\'est quoi']):
                return first_line
            
            # Génère une question
            keywords = self.extract_keywords(first_line)
            if keywords:
                return f"C'est quoi {keywords[0]} ?"
        
        # Extrait le sujet principal
        keywords = self.extract_keywords(text[:200])
        if keywords:
            return f"Parle-moi de {keywords[0]}"
        
        return None
    
    def extract_keywords(self, text):
        """Extrait les mots-clés importants"""
        # Mots à ignorer
        stop_words = {
            'le', 'la', 'les', 'un', 'une', 'des', 'de', 'du', 'et', 'ou', 'mais',
            'est', 'sont', 'a', 'ont', 'pour', 'dans', 'sur', 'avec', 'par',
            'ce', 'cette', 'ces', 'qui', 'que', 'quoi', 'dont', 'où'
        }
        
        # Nettoie et découpe
        words = re.findall(r'\b[a-zàâäéèêëïîôùûüÿæœç]{3,}\b', text.lower())
        
        # Filtre et compte
        keywords = [w for w in words if w not in stop_words]
        
        # Retourne les plus fréquents
        from collections import Counter
        common = Counter(keywords).most_common(3)
        return [word for word, count in common]
