
import redis
import threading
import time
import random
import string
'''
r = redis.Redis(host='localhost', port=6060)


def cliente_lento(id):
    r = redis.Redis(host='localhost', port=6060)
    while True:
        data = r.hgetall('meu_hash_gigante')
        print(f"Cliente {id} leu {len(data)} campos.")
        time.sleep(1)  # Simula cliente lento (buffer não esvazia rápido)

# Criar 5 clientes simultâneos lendo o hash
for i in range(5):
    t = threading.Thread(target=cliente_lento, args=(i,))
    t.start()
'''
contador_requisicoes = 0
lock = threading.Lock()

# Cliente rápido lendo chave pequena
def cliente_rapido(id_cliente):
    global contador_requisicoes
    r = redis.Redis(host='127.0.0.1', port=6060, decode_responses=True)
    chave = 'simulacao:string:0'

    while True:
        valor = r.get(chave)
        with lock:
            contador_requisicoes += 1
        
        

# Monitor de RPS
def monitor_rps():
    global contador_requisicoes
    while True:
        time.sleep(1)
        with lock:
            print(f"📊 RPS Atual: {contador_requisicoes} requests/segundo")
            contador_requisicoes = 0

# Inicia monitor
threading.Thread(target=monitor_rps, daemon=True).start()

# Inicia clientes rápidos
for i in range(3):
    threading.Thread(target=cliente_rapido, args=(i,)).start()

# Mantém o script rodando (impede encerramento prematuro)
while True:
    time.sleep(1)