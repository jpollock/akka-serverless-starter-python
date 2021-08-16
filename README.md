# Akka Serverless - Python Starter App

A Python-based generic starter app for [Akka Serverless](https://developer.lightbend.com/docs/akka-serverless/).

Features include:

* Eventsourced and Value (CRUD) API implementations
* Both API services leverage the [`Views`](https://developer.lightbend.com/docs/akka-serverless/javascript/views.html) capability

## What is this repository?

To help you get started with Akka Serverless, this is a template repository that you can use as the the starting point for a new Python-based API that can run in Akka Serverless.

## Prerequisites

To build and deploy this example application, you'll need to have:

* An [Akka Serverless account](https://developer.lightbend.com/docs/akka-serverless/getting-started/lightbend-account.html)
* Python 3 installed
* The Docker CLI installed

It is recommended that you use a [virtual environment](https://docs.python.org/3/library/venv.html). It is also useful to have a Python version management system in place ([pyenv](https://github.com/pyenv/pyenv)).

## Develop and Run Locally

1. Define domain schema and API specification in `proto` files.
2. Write business logic in Python files, e.g. `thing_action.py` and `thing_eventsourced_entit.py`.
3. From terminal, `./bin/run.sh`. This will compile the `proto` files and start the service.
4. From another terminal, `docker-compose up` to start the proxy service.

### Use Postman to Try and Test

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/34862-7c169b10-366f-4e72-aff4-8188e0a96d1b?action=collection%2Ffork&collection-url=entityId%3D34862-7c169b10-366f-4e72-aff4-8188e0a96d1b%26entityType%3Dcollection%26workspaceId%3Ddee50495-76e5-4399-afea-21035ae2759d#?env%5BAkka%20Serverless%5D=W3sia2V5IjoiYXBpSG9zdCIsInZhbHVlIjoibG9jYWxob3N0OjkwMDAiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InRscyIsInZhbHVlIjoiaHR0cCIsImVuYWJsZWQiOnRydWV9XQ==)

## Build, Deploy, and Test

This repository contains one service that can be deployed to Akka Serverless. Deployment requires building a container.

### Build your containers

To build your own containers, execute the below commands:

```bash
## Set your dockerhub username
export DOCKER_REGISTRY=docker.io
export DOCKER_USER=<your dockerhub username>


## Build containers for each of the services
## Below assumes that the present working directory is the name of the container you want
## 0.0.1 should be changed to whatever verion numbe is desired
docker build . -t $DOCKER_REGISTRY/$DOCKER_USER/${PWD##*/}:0.0.1

```

### Deploy your container

To deploy the containers as a service in Akka Serverless, you'll need to:

```bash
## Set your dockerhub username
export DOCKER_REGISTRY=docker.io
export DOCKER_USER=<your dockerhub username>

## Push the containers to a container registry
## Below assumes that the present working directory is the name of the container you want
## 0.0.1 should be changed to whatever verion numbe is desired
docker push $DOCKER_REGISTRY/$DOCKER_USER/${PWD##*/}:0.0.1


## Set your Akka Serverless project name
export AKKASLS_PROJECT=<your project>

## Deploy the services to your Akka Serverless project
akkasls services deploy $i $DOCKER_REGISTRY/$DOCKER_USER/${PWD##*/}:0.0.1 --project $AKKASLS_PROJECT

```

### Testing your service

To test your services, you'll first need to expose them on a public URL

```bash
## Set your Akka Serverless project name
export AKKASLS_PROJECT=<your project>

## Expose the services with a public HTTP endpoint
for i in orders users warehouse cart; do
  akkasls services expose $i --enable-cors --project $AKKASLS_PROJECT
done
```

From there, you can use the endpoints with the below cURL commands for each of the operations that the service exposes.

#### Cart

##### Add item to cart

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/cart/1/items/add \
  --header 'Content-Type: application/json' \
  --data '{
  "userId": "1",
  "productId": "turkey",
  "name": "delicious turkey",
  "quantity": 2
}'
```

##### Remove item from cart

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/cart/1/items/turkey/remove \
  --header 'Content-Type: application/json' \
  --data '{
  "userId": "1",
  "productId": "turkey"
}'
```

##### Get cart

```bash
curl --request GET \
  --url https://<your Akka Serverless endpoint>/carts/1 \
  --header 'Content-Type: application/json' \
  --data '{
  "userId": "1",
}'
```

#### Orders

##### Add Order

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/order/1 \
  --header 'Content-Type: application/json' \
  --data '{
  "userID": "1",
  "orderID": "4557",
  "items":[
   {
    "productID": "turkey",
     "quantity": 12,
    "price": 10.4
   }
  ]
}'
```

##### Get Order Details

```bash
curl --request GET \
  --url https://<your Akka Serverless endpoint>/order/1/4557 \
  --header 'Content-Type: application/json'
```

#### Users

##### New User

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/user/1 \
  --header 'Content-Type: application/json' \
  --data '{
  "id": "1",
  "name": "retgits",
  "emailAddress": "retgits@example.com",
  "orderID":[]
}'
```

##### Get User Details

```bash
curl --request GET \
  --url https://<your Akka Serverless endpoint>/user/1
```

##### Update User Orders

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/user/1/order \
  --header 'Content-Type: application/json' \
  --data '{
  "id": "1",
  "orderID": "1234"
}'
```

#### Warehouse

##### Receive Product

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/warehouse/5c61f497e5fdadefe84ff9b9 \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "5c61f497e5fdadefe84ff9b9",
    "name": "Yoga Mat",
    "description": "Limited Edition Mat",
    "imageURL": "/static/images/yogamat_square.jpg",
    "price": 62.5,
    "stock": 5,
    "tags": [
        "mat"
    ]
}'
```

##### Get Product Details

```bash
curl --request GET \
  --url https://<your Akka Serverless endpoint>/warehouse/5c61f497e5fdadefe84ff9b9
```

##### Update Stock

```bash
curl --request POST \
  --url https://<your Akka Serverless endpoint>/warehouse/5c61f497e5fdadefe84ff9b9/stock \
  --header 'Content-Type: application/json' \
  --data '{
    "id": "5c61f497e5fdadefe84ff9b9",
    "stock": 10
}'
```

### Testing your services locally

To test your services, you'll need to run the proxy on your own machine and use the containers you've built.

```bash
## Set your dockerhub username
export DOCKER_REGISTRY=docker.io
export DOCKER_USER=<your dockerhub username>
export SERVICE= ## this can be one of orders users warehouse cart

## Create a docker bridged network
docker network create -d bridge akkasls

## Run your userfunction
docker run -d --name userfunction --hostname userfunction --network akkasls $DOCKER_REGISTRY/$DOCKER_USER/$SERVICE:3.0.0

## Run the proxy
docker run -d --name proxy --network akkasls -p 9000:9000 --env USER_FUNCTION_HOST=userfunction gcr.io/akkaserverless-public/akkaserverless-proxy:latest -Dconfig.resource=dev-mode.conf -Dcloudstate.proxy.protocol-compatibility-check=false
```

To clean it all up, you can run

```bash
docker stop userfunction
docker rm userfunction
docker stop proxy
docker rm proxy
docker network rm akkasls
```

## Contributing

We welcome all contributions! [Pull requests](https://github.com/lightbend-labs/akkaserverless-ecommerce-javascript/pulls) are the preferred way to share your contributions. For major changes, please open [an issue](https://github.com/lightbend-labs/akkaserverless-ecommerce-javascript/issues) first to discuss what you would like to change.

## Support

This project is provided on an as-is basis and is not covered by the Lightbend Support policy.

## License

See the [LICENSE](./LICENSE).