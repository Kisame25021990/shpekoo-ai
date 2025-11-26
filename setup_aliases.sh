#!/bin/bash

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🔧 Configuration des alias Shpekoo-AI...${NC}"

# Chemin du projet
PROJECT_PATH="$HOME/learning-ai"

# Ajouter les alias au .bashrc
cat >> ~/.bashrc << 'EOF'

# ========== Shpekoo-AI Aliases ==========
alias shpekoo='cd ~/learning-ai && source venv/bin/activate && python app.py'
alias pentest='cd ~/learning-ai && source venv/bin/activate && python pentest_assistant.py'
alias bruteforce='cd ~/learning-ai && source venv/bin/activate && python brute_force.py'
alias train='cd ~/learning-ai && source venv/bin/activate && python autonomous_training.py'
alias trainforever='cd ~/learning-ai && source venv/bin/activate && python train_forever.py'
alias collective='cd ~/learning-ai && source venv/bin/activate && python collective_brain.py'
alias cyber='cd ~/learning-ai && source venv/bin/activate && python cyber_knowledge.py'
alias prog='cd ~/learning-ai && source venv/bin/activate && python programming_knowledge.py'
alias base='cd ~/learning-ai && source venv/bin/activate && python base_knowledge.py'
alias aide='cat ~/learning-ai/COMMANDES_IA.txt'
# ========================================

EOF

echo -e "${GREEN}✅ Alias configurés avec succès!${NC}"
echo ""
echo -e "${BLUE}📝 Commandes disponibles:${NC}"
echo "  shpekoo       - Interface web"
echo "  pentest       - Assistant pentesting"
echo "  bruteforce    - Brute force & crack"
echo "  train         - Entraînement (100 itérations)"
echo "  trainforever  - Entraînement infini"
echo "  collective    - Cerveau collectif"
echo "  cyber         - Charger connaissances cyber"
echo "  prog          - Charger connaissances programmation"
echo "  base          - Charger connaissances de base"
echo "  aide          - Voir toutes les commandes"
echo ""
echo -e "${GREEN}🔄 Exécutez: source ~/.bashrc${NC}"
