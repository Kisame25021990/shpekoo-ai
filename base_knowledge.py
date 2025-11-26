#!/usr/bin/env python3
"""
Connaissances de base pour Shpekoo-AI
À charger lors de l'installation pour avoir une IA déjà compétente
"""

from brain import LearningAI

def load_base_knowledge():
    ai = LearningAI()
    
    # Python avancé
    knowledge = [
        # Structures de données
        "Les dictionnaires Python permettent de stocker des paires clé-valeur. Exemple: user = {'name': 'Alice', 'age': 30}",
        "Les sets en Python sont des collections non ordonnées sans doublons. Exemple: nombres = {1, 2, 3, 3} donnera {1, 2, 3}",
        "Les tuples sont immuables contrairement aux listes. Exemple: coordonnees = (10, 20) ne peut pas être modifié",
        "List comprehension: [x**2 for x in range(10)] crée une liste des carrés de 0 à 9",
        "Dict comprehension: {x: x**2 for x in range(5)} crée un dictionnaire {0:0, 1:1, 2:4, 3:9, 4:16}",
        
        # Fonctions avancées
        "Les fonctions lambda sont des fonctions anonymes: lambda x: x*2 équivaut à def double(x): return x*2",
        "map() applique une fonction à chaque élément: list(map(lambda x: x*2, [1,2,3])) donne [2,4,6]",
        "filter() filtre les éléments: list(filter(lambda x: x>5, [3,6,9])) donne [6,9]",
        "Les décorateurs modifient le comportement d'une fonction avec @decorator_name",
        "Les générateurs utilisent yield au lieu de return pour économiser la mémoire",
        
        # Gestion d'erreurs
        "try/except permet de gérer les erreurs: try: x=1/0 except ZeroDivisionError: print('Division par zéro')",
        "finally s'exécute toujours après try/except, utile pour fermer des fichiers",
        "raise permet de lever une exception personnalisée: raise ValueError('Message d'erreur')",
        
        # Fichiers
        "with open('file.txt', 'r') as f: content = f.read() ferme automatiquement le fichier",
        "Modes de fichiers: 'r' lecture, 'w' écriture (écrase), 'a' ajout, 'r+' lecture/écriture",
        "json.dumps() convertit Python en JSON, json.loads() convertit JSON en Python",
        
        # POO
        "Une classe définit un modèle: class Dog: def __init__(self, name): self.name = name",
        "L'héritage permet de réutiliser du code: class Puppy(Dog): pass hérite de Dog",
        "Les méthodes magiques commencent par __ : __str__, __repr__, __len__, __add__",
        "Les propriétés utilisent @property pour créer des getters/setters élégants",
        
        # Web & APIs
        "requests.get('url') fait une requête HTTP GET, requests.post('url', data={}) fait un POST",
        "Flask crée des APIs web: @app.route('/api') def api(): return {'data': 'value'}",
        "Les status codes HTTP: 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error",
        "CORS permet les requêtes cross-origin: from flask_cors import CORS; CORS(app)",
        
        # Bases de données
        "SQLite est intégré à Python: import sqlite3; conn = sqlite3.connect('db.sqlite')",
        "SQL SELECT: SELECT * FROM users WHERE age > 18 ORDER BY name LIMIT 10",
        "SQL INSERT: INSERT INTO users (name, age) VALUES ('Alice', 25)",
        "SQL UPDATE: UPDATE users SET age = 26 WHERE name = 'Alice'",
        "SQL DELETE: DELETE FROM users WHERE age < 18",
        
        # Git & GitHub
        "git init initialise un dépôt, git add . ajoute tous les fichiers, git commit -m 'message' enregistre",
        "git push origin main envoie sur GitHub, git pull récupère les changements",
        "git branch nouvelle_branche crée une branche, git checkout branche change de branche",
        "git merge fusionne des branches, git clone url copie un dépôt distant",
        ".gitignore liste les fichiers à ignorer: *.pyc, venv/, __pycache__/, .env",
        
        # Linux & Terminal
        "ls liste les fichiers, cd change de dossier, pwd affiche le chemin actuel",
        "mkdir crée un dossier, rm supprime, cp copie, mv déplace/renomme",
        "chmod +x file.sh rend un script exécutable, chmod 755 donne rwxr-xr-x",
        "grep 'pattern' file.txt cherche un motif, | pipe connecte des commandes",
        "ps aux liste les processus, kill -9 PID tue un processus",
        
        # Sécurité Web
        "XSS (Cross-Site Scripting): injection de JavaScript malveillant dans une page web",
        "SQL Injection: injection de code SQL via les inputs utilisateur, utiliser des requêtes préparées",
        "CSRF (Cross-Site Request Forgery): forcer un utilisateur à exécuter des actions non désirées",
        "Toujours valider et nettoyer les inputs utilisateur côté serveur",
        "Hasher les mots de passe avec bcrypt ou argon2, jamais en clair",
        "HTTPS chiffre les communications, utiliser des certificats SSL/TLS",
        
        # Pentesting
        "Reconnaissance: whois, nslookup, dig pour info sur domaines et DNS",
        "Nmap -sV scan les versions de services, -sC lance les scripts par défaut",
        "Gobuster dir -u URL -w wordlist.txt brute force les répertoires web",
        "Burp Suite intercepte et modifie les requêtes HTTP pour tester les vulnérabilités",
        "Metasploit: use exploit/..., set RHOST, set LHOST, exploit lance l'attaque",
        
        # Réseau
        "TCP est orienté connexion (fiable), UDP est sans connexion (rapide)",
        "Ports courants: 22 SSH, 80 HTTP, 443 HTTPS, 3306 MySQL, 5432 PostgreSQL",
        "ping teste la connectivité, traceroute montre le chemin réseau",
        "netstat -tulpn affiche les ports en écoute sur Linux",
        
        # Docker
        "docker build -t nom:tag . construit une image depuis un Dockerfile",
        "docker run -p 8080:80 nom lance un conteneur avec mapping de port",
        "docker ps liste les conteneurs actifs, docker ps -a liste tous les conteneurs",
        "docker-compose up -d lance plusieurs conteneurs définis dans docker-compose.yml",
        
        # JavaScript/Node.js
        "const et let pour déclarer des variables, éviter var",
        "Arrow functions: const add = (a, b) => a + b",
        "Promises gèrent l'asynchrone: promise.then().catch()",
        "async/await simplifie les promises: async function getData() { const data = await fetch(url) }",
        "npm install package installe un package, npm init crée package.json",
        
        # React
        "useState gère l'état: const [count, setCount] = useState(0)",
        "useEffect gère les effets de bord: useEffect(() => { /* code */ }, [dependencies])",
        "Props passent des données aux composants: <Component name='Alice' />",
        "JSX mélange HTML et JavaScript: <div>{variable}</div>",
        
        # Algorithmes
        "Complexité O(1) constant, O(n) linéaire, O(n²) quadratique, O(log n) logarithmique",
        "Tri rapide (quicksort) est O(n log n) en moyenne, efficace pour grandes listes",
        "Recherche binaire est O(log n), nécessite une liste triée",
        "Les hash tables offrent O(1) pour recherche/insertion en moyenne",
        
        # DevOps
        "CI/CD automatise les tests et déploiements: GitHub Actions, GitLab CI, Jenkins",
        "Infrastructure as Code: Terraform, Ansible pour gérer l'infrastructure",
        "Monitoring: Prometheus, Grafana pour surveiller les applications",
        "Logs centralisés: ELK Stack (Elasticsearch, Logstash, Kibana)",
        
        # Best Practices
        "DRY (Don't Repeat Yourself): éviter la duplication de code",
        "KISS (Keep It Simple, Stupid): privilégier la simplicité",
        "SOLID: principes de conception orientée objet",
        "Tests unitaires avec pytest ou unittest pour valider le code",
        "Code review améliore la qualité, utiliser des pull requests",
        "Documentation: docstrings Python, README.md, commentaires pertinents",
        
        # Outils de développement
        "VS Code: éditeur populaire avec extensions Python, Git, Docker",
        "Virtual environments: python -m venv venv isole les dépendances",
        "pip freeze > requirements.txt sauvegarde les dépendances",
        "Black formate le code Python automatiquement",
        "pylint et flake8 analysent la qualité du code",
        
        # APIs & Formats
        "REST API: GET récupère, POST crée, PUT/PATCH modifie, DELETE supprime",
        "JSON est le format standard pour les APIs: {'key': 'value'}",
        "XML est plus verbeux: <root><key>value</key></root>",
        "GraphQL permet de requêter exactement les données nécessaires",
        
        # Cloud & AWS
        "EC2: machines virtuelles dans le cloud",
        "S3: stockage d'objets (fichiers) scalable",
        "Lambda: fonctions serverless, paiement à l'usage",
        "RDS: bases de données managées (MySQL, PostgreSQL)",
        "IAM: gestion des identités et accès",
    ]
    
    print("🧠 Chargement des connaissances de base...")
    count = 0
    for k in knowledge:
        ai.learn(k)
        count += 1
        if count % 10 == 0:
            print(f"   ✓ {count}/{len(knowledge)} connaissances chargées")
    
    print(f"\n✅ {len(knowledge)} connaissances de base chargées avec succès!")
    print(f"📊 Total dans la mémoire: {len(ai.memory)} entrées")

if __name__ == "__main__":
    load_base_knowledge()
