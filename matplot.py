import redis
import matplotlib.pyplot as plt
import time


r = redis.Redis(host='localhost', port=6060)


timestamps = []
memory_usage = []


print("Monitorando memória do Redis por 60 segundos...")
for i in range(60):
    used_memory = int(r.info()['used_memory']) / (1024 * 1024)  # Convertendo para MB
    memory_usage.append(used_memory)
    timestamps.append(i)
    
    print(f"{i}s Memória usada: {used_memory:.2f} MB")
    time.sleep(1)

# Plotar o gráfico
plt.plot(timestamps, memory_usage, marker='o')
plt.title('Consumo de Memória do Redis em Tempo Real')
plt.xlabel('Tempo (s)')
plt.ylabel('Memória Usada (MB)')
plt.grid(True)
plt.show()
