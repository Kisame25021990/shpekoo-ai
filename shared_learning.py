"""
Système d'apprentissage collectif
Toutes les IA apprennent des questions/réponses de tous les utilisateurs
"""

import json
import os
from datetime import datetime
from brain import LearningAI

class SharedLearning:
    def __init__(self, shared_folder="/home/shpekoo/shared-ai"):
        self.shared_folder = shared_folder
        os.makedirs(shared_folder, exist_ok=True)
        self.my_id = os.uname().nodename
        self.ai = LearningAI('memory.json')
    
    def log_interaction(self, question, answer):
        """Enregistre une interaction pour partager avec les collègues"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        interaction = {
            'timestamp': timestamp,
            'user': self.my_id,
            'question': question,
            'answer': answer
        }
        
        filename = f"{timestamp}_{self.my_id}.json"
        filepath = os.path.join(self.shared_folder, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(interaction, f, indent=2, ensure_ascii=False)
        
        print(f"📤 Interaction partagée: {filename}")
    
    def sync_from_colleagues(self):
        """Récupère et apprend de toutes les interactions des collègues"""
        if not os.path.exists(self.shared_folder):
            print(f"❌ Dossier partagé non trouvé: {self.shared_folder}")
            return 0
        
        files = [f for f in os.listdir(self.shared_folder) if f.endswith('.json')]
        
        print(f"📚 {len(files)} interactions trouvées dans le dossier partagé")
        
        learned = 0
        skipped = 0
        
        for filename in files:
            filepath = os.path.join(self.shared_folder, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    interaction = json.load(f)
                
                user = interaction.get('user')
                question = interaction.get('question')
                answer = interaction.get('answer')
                
                # Vérifie si déjà connu
                result = self.ai.ask(question)
                
                if not result.get('found') or len(result.get('answer', '')) < 50:
                    self.ai.learn(question, answer)
                    learned += 1
                    print(f"  ✅ Appris de {user}: {question[:60]}...")
                else:
                    skipped += 1
            
            except Exception as e:
                print(f"  ⚠️ Erreur lecture {filename}: {e}")
        
        print(f"\n✅ {learned} nouvelles connaissances apprises")
        print(f"⏭️  {skipped} déjà connues (ignorées)")
        
        return learned
    
    def auto_sync_loop(self, interval=300):
        """Synchronisation automatique toutes les X secondes"""
        import time
        
        print("🔄 SYNCHRONISATION AUTOMATIQUE ACTIVÉE")
        print(f"   Dossier: {self.shared_folder}")
        print(f"   Intervalle: {interval}s ({interval//60} min)")
        print("   Appuyez sur Ctrl+C pour arrêter")
        print("=" * 60)
        
        iteration = 0
        
        try:
            while True:
                iteration += 1
                print(f"\n[Sync #{iteration}] {datetime.now().strftime('%H:%M:%S')}")
                
                learned = self.sync_from_colleagues()
                
                stats = self.ai.stats()
                print(f"📊 Total connaissances: {stats.get('total_knowledge', 0)}")
                
                print(f"\n⏳ Prochaine sync dans {interval}s...")
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\n🛑 Synchronisation arrêtée")

if __name__ == '__main__':
    print("🤝 APPRENTISSAGE COLLECTIF - SHPEKOO AI")
    print("=" * 60)
    
    # Configuration
    print("\n📁 Configuration du dossier partagé:")
    print("   Option 1: Dossier local (test)")
    print("   Option 2: Dossier réseau (production)")
    print("   Option 3: Google Drive / Dropbox")
    
    choice = input("\nChoix (1-3): ").strip()
    
    if choice == '1':
        shared_folder = "/home/shpekoo/shared-ai"
        print(f"✅ Dossier local: {shared_folder}")
    
    elif choice == '2':
        shared_folder = input("Chemin réseau (ex: /mnt/shared/ai): ").strip()
    
    elif choice == '3':
        shared_folder = input("Chemin Drive/Dropbox (ex: ~/Dropbox/shared-ai): ").strip()
        shared_folder = os.path.expanduser(shared_folder)
    
    else:
        shared_folder = "/home/shpekoo/shared-ai"
    
    # Initialisation
    shared = SharedLearning(shared_folder)
    
    print(f"\n🆔 Votre ID: {shared.my_id}")
    print(f"📁 Dossier partagé: {shared_folder}")
    
    # Menu
    print("\n" + "=" * 60)
    print("1. Synchroniser maintenant (une fois)")
    print("2. Synchronisation automatique (continue)")
    print("3. Tester en ajoutant une interaction")
    
    action = input("\nAction (1-3): ").strip()
    
    if action == '1':
        print("\n📥 Synchronisation...")
        learned = shared.sync_from_colleagues()
        
        stats = shared.ai.stats()
        print(f"\n📊 Total connaissances: {stats.get('total_knowledge', 0)}")
    
    elif action == '2':
        interval = input("Intervalle en secondes (300 = 5min): ").strip()
        interval = int(interval) if interval else 300
        
        shared.auto_sync_loop(interval)
    
    elif action == '3':
        question = input("Question test: ")
        answer = input("Réponse test: ")
        
        shared.log_interaction(question, answer)
        print("✅ Interaction enregistrée dans le dossier partagé")
    
    print("\n" + "=" * 60)
    print("💡 INSTRUCTIONS POUR VOS COLLÈGUES:")
    print(f"   1. Installer Shpekoo-AI")
    print(f"   2. Configurer le même dossier: {shared_folder}")
    print(f"   3. Lancer: sync")
    print(f"   4. Toutes les IA apprennent ensemble!")
