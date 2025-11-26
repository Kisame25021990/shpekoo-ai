import json
import re

class AgentPlanner:
    def __init__(self, ai_model, tools):
        self.ai_model = ai_model
        self.tools = tools
    
    def plan_task(self, task):
        """Décompose une tâche en étapes - utilise l'IA si disponible, sinon plan par défaut"""
        # Essaie d'abord avec l'IA pour générer du code intelligent
        if self.ai_model and self.ai_model.is_available():
            ai_plan = self._ai_plan(task)
            if ai_plan['success']:
                return ai_plan
        
        # Sinon, utilise le plan par défaut
        return self._default_plan(task)
    
    def _ai_plan(self, task):
        """Utilise l'IA pour générer du code directement avec un prompt optimisé"""
        
        # Prompt unique optimisé pour générer du code de qualité
        code_prompt = f"""Tu es un développeur Python expert. Génère un script Python complet et fonctionnel.

Demande: {task}

Instructions:
- Génère UNIQUEMENT du code Python, sans explications
- Le code doit être complet et prêt à l'exécution
- Utilise les bonnes pratiques Python
- Ajoute des commentaires uniquement si nécessaire
- Si la demande concerne des emails, utilise smtplib
- Si la demande concerne du web scraping, utilise requests et beautifulsoup4
- Si la demande concerne des fichiers, utilise os et shutil
- Inclus la gestion des erreurs basique

Si la demande est impossible ou pas claire, réponds 'IMPOSSIBLE'.

Code Python:"""
        
        code_result = self.ai_model.chat(code_prompt, "")
        
        if not code_result['success'] or 'IMPOSSIBLE' in code_result['answer'].upper():
            return {'success': False}
        
        # Extrait le code Python de la réponse
        code = code_result['answer'].strip()
        
        # Nettoie le code (enlève les balises markdown si présentes)
        if '```python' in code:
            code = code.split('```python')[1].split('```')[0].strip()
        elif '```' in code:
            code = code.split('```')[1].split('```')[0].strip()
        
        # Vérifie que c'est du code Python valide
        if not code or len(code) < 10:
            return {'success': False}
        
        # Génère un nom de fichier basé sur la tâche
        filename = 'script_genere.py'
        if 'email' in task.lower():
            filename = 'automatisation_emails.py'
        elif 'web' in task.lower() or 'scraping' in task.lower():
            filename = 'web_scraping.py'
        elif 'fichier' in task.lower():
            filename = 'gestion_fichiers.py'
        elif 'bot' in task.lower():
            filename = 'bot.py'
        
        return {
            'success': True,
            'steps': [{
                'action': 'create_file',
                'params': {
                    'filename': filename,
                    'content': code
                }
            }]
        }
    
    def _default_plan(self, task):
        """Plan par défaut intelligent basé sur mots-clés"""
        task_lower = task.lower()
        
        if any(word in task_lower for word in ['script', 'fichier', 'créer', 'crée', 'programme', 'code', 'exemple', 'fais', 'génère']):
            
            if 'variable' in task_lower:
                content = '''# Variables en Python
nom = "Shpekoo"
age = 25
taille = 1.75
est_actif = True

print(f"Nom: {nom}")
print(f"Age: {age}")
print(f"Taille: {taille}m")
print(f"Actif: {est_actif}")'''
            
            elif 'liste' in task_lower or 'list' in task_lower:
                content = '''# Listes en Python
fruits = ["pomme", "banane", "orange", "fraise"]
nombres = [1, 2, 3, 4, 5]

print(f"Fruits: {fruits}")
print(f"Premier fruit: {fruits[0]}")
print(f"Nombre de fruits: {len(fruits)}")

fruits.append("kiwi")
print(f"Après ajout: {fruits}")

for fruit in fruits:
    print(f"- {fruit}")'''
            
            elif 'tuple' in task_lower:
                content = '''# Tuples en Python
coordonnees = (10, 20)
personne = ("Alice", 25, "Paris")
couleurs = ("rouge", "vert", "bleu")

print(f"Coordonnées: {coordonnees}")
print(f"X: {coordonnees[0]}, Y: {coordonnees[1]}")

print(f"\\nPersonne: {personne}")
print(f"Nom: {personne[0]}")
print(f"Age: {personne[1]}")
print(f"Ville: {personne[2]}")

print(f"\\nCouleurs: {couleurs}")
for couleur in couleurs:
    print(f"- {couleur}")'''
            
            elif 'dictionnaire' in task_lower or 'dict' in task_lower:
                content = '''# Dictionnaires en Python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "profession": "Développeur"
}

print(f"Personne: {personne}")
print(f"Nom: {personne['nom']}")
print(f"Age: {personne['age']}")

personne["email"] = "alice@example.com"
print(f"\\nAprès ajout: {personne}")

print("\\nToutes les informations:")
for cle, valeur in personne.items():
    print(f"- {cle}: {valeur}")'''
            
            elif 'while' in task_lower:
                content = '''# Boucle while en Python
compteur = 0
while compteur < 5:
    print(f"Compteur: {compteur}")
    compteur += 1

print("\\nBoucle while avec condition:")
nombre = 1
while nombre <= 10:
    print(f"Nombre: {nombre}")
    nombre += 2'''
            
            elif 'boucle' in task_lower or 'for' in task_lower:
                content = '''# Boucles en Python

print("Boucle for:")
for i in range(5):
    print(f"Nombre: {i}")

print("\\nBoucle sur liste:")
nombres = [1, 2, 3, 4, 5]
for n in nombres:
    print(f"Carré de {n} = {n**2}")'''
            
            elif 'fonction' in task_lower:
                content = '''# Fonctions en Python

def calculer_carre(nombre):
    """Calcule le carré d'un nombre"""
    return nombre * nombre

def saluer(nom):
    """Retourne un message de salutation"""
    return f"Bonjour {nom}!"

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

print(calculer_carre(5))
print(saluer("Shpekoo"))
print(additionner(10, 20))'''
            
            elif 'condition' in task_lower or 'if' in task_lower:
                content = '''# Conditions en Python
age = 18
note = 15

if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

if note >= 16:
    print("Excellent!")
elif note >= 14:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")'''
            
            elif 'string' in task_lower or 'chaîne' in task_lower or 'texte' in task_lower:
                content = '''# Manipulation de strings en Python
texte = "Python est génial"

print(f"Texte: {texte}")
print(f"Majuscules: {texte.upper()}")
print(f"Minuscules: {texte.lower()}")
print(f"Longueur: {len(texte)}")
print(f"Remplacer: {texte.replace('génial', 'super')}")

mots = texte.split()
print(f"Mots: {mots}")

prenom = "Alice"
nom = "Dupont"
nom_complet = prenom + " " + nom
print(f"Nom complet: {nom_complet}")'''
            
            elif 'opérateur' in task_lower:
                content = '''# Opérateurs en Python
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Soustraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Division entière: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Puissance: {a} ** {b} = {a ** b}")

print(f"\\n{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")'''
            
            else:
                content = '''# Script Python
print("Hello World!")

nom = input("Quel est ton nom? ")
age = input("Quel âge as-tu? ")

print(f"\\nBonjour {nom}!")
print(f"Tu as {age} ans.")'''
            
            return {
                'success': True,
                'steps': [{
                    'action': 'create_file',
                    'params': {
                        'filename': 'exemple_python.py',
                        'content': content
                    }
                }]
            }
        
        return {'success': False, 'error': 'Tâche non reconnue'}
    
    def execute_plan(self, steps):
        """Exécute un plan étape par étape"""
        results = []
        
        for i, step in enumerate(steps):
            action = step.get('action')
            params = step.get('params', {})
            
            # Validation des paramètres
            if action == 'create_file':
                if 'filename' not in params or 'content' not in params:
                    return {
                        'success': False,
                        'error': f"Paramètres manquants pour create_file",
                        'results': results
                    }
            
            if hasattr(self.tools, action):
                try:
                    method = getattr(self.tools, action)
                    result = method(**params)
                    results.append({
                        'step': i+1,
                        'action': action,
                        'result': result
                    })
                    
                    if not result.get('success'):
                        return {
                            'success': False,
                            'error': f"Échec à l'étape {i+1}: {result.get('error', 'Erreur inconnue')}",
                            'results': results
                        }
                except Exception as e:
                    return {
                        'success': False,
                        'error': f"Exception à l'étape {i+1}: {str(e)}",
                        'results': results
                    }
            else:
                return {
                    'success': False,
                    'error': f"Action inconnue: {action}",
                    'results': results
                }
        
        return {'success': True, 'results': results}
    
    def execute_task(self, task):
        """Planifie et exécute une tâche complète"""
        plan = self.plan_task(task)
        
        if not plan['success']:
            return plan
        
        return self.execute_plan(plan['steps'])
