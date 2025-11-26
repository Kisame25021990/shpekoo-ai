import subprocess
import os

class BruteForceAssistant:
    def __init__(self):
        self.workspace = "/home/shpekoo/pentest-workspace"
        os.makedirs(self.workspace, exist_ok=True)
    
    def hydra_ssh(self, target, username, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Brute force SSH avec Hydra"""
        command = f'hydra -l {username} -P {wordlist} ssh://{target} -t 4'
        
        print(f"🔓 Brute force SSH sur {target}")
        print(f"   User: {username}")
        print(f"   Wordlist: {wordlist}")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def hydra_ftp(self, target, username, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Brute force FTP avec Hydra"""
        command = f'hydra -l {username} -P {wordlist} ftp://{target} -t 4'
        
        print(f"🔓 Brute force FTP sur {target}")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def hydra_http_post(self, target, username, wordlist, login_page, fail_string):
        """Brute force formulaire HTTP POST"""
        command = f'hydra -l {username} -P {wordlist} {target} http-post-form "{login_page}:^USER^=^PASS^:{fail_string}" -t 4'
        
        print(f"🔓 Brute force HTTP POST sur {target}")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def john_crack(self, hash_file, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Crack de hash avec John the Ripper"""
        command = f'john --wordlist={wordlist} {hash_file}'
        
        print(f"🔓 Crack de hash avec John")
        print(f"   Hash file: {hash_file}")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def hashcat_crack(self, hash_file, hash_type, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Crack de hash avec Hashcat"""
        # Types courants: 0=MD5, 100=SHA1, 1000=NTLM, 1400=SHA256, 3200=bcrypt
        command = f'hashcat -m {hash_type} -a 0 {hash_file} {wordlist}'
        
        print(f"🔓 Crack de hash avec Hashcat")
        print(f"   Type: {hash_type}")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def medusa_ssh(self, target, username, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Brute force SSH avec Medusa"""
        command = f'medusa -h {target} -u {username} -P {wordlist} -M ssh -t 4'
        
        print(f"🔓 Brute force SSH avec Medusa")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def ncrack_rdp(self, target, username, wordlist='/usr/share/wordlists/rockyou.txt'):
        """Brute force RDP avec Ncrack"""
        command = f'ncrack -u {username} -P {wordlist} rdp://{target}'
        
        print(f"🔓 Brute force RDP")
        print(f"   Commande: {command}\n")
        
        return self._execute(command)
    
    def create_custom_wordlist(self, base_word, output_file='custom_wordlist.txt'):
        """Crée une wordlist personnalisée avec des variations"""
        variations = [
            base_word,
            base_word.lower(),
            base_word.upper(),
            base_word.capitalize(),
            f"{base_word}123",
            f"{base_word}2024",
            f"{base_word}!",
            f"{base_word}@",
            f"123{base_word}",
            f"{base_word}2025",
        ]
        
        # Ajoute des variations avec chiffres
        for i in range(10):
            variations.append(f"{base_word}{i}")
            variations.append(f"{i}{base_word}")
        
        output_path = os.path.join(self.workspace, output_file)
        
        with open(output_path, 'w') as f:
            for word in variations:
                f.write(word + '\n')
        
        print(f"✅ Wordlist créée: {output_path}")
        print(f"   {len(variations)} mots générés")
        
        return {'success': True, 'file': output_path, 'count': len(variations)}
    
    def _execute(self, command):
        """Exécute une commande"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minutes max
                cwd=self.workspace
            )
            
            output = result.stdout + result.stderr
            
            # Sauvegarde le résultat
            output_file = os.path.join(self.workspace, 'brute_force_result.txt')
            with open(output_file, 'w') as f:
                f.write(output)
            
            return {
                'success': True,
                'output': output,
                'file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Timeout (5 min)'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def show_wordlists(self):
        """Affiche les wordlists disponibles"""
        wordlist_paths = [
            '/usr/share/wordlists/rockyou.txt',
            '/usr/share/wordlists/dirb/common.txt',
            '/usr/share/wordlists/metasploit/',
            '/usr/share/seclists/',
        ]
        
        print("📚 WORDLISTS DISPONIBLES:\n")
        
        for path in wordlist_paths:
            if os.path.exists(path):
                if os.path.isfile(path):
                    size = os.path.getsize(path)
                    print(f"✅ {path} ({size // 1024} KB)")
                else:
                    print(f"✅ {path} (dossier)")
            else:
                print(f"❌ {path} (non trouvé)")

if __name__ == '__main__':
    bf = BruteForceAssistant()
    
    print("🔓 ASSISTANT BRUTE FORCE")
    print("=" * 60)
    print("⚠️  AVERTISSEMENT: Utilisez uniquement sur vos propres systèmes")
    print("    ou avec autorisation explicite!\n")
    print("=" * 60)
    print("\n1. Brute force SSH (Hydra)")
    print("2. Brute force FTP (Hydra)")
    print("3. Brute force HTTP POST (Hydra)")
    print("4. Crack hash (John the Ripper)")
    print("5. Crack hash (Hashcat)")
    print("6. Créer wordlist personnalisée")
    print("7. Voir wordlists disponibles")
    
    choice = input("\nChoix (1-7): ").strip()
    
    if choice == '1':
        target = input("Cible (IP): ")
        username = input("Username: ")
        wordlist = input("Wordlist (Enter = rockyou.txt): ").strip()
        if not wordlist:
            wordlist = '/usr/share/wordlists/rockyou.txt'
        
        result = bf.hydra_ssh(target, username, wordlist)
        if result['success']:
            print(result['output'])
    
    elif choice == '2':
        target = input("Cible (IP): ")
        username = input("Username: ")
        result = bf.hydra_ftp(target, username)
        if result['success']:
            print(result['output'])
    
    elif choice == '3':
        target = input("Cible (ex: 192.168.1.1): ")
        username = input("Username: ")
        wordlist = input("Wordlist: ")
        login_page = input("Page login (ex: /login.php): ")
        fail_string = input("String d'échec (ex: 'Invalid'): ")
        
        result = bf.hydra_http_post(target, username, wordlist, login_page, fail_string)
        if result['success']:
            print(result['output'])
    
    elif choice == '4':
        hash_file = input("Fichier de hash: ")
        result = bf.john_crack(hash_file)
        if result['success']:
            print(result['output'])
    
    elif choice == '5':
        hash_file = input("Fichier de hash: ")
        hash_type = input("Type (0=MD5, 100=SHA1, 1000=NTLM, 1400=SHA256): ")
        result = bf.hashcat_crack(hash_file, hash_type)
        if result['success']:
            print(result['output'])
    
    elif choice == '6':
        base_word = input("Mot de base: ")
        result = bf.create_custom_wordlist(base_word)
        print(f"\n✅ Wordlist: {result['file']}")
    
    elif choice == '7':
        bf.show_wordlists()
    
    else:
        print("Choix invalide")
