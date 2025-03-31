import redis
import threading
import time

contador_requisicoes = 0
lock = threading.Lock()

def cliente_lento(id_cliente):
    global contador_requisicoes
    r = redis.Redis(host='localhost', port=4242)
    
    while True:
        dados = r.lrange('lista_monstra', 0, -1) 
        with lock:
            contador_requisicoes += 1
        time.sleep(1)  

def monitor():
    global contador_requisicoes
    r = redis.Redis(host='localhost', port=6060, decode_responses=True)
    
    while True:
        time.sleep(1)
        with lock:
            rps = contador_requisicoes
            contador_requisicoes = 0
        memoria = r.info('memory')['used_memory_human']
        print(f"LRANGE RPS: {rps} req/s | Memória Redis: {memoria}")


threading.Thread(target=monitor, daemon=True).start()


for i in range(5):
    threading.Thread(target=cliente_lento, args=(i,)).start()


while True:
    time.sleep(1)