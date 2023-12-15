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

Execício 1

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

Digitar no terminal

```
# entrar na pasta do exercício 2
cd aula/ex2

# gerar a imagem do exercício 2 com o nome ex2
docker build . -t ex2:1.0

# subir o container do exercício 1
docker run -d ex2:1.0

# verificar os containers que estão rodando na máquina
docker ps

# acessar o terminal docker container via linha de comando
docker ps
```
