# 🚀 Upgrade : IA avec Modèle de Langage

## 🎯 Nouvelles Capacités

Ton IA peut maintenant :
- ✅ **Comprendre** vraiment les questions
- ✅ **Raisonner** et analyser
- ✅ **Coder** en Python, JavaScript, etc.
- ✅ **Calculer** et résoudre des problèmes
- ✅ **Expliquer** des concepts complexes
- ✅ **Utiliser sa mémoire** comme contexte

## 📦 Installation

### Méthode 1 : Script automatique (recommandé)

```bash
cd /home/shpekoo/learning-ai
./setup_ollama.sh
```

### Méthode 2 : Manuel

```bash
# 1. Installer Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Télécharger le modèle (2 GB)
ollama pull llama3.2:3b

# 3. Vérifier
ollama list
```

## 🔧 Configuration

Le modèle se lance automatiquement. Si besoin :

```bash
# Démarrer Ollama
ollama serve

# Dans un autre terminal
cd learning-ai
source venv/bin/activate
python app.py
```

## 💡 Utilisation

### Mode Hybride Intelligent

L'IA utilise **2 sources** :

1. **📝 Mémoire** (rapide, exact)
   - Si la réponse est dans sa mémoire → Réponse instantanée
   
2. **🤖 Modèle IA** (intelligent, créatif)
   - Si pas dans la mémoire → Utilise le modèle pour comprendre et répondre

### Exemples

```
Toi: "C'est quoi Python ?"
IA [💾 Mémoire]: "Python est un langage de programmation"
→ Réponse depuis la mémoire

Toi: "Écris une fonction pour calculer la factorielle"
IA [🤖 Modèle IA]: "Voici une fonction Python:
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n-1)"
→ Génération par le modèle

Toi: "Explique-moi la différence entre Python et JavaScript"
IA [🤖 Modèle IA]: "Python est un langage interprété..."
→ Raisonnement du modèle
```

## 📊 Statut

L'interface affiche :
- ✅ **Modèle IA actif** → Ollama fonctionne
- ⚠️ **Modèle IA non disponible** → Utilise uniquement la mémoire

## ⚙️ Modèles Disponibles

### Léger (recommandé)
```bash
ollama pull llama3.2:3b  # 2 GB, 4 GB RAM
```

### Puissant
```bash
ollama pull llama3.2:8b  # 4.7 GB, 8 GB RAM
```

### Spécialisé Code
```bash
ollama pull codellama:7b  # 3.8 GB, 8 GB RAM
```

### Changer de modèle

Édite `ai_model.py` ligne 4 :
```python
def __init__(self, model_name="llama3.2:3b", ...):
```

## 🔥 Avantages

| Avant | Après |
|-------|-------|
| 📝 Stocke du texte | 🧠 Comprend et raisonne |
| 🔍 Cherche des mots-clés | 💡 Analyse le sens |
| ❌ Ne peut pas coder | ✅ Génère du code |
| ❌ Pas de calcul | ✅ Résout des problèmes |
| ⚡ Ultra rapide | ⚡ Rapide (2-5 sec) |
| 💾 0 MB RAM | 💾 4 GB RAM |

## 🎓 Cas d'Usage

### 1. Assistant de Code
```
"Écris une API REST en Flask"
"Comment optimiser cette fonction ?"
"Explique ce code"
```

### 2. Tuteur Personnel
```
"Explique-moi les pointeurs en C"
"Quelle est la différence entre let et const ?"
```

### 3. Résolution de Problèmes
```
"Comment trier un tableau en O(n log n) ?"
"Calcule la complexité de cet algorithme"
```

### 4. Avec Mémoire
```
Tu charges un cours de médecine
→ L'IA utilise ce contexte pour répondre précisément
```

## 🐛 Dépannage

### Ollama ne démarre pas
```bash
sudo systemctl start ollama
```

### Modèle trop lent
```bash
# Utilise un modèle plus petit
ollama pull llama3.2:1b
```

### Erreur de mémoire
- Ferme d'autres applications
- Utilise un modèle plus petit

## 📈 Performance

- **Mémoire** : < 0.1 sec
- **Modèle IA** : 2-5 sec (selon la question)
- **Hybride** : Meilleur des deux mondes

Profite de ton IA surpuissante ! 🚀
