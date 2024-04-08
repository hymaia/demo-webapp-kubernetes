# Webapp click count

## Objectif

J'ai créé cette webapp dans le but de pouvoir faire des démos simples et rapides sur Kubernetes. La webapp est composé d'un front/back déployés ensemble et d'une base de donnée redis. Tout est déployable via `docker-compose`.

## Pré-requis

Avoir d'installé :
* Poetry
* Python 3.10
* Docker et docker-compose
* kubectl
* Un cluster Kubernetes disponible (si vous voulez refaire la démo)

## Local dev

```bash
poetry install
```

## Build

```bash
docker build -t <image_name> .
docker push <image_name>
```

## Local deploy

```bash
docker-compose up -d
```

Et retrouvez la webapp sur [localhost:5000](localhost:5000)

## Kubernetes deploy

```bash
kubectl apply -f webapp.yaml
```

Retrouvez la webapp sur l'ip externe du LoadBalancer via :

```bash
kubectl get svc front-end
```
