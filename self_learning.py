import json
from datetime import datetime

class SelfLearning:
    def __init__(self, brain):
        self.brain = brain
        self.experience_file = "experience.json"
        self.load_experience()
    
    def load_experience(self):
        """Charge l'expérience passée"""
        try:
            with open(self.experience_file, 'r', encoding='utf-8') as f:
                self.experience = json.load(f)
        except:
            self.experience = {
                'successful_tasks': [],
                'failed_tasks': [],
                'patterns': {},
                'improvements': []
            }
    
    def save_experience(self):
        """Sauvegarde l'expérience"""
        with open(self.experience_file, 'w', encoding='utf-8') as f:
            json.dump(self.experience, f, indent=2, ensure_ascii=False)
    
    def learn_from_success(self, task, plan, result):
        """Apprend d'une tâche réussie"""
        self.experience['successful_tasks'].append({
            'task': task,
            'plan': plan,
            'timestamp': datetime.now().isoformat(),
            'result': 'success'
        })
        
        # Détecte des patterns
        self._detect_patterns(task, plan)
        
        # Sauvegarde dans la mémoire
        self.brain.learn(
            f"Comment faire: {task}",
            f"Plan réussi: {json.dumps(plan, ensure_ascii=False)}"
        )
        
        self.save_experience()
    
    def learn_from_failure(self, task, error):
        """Apprend d'un échec"""
        self.experience['failed_tasks'].append({
            'task': task,
            'error': error,
            'timestamp': datetime.now().isoformat()
        })
        
        # Analyse l'erreur
        improvement = self._analyze_failure(task, error)
        if improvement:
            self.experience['improvements'].append(improvement)
        
        self.save_experience()
    
    def _detect_patterns(self, task, plan):
        """Détecte des patterns dans les tâches réussies"""
        task_lower = task.lower()
        
        # Mots-clés importants
        keywords = ['script', 'fichier', 'variable', 'liste', 'boucle', 'fonction']
        
        for keyword in keywords:
            if keyword in task_lower:
                if keyword not in self.experience['patterns']:
                    self.experience['patterns'][keyword] = []
                
                self.experience['patterns'][keyword].append({
                    'task': task,
                    'plan': plan
                })
    
    def _analyze_failure(self, task, error):
        """Analyse un échec pour amélioration"""
        return {
            'task': task,
            'error': error,
            'suggestion': 'Améliorer la détection de mots-clés',
            'timestamp': datetime.now().isoformat()
        }
    
    def get_similar_task(self, task):
        """Trouve une tâche similaire réussie"""
        task_lower = task.lower()
        
        for success in self.experience['successful_tasks']:
            if any(word in task_lower for word in success['task'].lower().split()):
                return success
        
        return None
    
    def suggest_improvement(self, task):
        """Suggère une amélioration basée sur l'expérience"""
        similar = self.get_similar_task(task)
        
        if similar:
            return {
                'found': True,
                'suggestion': f"Tâche similaire trouvée: {similar['task']}",
                'plan': similar['plan']
            }
        
        return {'found': False}
    
    def get_stats(self):
        """Statistiques d'apprentissage"""
        return {
            'total_success': len(self.experience['successful_tasks']),
            'total_failures': len(self.experience['failed_tasks']),
            'patterns_learned': len(self.experience['patterns']),
            'improvements': len(self.experience['improvements'])
        }
