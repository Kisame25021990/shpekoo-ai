# 🤖 Installation d'Ollama

## 1. Installer Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Télécharger un modèle

### Option A : Modèle léger (recommandé pour débuter)
```bash
ollama pull llama3.2:3b
```
**Taille :** ~2 GB | **RAM :** 4 GB minimum

### Option B : Modèle puissant
```bash
ollama pull llama3.2:8b
```
**Taille :** ~4.7 GB | **RAM :** 8 GB minimum

### Option C : Modèle spécialisé code
```bash
ollama pull codellama:7b
```
**Taille :** ~3.8 GB | **RAM :** 8 GB minimum

## 3. Vérifier l'installation

```bash
ollama list
```

## 4. Tester

```bash
ollama run llama3.2:3b "Bonjour, qui es-tu ?"
```

## 5. Lancer le serveur (automatique)

Ollama démarre automatiquement sur `http://localhost:11434`

---

## ⚡ Commandes Utiles

```bash
# Lister les modèles installés
ollama list

# Supprimer un modèle
ollama rm llama3.2:3b

# Voir les modèles disponibles
ollama search
```
