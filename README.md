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
akkasls services deploy ${PWD##*/} $DOCKER_REGISTRY/$DOCKER_USER/${PWD##*/}:0.0.1 --project $AKKASLS_PROJECT

```

### Testing your service

To test your services, you'll first need to expose them on a public URL

```bash
## Set your Akka Serverless project name
export AKKASLS_PROJECT=<your project>

## Expose the services with a public HTTP endpoint
akkasls services expose ${PWD##*/} --enable-cors --project $AKKASLS_PROJECT
```


## Contributing

We welcome all contributions! [Pull requests](https://github.com/jpollock/akka-serverless-starter-python/pulls) are the preferred way to share your contributions. For major changes, please open [an issue](https://github.com/jpollock/akka-serverless-starter-python/issues) first to discuss what you would like to change.

## Support

This project is provided on an as-is basis and is not covered by the Lightbend Support policy.

## License

See the [LICENSE](./LICENSE).