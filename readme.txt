-----python-----
1- Instalar o python para rodar os scripts
2 - Criar o ambiente virtual python -m nome_do_ambiente (para ativar use ./Scripts/activate no cmd)
3- Instale as bibliotecas do arquivo requirements usando: pip install -r requirements.txt
4- Altere o ip/porta dos scripts para o ip da sua vm/wsl
-----docker-compose-replication-----
1- Instale o docker em um ambiente linux ou no wsl
1.2- inicie o serviço do docker sudo service docker start
2- Coloque o arquivo do sentinel.conf na mesma pasta do docker compose
3- Rode o comando docker-compose up -d
4- Use o comando ip addr para descobrir o ip da vm/wsl para poder se conectar ao redis de forma externa
5- Para acessar o container use : docker exec -it redis-master redis-cli -p 6380
---docer-compose-cluster------
1- instale o docker em um ambiente linux ou no wsl
2- Copie os arquivos do docker-compose-cluster.yml e node1.conf,node2.conf,node3.conf para sua vm ou wsl
3-Substitua o IP pelo IP do WSL / VM
4- rode o comando docker-compose -f docker-compose-cluster.yml up -d
5- Crie o cluster com: docker run -it --rm --network host redis:7-alpine redis-cli --cluster create  
6- Acesse pelo ip da VM ou WSL 

portas:
Node	Redis Port	Cluster Bus Port
node-1	  7001	       17001
node-2	  7002	       17002
node-3	  7003	       17003


----Conferir os arquivos .conf para mudar os parâmetros com o seu IP---------

----SCRIPTS-----
1.lab-sentinel.py:
Conexão básica usando sentinel para identificar master/slave
2.conexao-standalone:
Conexão simples em um nó
3.lab-buffer-hash.py:
Simula clientes fazendo um hgetall no redis
4.lab-cluster.py
Conexão simples feita com o redis no modo cluster
5.lab-buffer-lrange.py
Simula clientes fazendos lrange no redis
6.lab-buffer-str.py
Simula clientes fazendo um get no redis
7.lab-buffer-lpush
Simula clientes fazendo um lpush em uma lista
8.criar_listra_monstra.py
Cria uma lista no redis para fazer o lab lrange e lpush