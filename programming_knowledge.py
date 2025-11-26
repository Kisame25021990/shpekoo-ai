"""
Base de connaissances en programmation multi-langages
"""

PROGRAMMING_KNOWLEDGE = {
    # JavaScript
    "JavaScript": """Langage de programmation pour le web (frontend et backend avec Node.js).
Syntaxe: let x = 10; const name = "John"; function hello() { return "Hi"; }
Frameworks: React, Vue, Angular, Express, Next.js
Utilisations: Sites web interactifs, applications web, APIs""",

    "React": """Bibliothèque JavaScript pour créer des interfaces utilisateur.
Composants: function App() { return <div>Hello</div>; }
Hooks: useState, useEffect, useContext, useReducer
JSX: Syntaxe HTML dans JavaScript
Props et State pour gérer les données""",

    "Node.js": """Runtime JavaScript côté serveur.
Modules: require(), import/export
NPM: Gestionnaire de packages
Express: Framework web populaire
Async: Promises, async/await pour opérations asynchrones""",

    # TypeScript
    "TypeScript": """JavaScript avec typage statique.
Types: string, number, boolean, array, object
Interfaces: interface User { name: string; age: number; }
Classes: class Person { constructor(name: string) {} }
Compilation vers JavaScript""",

    # HTML/CSS
    "HTML": """Langage de balisage pour structurer les pages web.
Balises: <div>, <p>, <h1>, <a>, <img>, <form>
Attributs: class, id, src, href
Sémantique: <header>, <nav>, <main>, <footer>, <article>""",

    "CSS": """Langage de style pour les pages web.
Sélecteurs: .class, #id, element, [attribute]
Propriétés: color, background, margin, padding, display, flex
Responsive: @media queries, flexbox, grid
Animations: transition, @keyframes""",

    # Python avancé
    "Python avancé": """Concepts avancés Python.
Décorateurs: @decorator pour modifier des fonctions
Générateurs: yield pour itération lazy
Context managers: with statement
Métaclasses: Personnaliser la création de classes
Async: asyncio, async/await""",

    # Java
    "Java": """Langage orienté objet pour applications enterprise.
Classes: public class MyClass { }
Héritage: extends, implements
Collections: ArrayList, HashMap, HashSet
Exceptions: try-catch-finally
Spring Framework pour applications web""",

    # C/C++
    "C": """Langage bas niveau pour performance.
Pointeurs: int *ptr = &variable;
Mémoire: malloc(), free()
Structures: struct Person { char name[50]; int age; };
Compilation: gcc, make""",

    "C++": """Extension orientée objet de C.
Classes: class MyClass { public: void method(); };
Templates: template<typename T>
STL: vector, map, set, algorithm
Smart pointers: unique_ptr, shared_ptr""",

    # PHP
    "PHP": """Langage serveur pour le web.
Syntaxe: <?php echo "Hello"; ?>
Variables: $name = "John";
Arrays: $arr = array(1, 2, 3);
MySQL: mysqli, PDO pour bases de données
Laravel: Framework PHP moderne""",

    # Ruby
    "Ruby": """Langage élégant et expressif.
Syntaxe: puts "Hello"
Blocs: array.each { |item| puts item }
Classes: class Person; end
Rails: Framework web populaire""",

    # Go
    "Go": """Langage de Google pour performance et concurrence.
Syntaxe: func main() { fmt.Println("Hello") }
Goroutines: go function() pour concurrence
Channels: ch := make(chan int)
Compilation rapide, typage statique""",

    # Rust
    "Rust": """Langage système sûr et performant.
Ownership: Gestion mémoire sans garbage collector
Borrowing: &variable pour références
Pattern matching: match expression
Cargo: Gestionnaire de packages""",

    # SQL
    "SQL": """Langage pour bases de données relationnelles.
SELECT: SELECT * FROM users WHERE age > 18;
INSERT: INSERT INTO users (name, age) VALUES ('John', 25);
UPDATE: UPDATE users SET age = 26 WHERE id = 1;
JOIN: INNER JOIN, LEFT JOIN, RIGHT JOIN
Bases: MySQL, PostgreSQL, SQLite""",

    # Git
    "Git": """Système de contrôle de version.
Commandes: git init, git add, git commit, git push, git pull
Branches: git branch, git checkout, git merge
Remote: git remote add origin url
Workflow: feature branches, pull requests""",

    # Docker
    "Docker": """Conteneurisation d'applications.
Dockerfile: FROM, RUN, COPY, CMD
Images: docker build, docker pull
Containers: docker run, docker ps, docker stop
Docker Compose: Orchestration multi-conteneurs""",

    # APIs REST
    "API REST": """Architecture pour services web.
Méthodes HTTP: GET, POST, PUT, DELETE, PATCH
Status codes: 200 OK, 201 Created, 404 Not Found, 500 Error
JSON: Format d'échange de données
Authentication: JWT, OAuth, API keys""",

    # GraphQL
    "GraphQL": """Langage de requête pour APIs.
Query: query { user(id: 1) { name email } }
Mutation: mutation { createUser(name: "John") { id } }
Schema: type User { id: ID! name: String! }
Avantages: Requêtes précises, pas de over-fetching""",

    # MongoDB
    "MongoDB": """Base de données NoSQL orientée documents.
Documents: JSON-like { name: "John", age: 25 }
Collections: Équivalent des tables SQL
Requêtes: db.users.find({ age: { $gt: 18 } })
Mongoose: ODM pour Node.js""",

    # Redis
    "Redis": """Base de données en mémoire clé-valeur.
Commandes: SET key value, GET key, DEL key
Structures: Strings, Lists, Sets, Hashes, Sorted Sets
Cache: Très rapide pour mise en cache
Pub/Sub: Messagerie temps réel""",

    # Kubernetes
    "Kubernetes": """Orchestration de conteneurs.
Pods: Unité de déploiement
Services: Exposition des applications
Deployments: Gestion des réplicas
kubectl: CLI pour gérer le cluster""",

    # AWS
    "AWS": """Services cloud Amazon.
EC2: Serveurs virtuels
S3: Stockage d'objets
Lambda: Fonctions serverless
RDS: Bases de données managées
CloudFormation: Infrastructure as Code""",

    # Linux
    "Linux": """Système d'exploitation open source.
Commandes: ls, cd, mkdir, rm, cp, mv, grep, find
Permissions: chmod, chown
Processus: ps, top, kill
Shell: bash, zsh
Distributions: Ubuntu, Debian, CentOS, Arch""",

    # Regex
    "Regex": """Expressions régulières pour pattern matching.
Caractères: . (any), * (0+), + (1+), ? (0-1)
Classes: [a-z], [0-9], \\d (digit), \\w (word), \\s (space)
Groupes: (pattern), (?:pattern) non-capturant
Anchors: ^ (début), $ (fin), \\b (word boundary)""",
}

def load_programming_knowledge(ai):
    """Charge toutes les connaissances de programmation"""
    print("💻 Chargement de la base de connaissances programmation...")
    
    for topic, content in PROGRAMMING_KNOWLEDGE.items():
        ai.learn(f"Qu'est-ce que {topic}?", content)
        print(f"  ✅ {topic}")
    
    print(f"\n✅ {len(PROGRAMMING_KNOWLEDGE)} langages/technologies chargés !")

if __name__ == '__main__':
    from brain import LearningAI
    
    ai = LearningAI('memory.json')
    load_programming_knowledge(ai)
    
    print("\n📊 Statistiques:")
    stats = ai.stats()
    print(f"  Total connaissances: {stats.get('total_knowledge', 0)}")
    print(f"  (Cyber + Programmation + Python)")
