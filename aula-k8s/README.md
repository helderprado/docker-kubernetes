Conhecendo a command line interface do Docker (Docker CLI)

Verificação da instalação do Kind

```
kind
```

Verificação da instalação do Kubectl

```
kubectl
```

Criando nosso cluster Kubernetes utilizando o Kind

```
kind create cluster
```

Para se conectar ao cluster nas configuração do Kubernetes para o contexto do kind

```
kubectl cluster-info --context kind-kind
```

Verificando os nós Kubernetes que estão prontos para uso

```
# verificando que o cluster está rodando no docker
docker ps -a

# verificando os nós disponíveis utilizando o kubectl
kubectl get nodes
```

Criando Cluster com multíplos nós utilizando o kind

```

# entrando no diretório da criação do cluster
cd criar-cluster

# criar o cluster com 3 nós workers e um painel de controle no cluster
kind create cluster --config=aula-k8s/ex1/cluster.yaml --name=k8s-cluster

# aplicar o novo contexto para se conectar ao arquivo de configuração do kubectl
kubectl cluster-info --context kind-k8s-cluster

# verificando os nós disponíveis
kubectl get nodes

# verificando cada container do cluster
docker ps -a

```

Criando o primeiro pod no cluster Kubernetes com a nossa aplicação

```

# acesar o diretório
cd criar-pod

# criar a imagem docker da aplicação
docker build -t helderprado/servidor-python:1.0 .

# verificando se o container roda em ambiente docker
docker run --rm -p 8000:8000 helderprado/servidor-python:1.0

# subindo a imagem para o repositório público do Docker Hub
docker push helderprado/servidor-python:1.0

# criar o pod utilizando o arquivod de configuração .yaml
kubectl apply -f pod.yaml

# verificando a situação atual do pod criado
kubectl get pods

# excluindo o pod criado
kubectl delete pod servidor-python

```

```
kubectl apply -f replicaset.yaml

```
