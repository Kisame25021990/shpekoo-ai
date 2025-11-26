import time
import random
from brain import LearningAI
from self_learning import SelfLearning

class AutonomousTraining:
    def __init__(self):
        self.ai = LearningAI('memory.json')
        self.self_learning = SelfLearning(self.ai)
        
        self.training_tasks = [
            "Crée un script sur les variables Python",
            "Génère un exemple de liste",
            "Fais un fichier avec des boucles for",
            "Crée un script avec des fonctions",
            "Génère un exemple de conditions if/else",
            "Crée un script pour manipuler des strings",
            "Fais un exemple de dictionnaire",
            "Génère un script avec des opérateurs",
            "Crée un fichier pour les tuples",
            "Fais un exemple de boucle while"
        ]
    
    def train(self, iterations=10, delay=2):
        """Entraînement autonome"""
        print(f"🤖 Démarrage de l'entraînement autonome ({iterations} itérations)")
        print("=" * 60)
        
        for i in range(iterations):
            task = random.choice(self.training_tasks)
            
            print(f"\n[{i+1}/{iterations}] Tâche: {task}")
            
            self.ai.agent_mode = True
            result = self.ai.ask(task)
            
            # Vérifie le succès basé sur la source agent
            if result.get('source') == 'agent' and result.get('found'):
                print("✅ Succès !")
                self.self_learning.learn_from_success(task, [], result)
            else:
                print(f"❌ Échec: {result.get('answer', 'Erreur')}")
                self.self_learning.learn_from_failure(task, result.get('answer', ''))
            
            stats = self.self_learning.get_stats()
            print(f"📊 Stats: {stats['total_success']} succès, {stats['total_failures']} échecs")
            
            time.sleep(delay)
        
        print("\n" + "=" * 60)
        print("🎓 Entraînement terminé !")
        self.show_final_stats()
    
    def show_final_stats(self):
        """Affiche les statistiques finales"""
        stats = self.self_learning.get_stats()
        
        print("\n📈 STATISTIQUES FINALES:")
        print(f"  • Tâches réussies: {stats['total_success']}")
        print(f"  • Tâches échouées: {stats['total_failures']}")
        print(f"  • Patterns appris: {stats['patterns_learned']}")
        
        total = stats['total_success'] + stats['total_failures']
        if total > 0:
            success_rate = (stats['total_success'] / total) * 100
            print(f"  • Taux de réussite: {success_rate:.1f}%")
    
    def continuous_training(self, duration_minutes=60):
        """Entraînement continu pendant X minutes"""
        print(f"🤖 Entraînement continu pendant {duration_minutes} minutes")
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        iteration = 0
        
        while time.time() < end_time:
            iteration += 1
            task = random.choice(self.training_tasks)
            
            print(f"\n[Itération {iteration}] {task}")
            
            self.ai.agent_mode = True
            result = self.ai.ask(task)
            
            if result.get('source') == 'agent' and result.get('found'):
                self.self_learning.learn_from_success(task, [], result)
                print("✅")
            else:
                self.self_learning.learn_from_failure(task, result.get('answer', ''))
                print("❌")
            
            time.sleep(3)
        
        print("\n🎓 Entraînement continu terminé !")
        self.show_final_stats()

if __name__ == '__main__':
    trainer = AutonomousTraining()
    
    print("Mode d'entraînement:")
    print("1. Entraînement rapide (10 itérations)")
    print("2. Entraînement moyen (50 itérations)")
    print("3. Entraînement intensif (100 itérations)")
    print("4. Entraînement continu (1 heure)")
    
    choice = input("\nChoix (1-4): ").strip()
    
    if choice == '1':
        trainer.train(iterations=10, delay=2)
    elif choice == '2':
        trainer.train(iterations=50, delay=1)
    elif choice == '3':
        trainer.train(iterations=100, delay=1)
    elif choice == '4':
        trainer.continuous_training(duration_minutes=60)
    else:
        print("Choix invalide")
