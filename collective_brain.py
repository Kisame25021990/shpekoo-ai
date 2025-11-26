"""
Cerveau Collectif
- Chaque IA fonctionne normalement
- Chaque IA partage ses connaissances uniques
- Chaque IA apprend des autres (seulement ce qu'elle ne connaît pas)
- Tout le monde devient plus intelligent ensemble
"""

import json
import os
from datetime import datetime
from brain import LearningAI

class CollectiveBrain:
    def __init__(self, shared_folder="/home/shpekoo/collective-brain"):
        self.shared_folder = shared_folder
        os.makedirs(shared_folder, exist_ok=True)
        self.my_id = os.uname().nodename
        self.my_file = os.path.join(shared_folder, f"{self.my_id}.json")
    
    def share_my_knowledge(self, ai):
        """Partage MES connaissances uniques"""
        my_knowledge = ai.get_all_knowledge()
        
        data = {
            'id': self.my_id,
            'timestamp': datetime.now().isoformat(),
            'knowledge': my_knowledge
        }
        
        with open(self.my_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return len(my_knowledge)
    
    def learn_from_others(self, ai):
        """Apprend des autres (seulement ce que je ne connais pas)"""
        if not os.path.exists(self.shared_folder):
            return 0
        
        files = [f for f in os.listdir(self.shared_folder) if f.endswith('.json')]
        
        total_learned = 0
        contributors = []
        
        for filename in files:
            # Ignore mon propre fichier
            if filename == f"{self.my_id}.json":
                continue
            
            filepath = os.path.join(self.shared_folder, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                contributor_id = data.get('id')
                knowledge_list = data.get('knowledge', [])
                
                learned = 0
                for item in knowledge_list:
                    question = item.get('question')
                    answer = item.get('answer')
                    
                    # Vérifie si je connais déjà
                    result = ai.ask(question)
                    
                    # J'apprends seulement si je ne connais pas ou si ma réponse est courte
                    if not result.get('found') or len(result.get('answer', '')) < 50:
                        ai.learn(question, answer)
                        learned += 1
                
                if learned > 0:
                    total_learned += learned
                    contributors.append(f"{contributor_id} ({learned})")
            
            except Exception as e:
                pass
        
        return total_learned, contributors
    
    def sync(self, ai):
        """Synchronisation complète: partage + apprentissage"""
        print(f"🔄 Synchronisation - {self.my_id}")
        print("=" * 60)
        
        # 1. Partage mes connaissances
        print("\n📤 Partage de mes connaissances...")
        shared = self.share_my_knowledge(ai)
        print(f"   ✅ {shared} connaissances partagées")
        
        # 2. Apprends des autres
        print("\n📥 Apprentissage des autres...")
        learned, contributors = self.learn_from_others(ai)
        
        if learned > 0:
            print(f"   ✅ {learned} nouvelles connaissances apprises")
            for contrib in contributors:
                print(f"      • {contrib}")
        else:
            print(f"   ℹ️  Rien de nouveau à apprendre")
        
        # 3. Stats
        stats = ai.stats()
        print(f"\n📊 Total connaissances: {stats.get('total_knowledge', 0)}")
        print("=" * 60)
        
        return learned
    
    def auto_sync_loop(self, ai, interval=300):
        """Synchronisation automatique continue"""
        import time
        
        print("🔄 SYNCHRONISATION AUTOMATIQUE")
        print(f"   ID: {self.my_id}")
        print(f"   Dossier: {self.shared_folder}")
        print(f"   Intervalle: {interval}s ({interval//60} min)")
        print("   Ctrl+C pour arrêter")
        print("=" * 60)
        
        iteration = 0
        
        try:
            while True:
                iteration += 1
                print(f"\n[Sync #{iteration}] {datetime.now().strftime('%H:%M:%S')}")
                
                # Partage
                shared = self.share_my_knowledge(ai)
                print(f"📤 {shared} connaissances partagées")
                
                # Apprend
                learned, contributors = self.learn_from_others(ai)
                
                if learned > 0:
                    print(f"📥 {learned} nouvelles connaissances apprises")
                    for contrib in contributors:
                        print(f"   • {contrib}")
                else:
                    print(f"📥 Rien de nouveau")
                
                stats = ai.stats()
                print(f"📊 Total: {stats.get('total_knowledge', 0)}")
                
                print(f"⏳ Prochaine sync dans {interval}s...")
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\n🛑 Synchronisation arrêtée")

if __name__ == '__main__':
    print("🧠 CERVEAU COLLECTIF - SHPEKOO AI")
    print("=" * 60)
    
    # Configuration
    folder = input("Dossier partagé (Enter = /home/shpekoo/collective-brain): ").strip()
    if not folder:
        folder = "/home/shpekoo/collective-brain"
    
    brain = CollectiveBrain(folder)
    ai = LearningAI('memory.json')
    
    print(f"\n🆔 Votre ID: {brain.my_id}")
    print(f"📁 Dossier: {folder}")
    
    # Menu
    print("\n" + "=" * 60)
    print("1. Synchroniser maintenant (une fois)")
    print("2. Synchronisation automatique (continue)")
    
    choice = input("\nChoix (1-2): ").strip()
    
    if choice == '1':
        brain.sync(ai)
    
    elif choice == '2':
        interval = input("Intervalle en secondes (300 = 5min): ").strip()
        interval = int(interval) if interval else 300
        
        brain.auto_sync_loop(ai, interval)
    
    print("\n" + "=" * 60)
    print("💡 INSTRUCTIONS:")
    print("   1. Créez un dossier partagé (Google Drive, Dropbox, réseau)")
    print("   2. Tous les collègues configurent le même dossier")
    print("   3. Chacun lance: python collective_brain.py (mode 2)")
    print("   4. Toutes les IA apprennent les unes des autres!")
    print("   5. Chacun garde son IA fonctionnelle + devient plus intelligent!")
    print("\n   ✅ Pas de doublons - Seulement les nouvelles connaissances")
    print("   ✅ Tout le monde profite de tout le monde")
    print("   ✅ Le cerveau collectif grandit en permanence! 🚀")
