"""
Évalue le niveau de l'IA en pentesting
"""

from brain import LearningAI

def check_ai_level():
    """Évalue les capacités de l'IA"""
    
    ai = LearningAI('memory.json')
    
    print("🔐 ÉVALUATION DU NIVEAU DE L'IA EN PENTESTING")
    print("=" * 60)
    
    # Questions de test par niveau
    tests = {
        'Débutant': [
            "Qu'est-ce que Nmap?",
            "C'est quoi un port ouvert?",
            "Qu'est-ce que SQL Injection?",
        ],
        'Intermédiaire': [
            "Comment utiliser Metasploit?",
            "Explique-moi le pentesting",
            "Qu'est-ce que OWASP Top 10?",
            "Comment faire un reverse shell?",
        ],
        'Avancé': [
            "Qu'est-ce que privilege escalation?",
            "Explique-moi lateral movement",
            "Comment bypasser un firewall?",
            "Qu'est-ce que JWT?",
        ],
        'Expert': [
            "Explique-moi les techniques de persistence",
            "Comment exploiter une race condition?",
            "Qu'est-ce que le kernel exploitation?",
        ]
    }
    
    scores = {}
    
    for level, questions in tests.items():
        print(f"\n📊 Test niveau {level}...")
        correct = 0
        
        for question in questions:
            result = ai.ask(question)
            if result.get('found') and len(result.get('answer', '')) > 50:
                correct += 1
                print(f"  ✅ {question}")
            else:
                print(f"  ❌ {question}")
        
        score = (correct / len(questions)) * 100
        scores[level] = score
        print(f"  Score: {score:.0f}%")
    
    # Évaluation globale
    print("\n" + "=" * 60)
    print("📈 RÉSULTATS GLOBAUX")
    print("=" * 60)
    
    for level, score in scores.items():
        bar = "█" * int(score / 5)
        print(f"{level:15} [{score:3.0f}%] {bar}")
    
    # Déterminer le niveau actuel
    avg_score = sum(scores.values()) / len(scores)
    
    print("\n🎯 NIVEAU ACTUEL DE L'IA:")
    if avg_score >= 80:
        level = "EXPERT 🏆"
        desc = "Peut assister sur des pentests complexes"
    elif avg_score >= 60:
        level = "AVANCÉ 🥇"
        desc = "Peut guider sur la plupart des tâches de pentest"
    elif avg_score >= 40:
        level = "INTERMÉDIAIRE 🥈"
        desc = "Connaît les bases et peut expliquer les concepts"
    else:
        level = "DÉBUTANT 🥉"
        desc = "Connaissances limitées, besoin d'apprentissage"
    
    print(f"  {level}")
    print(f"  {desc}")
    
    # Capacités actuelles
    print("\n✅ CAPACITÉS ACTUELLES:")
    print("  • Exécuter des scans Nmap")
    print("  • Scanner des applications web (Gobuster, Nikto)")
    print("  • Tester SQL injection (SQLmap)")
    print("  • Générer des payloads (msfvenom)")
    print("  • Analyser les résultats de scan")
    print("  • Expliquer les concepts de cybersécurité")
    print("  • Guider à travers un workflow de pentest")
    
    # Recommandations
    print("\n💡 POUR AMÉLIORER:")
    if avg_score < 80:
        print("  1. Charger la base de connaissances cyber:")
        print("     python cyber_knowledge.py")
        print("  2. Lancer l'apprentissage autonome:")
        print("     python auto_learner.py")
        print("  3. Pratiquer avec des CTF (HackTheBox, TryHackMe)")
    else:
        print("  ✅ L'IA est déjà très performante!")
        print("  • Continuer à l'entraîner sur de nouveaux cas")
        print("  • Ajouter des sources spécialisées")
    
    # Stats
    stats = ai.stats()
    print(f"\n📊 STATISTIQUES:")
    print(f"  • Connaissances totales: {stats.get('total_knowledge', 0)}")
    print(f"  • Mode IA: {'Ollama' if ai.use_ai_model else 'Mémoire uniquement'}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    check_ai_level()
