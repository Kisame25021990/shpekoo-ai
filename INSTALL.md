# 🤖 Shpekoo-AI - Installation

IA complète pour le développement et la cybersécurité

## 📋 Prérequis

- Linux (Kali, Ubuntu, Debian)
- Python 3.9+
- Git

## 🚀 Installation rapide

```bash
# 1. Cloner le projet
cd ~
git clone [URL_DU_REPO] learning-ai
cd learning-ai

# 2. Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances
pip install flask requests beautifulsoup4 ollama

# 4. Installer Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b

# 5. Configurer les alias
bash setup_aliases.sh
source ~/.bashrc

# 6. Charger les connaissances
cyber && prog
```

## ⚡ Commandes

- `shpekoo` - Interface web (http://127.0.0.1:5000)
- `pentest` - Assistant pentesting
- `bruteforce` - Brute force & crack
- `train` - Entraînement (100 itérations)
- `trainforever` - Entraînement infini
- `aide` - Voir toutes les commandes

## 🔧 Outils requis (optionnels)

```bash
sudo apt update
sudo apt install -y nmap hydra hashcat john gobuster nikto sqlmap
```

## 📊 Vérification

```bash
cd ~/learning-ai
source venv/bin/activate
python audit_ia.py
```

## 🎯 Utilisation

1. Lancer l'IA : `shpekoo`
2. Ouvrir : http://127.0.0.1:5000
3. Poser des questions ou charger des sources

## 🔐 Capacités

- Python expert (génération de code)
- Cybersécurité (OWASP, pentesting)
- Programmation (25+ langages)
- Pentesting (Nmap, Hydra, Hashcat, etc.)
- Auto-apprentissage

## ⚠️ Important

Utilisez les outils de pentesting UNIQUEMENT sur vos propres systèmes ou avec autorisation explicite.

## 📝 Licence

Libre d'utilisation pour l'apprentissage et la formation.

---
Créé par Shpekoo - Version 1.0
