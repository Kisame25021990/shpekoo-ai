"""
Analyseur de résultats de scan pour expliquer ce qu'on trouve
"""

def analyze_nmap_result(output):
    """Analyse un résultat Nmap et explique ce qu'il faut comprendre"""
    analysis = {
        'summary': '',
        'open_ports': [],
        'recommendations': [],
        'vulnerabilities': []
    }
    
    lines = output.split('\n')
    
    # Détecte les ports ouverts
    for line in lines:
        if 'open' in line and '/tcp' in line:
            parts = line.split()
            port = parts[0].split('/')[0]
            service = parts[2] if len(parts) > 2 else 'unknown'
            
            analysis['open_ports'].append({
                'port': port,
                'service': service,
                'line': line.strip()
            })
    
    # Génère le résumé
    if analysis['open_ports']:
        analysis['summary'] = f"✅ {len(analysis['open_ports'])} port(s) ouvert(s) trouvé(s)"
    else:
        analysis['summary'] = "❌ Aucun port ouvert trouvé"
    
    # Recommandations par service
    for port_info in analysis['open_ports']:
        port = port_info['port']
        service = port_info['service']
        
        if port == '80' or port == '8080':
            analysis['recommendations'].append(
                f"🌐 Port {port} (HTTP) : Scanner avec Gobuster, Nikto, tester XSS/SQL injection"
            )
        
        elif port == '443':
            analysis['recommendations'].append(
                f"🔒 Port {port} (HTTPS) : Vérifier le certificat SSL, scanner avec SSLscan"
            )
        
        elif port == '22':
            analysis['recommendations'].append(
                f"🔑 Port {port} (SSH) : Tester brute force avec Hydra, vérifier la version"
            )
        
        elif port == '21':
            analysis['recommendations'].append(
                f"📁 Port {port} (FTP) : Tester anonymous login, vérifier les vulnérabilités"
            )
        
        elif port == '3306':
            analysis['recommendations'].append(
                f"🗄️ Port {port} (MySQL) : Tester les credentials par défaut, brute force"
            )
        
        elif port == '5000':
            analysis['recommendations'].append(
                f"🐍 Port {port} (Flask/Python) : Application web, scanner avec Burp Suite, tester les APIs"
            )
        
        elif port == '8000' or port == '8888':
            analysis['recommendations'].append(
                f"🌐 Port {port} (Web dev) : Application de développement, vérifier les endpoints"
            )
        
        else:
            analysis['recommendations'].append(
                f"❓ Port {port} ({service}) : Rechercher des exploits pour ce service"
            )
    
    return analysis

def print_analysis(analysis):
    """Affiche l'analyse de manière lisible"""
    print("\n" + "=" * 60)
    print("📊 ANALYSE DU SCAN")
    print("=" * 60)
    
    print(f"\n{analysis['summary']}\n")
    
    if analysis['open_ports']:
        print("🎯 PORTS OUVERTS:")
        for port_info in analysis['open_ports']:
            print(f"  • Port {port_info['port']} - {port_info['service']}")
        
        print("\n💡 RECOMMANDATIONS:")
        for i, rec in enumerate(analysis['recommendations'], 1):
            print(f"  {i}. {rec}")
    
    if analysis['vulnerabilities']:
        print("\n⚠️ VULNÉRABILITÉS POTENTIELLES:")
        for vuln in analysis['vulnerabilities']:
            print(f"  • {vuln}")
    
    print("\n" + "=" * 60)

def explain_scan_basics():
    """Explique les bases d'un scan Nmap"""
    print("""
📚 COMPRENDRE UN SCAN NMAP

🔍 Ce que Nmap fait:
  • Envoie des paquets aux ports de la cible
  • Détecte quels ports sont ouverts (services actifs)
  • Identifie les services qui tournent sur ces ports

📊 États des ports:
  • OPEN : Un service écoute sur ce port (cible potentielle)
  • CLOSED : Aucun service, mais le port répond
  • FILTERED : Firewall bloque les paquets

🎯 Pourquoi c'est important:
  • Les ports ouverts = points d'entrée potentiels
  • Chaque service peut avoir des vulnérabilités
  • C'est la première étape du pentesting

🔐 Prochaines étapes:
  1. Scanner les services en détail (nmap -sV)
  2. Chercher des vulnérabilités connues
  3. Tester les exploits appropriés
""")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        # Analyse un fichier de résultats
        with open(sys.argv[1], 'r') as f:
            output = f.read()
        
        analysis = analyze_nmap_result(output)
        print_analysis(analysis)
    else:
        # Exemple avec le résultat fourni
        example_output = """Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-26 13:19 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000020s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds"""
        
        print("📖 EXPLICATION DES BASES")
        explain_scan_basics()
        
        print("\n📊 EXEMPLE D'ANALYSE")
        analysis = analyze_nmap_result(example_output)
        print_analysis(analysis)
