# 🤖 Shpekoo-AI

IA complète pour le développement et la cybersécurité avec apprentissage collectif.

## ✨ Fonctionnalités

- 🐍 **Python Expert** - Génération de code, explications
- 🔐 **Cybersécurité** - OWASP, pentesting, 30+ concepts
- 💻 **Multi-langages** - JavaScript, React, Java, C++, etc.
- 🔧 **Pentesting** - Nmap, Hydra, Hashcat, Gobuster, SQLmap
- 🧠 **Auto-apprentissage** - S'entraîne automatiquement
- 🤝 **Cerveau collectif** - Apprend des autres utilisateurs

## 📋 Prérequis

- Linux (Kali, Ubuntu, Debian)
- Python 3.9+
- Git

## 🚀 Installation

```bash
# 1. Cloner le projet
git clone https://github.com/VOTRE_USERNAME/shpekoo-ai.git
cd shpekoo-ai

# 2. Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances
pip install flask requests beautifulsoup4

# 4. Installer Ollama (IA)
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &
ollama pull llama3.2:3b

# 5. Configurer les alias
bash setup_aliases.sh
source ~/.bashrc

# 6. Charger les connaissances
cyber && prog
```

## ⚡ Commandes

| Commande | Description |
|----------|-------------|
| `shpekoo` | Interface web (http://127.0.0.1:5000) |
| `pentest` | Assistant pentesting |
| `bruteforce` | Brute force & crack de hash |
| `train` | Entraînement (100 itérations) |
| `trainforever` | Entraînement infini |
| `collective` | Cerveau collectif |
| `aide` | Voir toutes les commandes |

## 🔧 Outils de pentesting (optionnels)

```bash
sudo apt update
sudo apt install -y nmap hydra hashcat john gobuster nikto sqlmap
```

## 🤝 Cerveau Collectif

Le système de cerveau collectif permet à plusieurs utilisateurs de partager leurs connaissances :

1. Créez un dossier partagé (Google Drive, Dropbox, réseau)
2. Configurez le même chemin pour tous
3. Lancez `collective` (mode 2)
4. Toutes les IA apprennent les unes des autres !

**Avantages** :
- ✅ Pas de doublons
- ✅ Chacun garde son IA fonctionnelle
- ✅ Apprentissage automatique continu
- ✅ Le cerveau collectif grandit en permanence

## 📊 Vérification

```bash
cd ~/shpekoo-ai
source venv/bin/activate
python audit_ia.py
```

## 🎯 Utilisation

### Interface Web
```bash
shpekoo
# Ouvrir http://127.0.0.1:5000
```

### Pentesting
```bash
pentest
# Choisir l'outil (Nmap, Gobuster, etc.)
```

### Brute Force
```bash
bruteforce
# Choisir Hydra, Hashcat, ou John
```

### Entraînement
```bash
trainforever
# L'IA s'entraîne en continu
```

## 📚 Capacités

- **Python** : Variables, listes, fonctions, boucles, etc.
- **Cybersécurité** : OWASP Top 10, SQL injection, XSS, pentesting
- **Programmation** : JavaScript, React, Node.js, Java, C++, PHP, etc.
- **Pentesting** : Nmap, Metasploit, Burp Suite, Hydra, Hashcat
- **Auto-apprentissage** : S'améliore automatiquement

## ⚠️ Avertissement

Utilisez les outils de pentesting UNIQUEMENT sur :
- Vos propres systèmes
- Des environnements de test (HackTheBox, TryHackMe)
- Avec autorisation écrite explicite

Le pentesting sans autorisation est ILLÉGAL.

## 🏗️ Architecture

```
shpekoo-ai/
├── brain.py              # Cerveau de l'IA
├── ai_model.py           # Intégration Ollama
├── app.py                # Interface web
├── agent_tools.py        # Outils agent
├── agent_planner.py      # Planificateur
├── self_learning.py      # Auto-apprentissage
├── collective_brain.py   # Cerveau collectif
├── pentest_assistant.py  # Assistant pentesting
├── brute_force.py        # Brute force
├── cyber_knowledge.py    # Connaissances cyber
├── programming_knowledge.py # Connaissances prog
├── templates/            # Interface web
└── static/               # CSS/JS
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ajouter de nouvelles connaissances
- Améliorer les outils
- Corriger des bugs
- Proposer de nouvelles fonctionnalités

## 📝 Licence

MIT License - Libre d'utilisation pour l'apprentissage et la formation.

## 👤 Auteur

Créé par Shpekoo

## 🌟 Remerciements

- Ollama pour le modèle IA
- La communauté cybersécurité
- Tous les contributeurs

---

⭐ Si ce projet vous aide, n'hésitez pas à mettre une étoile !
