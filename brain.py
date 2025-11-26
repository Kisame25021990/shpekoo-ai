import json
import os
from difflib import SequenceMatcher
from ai_model import AIModel
from agent_tools import AgentTools
from agent_planner import AgentPlanner

class LearningAI:
    def __init__(self, memory_file='memory.json'):
        self.memory_file = memory_file
        self.memory = self.load_memory()
        self.ai_model = AIModel()
        self.use_ai_model = self.ai_model.is_available()
        
        # Mode agent
        self.agent_tools = AgentTools()
        self.agent_planner = AgentPlanner(self.ai_model, self.agent_tools)
        self.agent_mode = False
    
    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"knowledge": []}
    
    def save_memory(self):
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, indent=2, ensure_ascii=False)
    
    def similarity(self, a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()
    
    def ask(self, question):
        # Détecte si c'est une demande d'action
        action_keywords = ['crée', 'créer', 'fais', 'faire', 'exécute', 'lance', 'installe', 'génère']
        is_action = any(keyword in question.lower() for keyword in action_keywords)
        
        # Mode agent pour les actions
        if is_action and self.use_ai_model and self.agent_mode:
            result = self.agent_planner.execute_task(question)
            
            if result['success']:
                summary = f"Tâche exécutée avec succès !\n\n"
                for r in result['results']:
                    summary += f"✅ Étape {r['step']}: {r['action']}\n"
                
                return {
                    'found': True,
                    'answer': summary,
                    'confidence': 100,
                    'source': 'agent'
                }
            else:
                return {
                    'found': True,
                    'answer': f"❌ Erreur: {result.get('error', 'Inconnu')}",
                    'confidence': 100,
                    'source': 'agent'
                }
        
        # Si le modèle IA est disponible, l'utiliser en priorité
        if self.use_ai_model:
            # Prépare le contexte depuis la mémoire
            context = self.get_relevant_context(question)
            result = self.ai_model.chat(question, context)
            
            if result['success']:
                return {
                    'found': True,
                    'answer': result['answer'],
                    'confidence': 100,
                    'source': 'ai_model'
                }
        
        # Sinon, cherche dans la mémoire (fallback)
        best_match = None
        best_score = 0
        question_lower = question.lower()
        
        ignore_words = {'c\'est', 'quoi', 'le', 'la', 'les', 'un', 'une', 'des', 'est', 'sont', 'comment', 'pourquoi', 'que', 'qui', 'ou', 'à', 'de', 'du', 'en', 'pour', 'avec', 'dans', 'sur', 'par', 'tu', 'me', 'moi', 'toi'}
        question_keywords = set(question_lower.split()) - ignore_words
        
        for item in self.memory['knowledge']:
            score = self.similarity(question, item['question'])
            
            item_keywords = set(item['question'].lower().split()) - ignore_words
            common_keywords = question_keywords & item_keywords
            
            answer_keywords = set(item['answer'].lower().split()) - ignore_words
            keywords_in_answer = question_keywords & answer_keywords
            
            if common_keywords:
                score += len(common_keywords) * 0.15
            if keywords_in_answer:
                score += len(keywords_in_answer) * 0.1
                
            if score > best_score:
                best_score = score
                best_match = item
        
        if best_match and best_score > 0.85:
            return {
                'found': True,
                'answer': best_match['answer'],
                'confidence': round(min(best_score * 100, 100), 1),
                'source': 'memory'
            }
        
        return {'found': False, 'answer': None}
    
    def get_relevant_context(self, question, max_items=3):
        """Récupère le contexte pertinent de la mémoire"""
        relevant = []
        
        for item in self.memory['knowledge']:
            score = self.similarity(question, item['question'])
            if score > 0.3:
                relevant.append((score, item))
        
        relevant.sort(reverse=True, key=lambda x: x[0])
        
        context_parts = []
        for score, item in relevant[:max_items]:
            context_parts.append(f"Q: {item['question']}\nR: {item['answer']}")
        
        return "\n\n".join(context_parts) if context_parts else ""
    
    def learn(self, question, answer):
        for item in self.memory['knowledge']:
            if self.similarity(question, item['question']) > 0.9:
                item['answer'] = answer
                self.save_memory()
                return {'status': 'updated', 'message': 'Connaissance mise à jour !'}
        
        self.memory['knowledge'].append({
            'question': question,
            'answer': answer
        })
        self.save_memory()
        return {'status': 'learned', 'message': 'Nouvelle connaissance acquise !'}
    
    def forget(self, question):
        initial_count = len(self.memory['knowledge'])
        self.memory['knowledge'] = [
            item for item in self.memory['knowledge']
            if self.similarity(question, item['question']) < 0.9
        ]
        
        if len(self.memory['knowledge']) < initial_count:
            self.save_memory()
            return {'status': 'forgotten', 'message': 'Connaissance supprimée'}
        
        return {'status': 'not_found', 'message': 'Connaissance introuvable'}
    
    def get_all_knowledge(self):
        return self.memory['knowledge']
    
    def stats(self):
        return {
            'total_knowledge': len(self.memory['knowledge']),
            'memory_size': os.path.getsize(self.memory_file) if os.path.exists(self.memory_file) else 0,
            'ai_model_available': self.use_ai_model,
            'model_name': self.ai_model.model_name if self.use_ai_model else None
        }
