from redis.sentinel import Sentinel


sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)

master = sentinel.master_for('mymaster', socket_timeout=0.1, decode_responses=True)
slave = sentinel.slave_for('mymaster', socket_timeout=0.1, decode_responses=True)   


master.set('chave', 'teste')
print('Lido do slave:', slave.get('chave'))