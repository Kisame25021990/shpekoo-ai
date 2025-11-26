#!/bin/bash

echo "🤖 Installation d'Ollama..."

# Installe Ollama
curl -fsSL https://ollama.com/install.sh | sh

echo ""
echo "✅ Ollama installé !"
echo ""
echo "📥 Téléchargement du modèle llama3.2:3b (2 GB)..."
echo "Cela peut prendre quelques minutes..."

# Télécharge le modèle
ollama pull llama3.2:3b

echo ""
echo "✅ Modèle installé !"
echo ""
echo "🧪 Test du modèle..."

# Test
ollama run llama3.2:3b "Dis bonjour en français" --verbose false

echo ""
echo "✅ Installation terminée !"
echo ""
echo "Pour lancer ton IA :"
echo "  cd learning-ai"
echo "  source venv/bin/activate"
echo "  python app.py"
