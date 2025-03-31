from redis.cluster import RedisCluster, ClusterNode

# Define os nós corretamente
startup_nodes = [ ClusterNode("localhost", 7001)]

# Cria o client
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
rc.set("chave", "valor")
print(rc.get("chave"))

