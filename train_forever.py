import time
import random
from brain import LearningAI
from self_learning import SelfLearning

class InfiniteTraining:
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
    
    def train_forever(self, delay=2):
        """Entraînement infini"""
        print("🤖 ENTRAÎNEMENT INFINI ACTIVÉ")
        print("=" * 60)
        print("⚠️  L'IA va s'entraîner en continu")
        print("   Appuyez sur Ctrl+C pour arrêter\n")
        print("=" * 60)
        
        iteration = 0
        
        try:
            while True:
                iteration += 1
                task = random.choice(self.training_tasks)
                
                print(f"\n[{iteration}] {task}")
                
                self.ai.agent_mode = True
                result = self.ai.ask(task)
                
                if result.get('source') == 'agent' and result.get('found'):
                    self.self_learning.learn_from_success(task, [], result)
                    print("✅")
                else:
                    self.self_learning.learn_from_failure(task, result.get('answer', ''))
                    print("❌")
                
                # Affiche stats tous les 10 itérations
                if iteration % 10 == 0:
                    stats = self.self_learning.get_stats()
                    success_rate = (stats['total_success'] / (stats['total_success'] + stats['total_failures'])) * 100
                    print(f"\n📊 [{iteration} itérations] Succès: {stats['total_success']} | Échecs: {stats['total_failures']} | Taux: {success_rate:.1f}%")
                
                time.sleep(delay)
        
        except KeyboardInterrupt:
            print("\n\n🛑 Entraînement arrêté par l'utilisateur")
            self.show_final_stats(iteration)
    
    def show_final_stats(self, total_iterations):
        """Affiche les statistiques finales"""
        stats = self.self_learning.get_stats()
        
        print("\n" + "=" * 60)
        print("📈 STATISTIQUES FINALES")
        print("=" * 60)
        print(f"  • Itérations totales: {total_iterations}")
        print(f"  • Tâches réussies: {stats['total_success']}")
        print(f"  • Tâches échouées: {stats['total_failures']}")
        print(f"  • Patterns appris: {stats['patterns_learned']}")
        
        total = stats['total_success'] + stats['total_failures']
        if total > 0:
            success_rate = (stats['total_success'] / total) * 100
            print(f"  • Taux de réussite: {success_rate:.1f}%")
        
        print("=" * 60)

if __name__ == '__main__':
    trainer = InfiniteTraining()
    
    print("🔄 MODE D'ENTRAÎNEMENT INFINI")
    print("=" * 60)
    print("L'IA va s'entraîner en continu jusqu'à ce que vous l'arrêtiez.")
    print("\nOptions:")
    print("  • Délai entre tâches: 2 secondes (rapide)")
    print("  • Arrêt: Ctrl+C")
    print("  • Stats: Affichées tous les 10 itérations")
    
    input("\nAppuyez sur Entrée pour démarrer...")
    
    trainer.train_forever(delay=2)
