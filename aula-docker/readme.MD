Conhecendo a command line interface do Docker (Docker CLI)

Verificação da instalação

```
docker
```

Verificação da versão atual do docker

```
docker -v
```

Puxando a primeira imagem do docker hub

```
docker pull hello-world
```

Rodando a primeira imagem docker

```
docker run hello-world
```

Execício 1 (Fazer o build e rodar um container via Dockerfile)

Digitar no terminal

```
# entrar na pasta do exercício 1
cd aula/ex1

# gerar a imagem do exercício 1 com o nome ex1
docker build . -t ex1

# subir o container do exercício 1
docker run ex1

# subir o container do exercício 1 e eliminar ele após rodar todas as linhas do Dockerfile
docker run --rm ex1

# alterar o script do exercício 1 com o texto
print("Esse script foi alterado)

# subir novamente o script do exercício 1 com o argumento --rm
docker run --rm ex1
```

Execício 2

Digitar no terminal (Container sem interrupção e utilização do terminal do container)

```
# entrar na pasta do exercício 2
cd aula/ex2

# gerar a imagem do exercício 2 com o nome ex2
docker build . -t ex2:1.0

# subir o container do exercício 2 com o nome ex2
docker run -d --name ex2 ex2:1.0

# verificar os containers que estão rodando na máquina
docker ps

# acessar o terminal docker container via linha de comando
docker exec -it ex2 bash

# verificar as pastas e os arquivos do container usando o terminal do container
ls

# criar um arquivo teste dentro do container
touch teste
```

Execício 3 (Volumes compartilhados host:container)

Digitar no terminal

```
# entrar na pasta do exercício 3
cd aula/ex3

# gerar a imagem do exercício 3 com o nome ex3
docker build . -t ex3:1.0

# subir o container do exercício 3 com o nome ex3
docker run -d --name ex3 -v ./volume:/ex3/ ex3:1.0

# verificar os containers que estão rodando na máquina
docker ps

# acessar o terminal docker container via linha de comando
docker exec -it ex3 bash

# criar arquivos teste1.txt, teste2.txt e teste3.txt fora do container

# criar o arquivo teste4.txt dentro do container
touch teste4.txt

```

Execício 4 (Parando, removendo, iniciando e resetando containers via Docker CLI)

```
# parando o container do exercício 2
docker stop ex2

# parando o container do exercício 3
docker stop ex3

# verificando situação dos containers
docker ps

# iniciando o container do exercício 2
docker start ex2

# iniciando o container do exercício 3
docker start ex3

# parando todos os containers que estão em execução
docker stop $(docker ps -a -q)

# parando todos os containers que estão parados
docker rm $(docker ps -a -q)
```

Execício 5 (Parando, removendo, iniciando e resetando containers via extensão Docker do VS Code)

```
# inicializando os dois containers
docker run -d --name ex2 ex2:1.0
docker run -d --name ex3 ex3:1.0

# apresentação da janela de containers
# apresentação da janela de imagens
# apresentação da janela de volumes

# parar container ex2
# parar container ex3
# inicializar container ex2
# inicializar container ex3
# acessar terminal do container ex2
# sair do terminal do container ex2
# acessar terminal do conntainer ex3
```

Execício 6 (Mapeamento de portas)

Digitar no terminal

```
# entrar na pasta do exercício 6
cd aula/ex6

# gerar a imagem do exercício  com o nome ex6
docker build . -t ex6:1.0

# subir o container do exercício 6 com o nome ex6 compartilhando o diretório fonte da aplicação
docker run -d --name ex6 -v ./app:/ex6/app ex6:1.0

# tentar acessar a aplicação que está rodando dentro do container no browser pela porta 8000
http://localhost:8000

# remover o container via extensão Docker

# adicionar o mapeamento de portas máquina:container para acessar o container
docker run -d -p 8000:8000 --name ex6 -v ./app:/ex6/app ex6:1.0

# resposta da requisição
{message: "Estou dentro do container"}

# alterar o texto da requisição para "A aplicação foi alterada..." no arquivo main.py

# acessar novamente o browser na porta 8000 e receber a resposta da requisição
{"message": "A aplicação foi alterada..."}

# remover o container ex6 via extensão docker

# alterando o mapeamento das portas para que a porta 9000 redirecione as requisições para a porta 8000 do container
docker run -d -p 9000:8000 --name ex6 -v ./app:/ex6/app ex6:1.0

# acessar a porta 9000 pelo browser e ser redirecionado para a porta 8000 do container
# receber a resposta da requisição da aplicação
{"message": "A aplicação foi alterada..."}

# remover o container ex6 via extensão docker

# alterando o mapeamento das portas para que a porta 8000 redirecione as requisições para a porta 9000 do container
docker run -d -p 8000:9000 --name ex6 -v ./app:/ex6/app ex6:1.0

# a aplicação não tem mais o acesso da porta do servidor do container via mapeamento de portas

```

Execício 7 (Orquestrando múltiplos containers usando Docker Compose)

Digitar no terminal

```
# entrar na pasta do exercício 7
cd aula/ex7

# gerar as imagens de todos os serviços do arquivo docker-compose.yaml
docker-compose build

# rodar os containers de todos os serviços do arquivo docker-compose.yaml com terminal desatachado
docker-compose up -d
```

```
# entrar na pasta do exercício 8
cd aula/ex8

# gerar as imagens de todos os serviços do arquivo docker-compose.yaml
docker-compose build

# rodar os containers de todos os serviços do arquivo docker-compose.yaml com terminal desatachado
docker-compose up -d
```
