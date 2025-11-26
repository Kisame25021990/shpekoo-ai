import os
import time
import random
from brain import LearningAI
from document_loader import DocumentLoader

class AutoLearner:
    def __init__(self):
        self.ai = LearningAI('memory.json')
        self.doc_loader = DocumentLoader(self.ai)
        
        # Sources d'apprentissage optimisées
        self.learning_sources = {
            'urls': [
                # Python
                'https://docs.python.org/fr/3/tutorial/',
                
                # Cybersécurité
                'https://owasp.org/www-project-top-ten/',
                'https://portswigger.net/web-security',
                'https://www.offensive-security.com/metasploit-unleashed/',
            ],
            'files': [
                # Fichiers spécifiques à charger
                '/home/shpekoo/devsecops-scanner/main.py',
                '/home/shpekoo/devsecops-scanner/scanners/secret_scanner.py',
                '/home/shpekoo/devsecops-scanner/scanners/code_scanner.py',
            ]
        }
    
    def explore_and_learn(self, duration_minutes=30):
        """Explore et apprend de nouvelles sources"""
        print(f"🧠 Apprentissage autonome pendant {duration_minutes} minutes")
        print("=" * 60)
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        iteration = 0
        
        while time.time() < end_time:
            iteration += 1
            
            source_type = random.choice(['url', 'file'])
            
            if source_type == 'url' and self.learning_sources['urls']:
                url = random.choice(self.learning_sources['urls'])
                print(f"\n[{iteration}] 📄 {url}")
                
                result = self.doc_loader.load_from_url(url)
                
                if result.get('success'):
                    print(f"    ✅ {result.get('learned', 0)} connaissances")
                else:
                    print(f"    ⚠️ Ignoré")
            
            elif source_type == 'file' and self.learning_sources['files']:
                file_path = random.choice(self.learning_sources['files'])
                
                if os.path.exists(file_path):
                    print(f"\n[{iteration}] 📄 {os.path.basename(file_path)}")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        result = self.doc_loader.load_from_text(content)
                        
                        if result.get('success'):
                            print(f"    ✅ {result.get('learned', 0)} connaissances")
                    except:
                        print(f"    ⚠️ Erreur lecture")
            
            stats = self.ai.stats()
            print(f"    📊 Total: {stats.get('total_knowledge', 0)}")
            
            time.sleep(3)
        
        print("\n" + "=" * 60)
        print("🎓 Terminé !")
        self.show_stats()
    
    def quick_learning(self):
        """Apprentissage rapide - charge l'essentiel"""
        print("🧠 APPRENTISSAGE RAPIDE")
        print("=" * 60)
        
        # Charge fichiers importants
        print("\n📄 Chargement des fichiers clés...")
        for file_path in self.learning_sources['files']:
            if os.path.exists(file_path):
                print(f"  {os.path.basename(file_path)}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    self.doc_loader.load_from_text(content)
                    print(f"  ✅")
                except:
                    print(f"  ⚠️")
                time.sleep(1)
        
        # Génère connaissances
        print("\n🤖 Génération de connaissances...")
        self.generate_knowledge()
        
        print("\n" + "=" * 60)
        print("🎓 Terminé !")
        self.show_stats()
    
    def deep_learning_session(self):
        """Session approfondie - charge URLs + génère connaissances"""
        print("🧠 SESSION APPROFONDIE")
        print("=" * 60)
        
        # Charge URLs
        print("\n🌐 Chargement des URLs...")
        for i, url in enumerate(self.learning_sources['urls'], 1):
            print(f"  [{i}/{len(self.learning_sources['urls'])}] {url}")
            result = self.doc_loader.load_from_url(url)
            if result.get('success'):
                print(f"  ✅ {result.get('learned', 0)} connaissances")
            else:
                print(f"  ⚠️ Ignoré")
            time.sleep(5)
        
        # Charge fichiers
        print("\n📄 Chargement des fichiers...")
        for file_path in self.learning_sources['files']:
            if os.path.exists(file_path):
                print(f"  {os.path.basename(file_path)}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    self.doc_loader.load_from_text(content)
                    print(f"  ✅")
                except:
                    print(f"  ⚠️")
                time.sleep(1)
        
        # Génère connaissances
        print("\n🤖 Génération de connaissances...")
        self.generate_knowledge()
        
        print("\n" + "=" * 60)
        print("🎓 Terminé !")
        self.show_stats()
    
    def generate_knowledge(self):
        """Génère des connaissances"""
        topics = [
            "variables Python",
            "listes Python",
            "dictionnaires Python",
            "fonctions Python",
            "OWASP Top 10",
            "injection SQL",
            "XSS",
            "pentesting",
            "Metasploit",
            "sécurité réseau",
        ]
        
        for topic in topics:
            question = f"Qu'est-ce que {topic}?"
            result = self.ai.ask(question)
            
            if result.get('found'):
                self.ai.learn(f"Explication: {topic}", result.get('answer', ''))
                print(f"  ✅ {topic}")
            
            time.sleep(1)
    
    def show_stats(self):
        """Affiche les statistiques"""
        stats = self.ai.stats()
        
        print("\n📈 STATISTIQUES:")
        print(f"  • Connaissances: {stats.get('total_knowledge', 0)}")
        print(f"  • Sources URL: {len(self.learning_sources['urls'])}")
        print(f"  • Fichiers: {len(self.learning_sources['files'])}")

if __name__ == '__main__':
    learner = AutoLearner()
    
    print("🔐 APPRENTISSAGE AUTONOME")
    print("=" * 60)
    print("1. Apprentissage rapide (2 min)")
    print("2. Exploration continue (30 min)")
    print("3. Session approfondie (10 min)")
    
    choice = input("\nChoix (1-3): ").strip()
    
    if choice == '1':
        learner.quick_learning()
    elif choice == '2':
        learner.explore_and_learn(duration_minutes=30)
    elif choice == '3':
        learner.deep_learning_session()
    else:
        print("Choix invalide")
