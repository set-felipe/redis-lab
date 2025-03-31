import redis
import threading
import time


contador_requisicoes = 0
lock = threading.Lock()


def cliente_lento(id_cliente):
    global contador_requisicoes
    r = redis.Redis(host='localhost', port=6060)
    while True:
        data = r.hgetall('meu_hash_gigante')
        with lock:
            contador_requisicoes += 1



def monitor_rps():
    global contador_requisicoes
    while True:
        time.sleep(1)
        with lock:
            print(f"RPS Atual: {contador_requisicoes} requests/segundo")
            contador_requisicoes = 0

threading.Thread(target=monitor_rps, daemon=True).start()


for i in range(5):
    t = threading.Thread(target=cliente_lento, args=(i,))
    t.start()


while True:
    time.sleep(1)