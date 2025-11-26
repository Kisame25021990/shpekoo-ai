"""
Audit complet de l'IA Shpekoo
"""

import os
import json
from brain import LearningAI

def audit_system():
    print("🔍 AUDIT COMPLET DE L'IA SHPEKOO")
    print("=" * 60)
    
    # 1. Vérification des fichiers
    print("\n📁 FICHIERS SYSTÈME")
    print("-" * 60)
    
    files_to_check = {
        'brain.py': 'Cerveau de l\'IA',
        'ai_model.py': 'Intégration Ollama',
        'app.py': 'Interface web',
        'agent_tools.py': 'Outils agent',
        'agent_planner.py': 'Planificateur',
        'self_learning.py': 'Auto-apprentissage',
        'pentest_assistant.py': 'Assistant pentesting',
        'brute_force.py': 'Brute force',
        'cyber_knowledge.py': 'Connaissances cyber',
        'programming_knowledge.py': 'Connaissances prog',
        'memory.json': 'Mémoire',
        'experience.json': 'Expérience',
    }
    
    for file, desc in files_to_check.items():
        path = f"/home/shpekoo/learning-ai/{file}"
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  ✅ {file:30} ({size:>10} bytes) - {desc}")
        else:
            print(f"  ❌ {file:30} MANQUANT - {desc}")
    
    # 2. Vérification de la mémoire
    print("\n🧠 MÉMOIRE")
    print("-" * 60)
    
    try:
        ai = LearningAI('memory.json')
        stats = ai.stats()
        
        print(f"  ✅ Mémoire chargée")
        print(f"  📊 Connaissances totales: {stats.get('total_knowledge', 0)}")
        print(f"  🤖 Ollama actif: {'Oui' if ai.use_ai_model else 'Non'}")
        print(f"  🔧 Mode agent: {'Oui' if ai.agent_mode else 'Non'}")
    except Exception as e:
        print(f"  ❌ Erreur mémoire: {e}")
    
    # 3. Vérification Ollama
    print("\n🤖 OLLAMA")
    print("-" * 60)
    
    from ai_model import AIModel
    model = AIModel()
    
    if model.is_available():
        print(f"  ✅ Ollama actif")
        print(f"  📦 Modèle: {model.model_name}")
        
        # Test rapide
        result = model.generate("Dis juste 'OK'")
        if result['success']:
            print(f"  ✅ Test réussi: {result['answer'][:50]}")
        else:
            print(f"  ⚠️ Test échoué")
    else:
        print(f"  ❌ Ollama non disponible")
        print(f"  💡 Lancez: ollama serve")
    
    # 4. Vérification des outils
    print("\n🔧 OUTILS PENTESTING")
    print("-" * 60)
    
    tools = {
        'nmap': 'Scanner réseau',
        'hydra': 'Brute force',
        'hashcat': 'Crack de hash',
        'john': 'John the Ripper',
        'gobuster': 'Scan web',
        'nikto': 'Scan vulnérabilités',
        'sqlmap': 'SQL injection',
        'metasploit': 'Framework exploitation',
    }
    
    for tool, desc in tools.items():
        result = os.system(f"which {tool} > /dev/null 2>&1")
        if result == 0:
            print(f"  ✅ {tool:15} - {desc}")
        else:
            print(f"  ❌ {tool:15} - {desc} (non installé)")
    
    # 5. Vérification des alias
    print("\n⚡ ALIAS")
    print("-" * 60)
    
    bashrc_path = os.path.expanduser("~/.bashrc")
    if os.path.exists(bashrc_path):
        with open(bashrc_path, 'r') as f:
            content = f.read()
        
        aliases = ['shpekoo', 'pentest', 'bruteforce', 'train', 'learn', 'cyber', 'prog']
        
        for alias in aliases:
            if f"alias {alias}=" in content:
                print(f"  ✅ {alias}")
            else:
                print(f"  ❌ {alias} (manquant)")
    else:
        print(f"  ❌ .bashrc non trouvé")
    
    # 6. Recommandations
    print("\n💡 RECOMMANDATIONS")
    print("=" * 60)
    
    recommendations = []
    
    # Vérifier si connaissances chargées
    if stats.get('total_knowledge', 0) < 100:
        recommendations.append("⚠️ Peu de connaissances - Lancez: cyber && prog")
    
    # Vérifier Ollama
    if not model.is_available():
        recommendations.append("⚠️ Ollama non actif - Lancez: ollama serve")
    
    # Vérifier outils manquants
    missing_tools = []
    for tool in tools.keys():
        if os.system(f"which {tool} > /dev/null 2>&1") != 0:
            missing_tools.append(tool)
    
    if missing_tools:
        recommendations.append(f"⚠️ Outils manquants: {', '.join(missing_tools)}")
    
    if not recommendations:
        print("  ✅ Tout est optimal !")
    else:
        for rec in recommendations:
            print(f"  {rec}")
    
    # 7. Score global
    print("\n🏆 SCORE GLOBAL")
    print("=" * 60)
    
    score = 0
    max_score = 0
    
    # Fichiers (30 points)
    max_score += 30
    files_ok = sum(1 for f in files_to_check.keys() if os.path.exists(f"/home/shpekoo/learning-ai/{f}"))
    score += (files_ok / len(files_to_check)) * 30
    
    # Mémoire (20 points)
    max_score += 20
    if stats.get('total_knowledge', 0) > 0:
        score += 20
    
    # Ollama (20 points)
    max_score += 20
    if model.is_available():
        score += 20
    
    # Outils (20 points)
    max_score += 20
    tools_ok = sum(1 for t in tools.keys() if os.system(f"which {t} > /dev/null 2>&1") == 0)
    score += (tools_ok / len(tools)) * 20
    
    # Alias (10 points)
    max_score += 10
    aliases_ok = sum(1 for a in aliases if f"alias {a}=" in content)
    score += (aliases_ok / len(aliases)) * 10
    
    percentage = (score / max_score) * 100
    
    print(f"  Score: {score:.0f}/{max_score} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print(f"  🏆 EXCELLENT - IA prête pour production")
    elif percentage >= 70:
        print(f"  🥇 TRÈS BIEN - Quelques améliorations possibles")
    elif percentage >= 50:
        print(f"  🥈 BIEN - Plusieurs éléments à améliorer")
    else:
        print(f"  🥉 MOYEN - Configuration incomplète")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    audit_system()
