import redis

# Conexão com o Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Nome da lista
chave = 'lista_monstra'

# Remove a lista se ela já existir
r.delete(chave)

print("Criando lista_monstra com 100.000 posições...")

# Inserção em lote
for i in range(100_000):
    r.rpush(chave, f"valor_{i}")

print("Lista criada com sucesso!")
print(f"Tamanho da lista: {r.llen(chave)}")