## Operationalizing a Coworking Space Microservice

### Overview

The Coworking Space Service is a set of APIs that enables users to request one-time tokens and administrators to authorize access to a coworking space. This service follows a microservice pattern and the APIs are split into distinct services that can be deployed and managed independently of one another.

### Setup

Not: you must hast the following ready to be able to properly configure coworking space

- Kubernetes cluster should created.
- `kubectl` installed and configured to interact with your cluster.
- install Helm for installing charts
- `docker` installed and configured for maybe local testing befor deployment

### 1. Configure a Database

- Install Bitnami Helm Repository:
  ```bash
  helm repo add bitnami https://charts.bitnami.com/bitnami
  helm repo update
  ```
- Install the PostgreSQL Chart:
  ```bash
  helm install my-postgres bitnami/postgresql
  ```
- Verify the Installation:
  ```bash
  helm list
  kubectl get pods
  ```
- To test database connection
  ```bash
  kubectl port-forward --namespace default svc/<SERVICE_NAME>-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432
  ```

### 2. Setup git repository and connect your aws codebuild via webhook to watch for changes:

Codebuild will be responsible for building and pushing your image to the aws ECR

### 3. Kubernetes Service and Deployment

On the root folder you find a folder called deployment. Here you see configuration for our container deployment, service and database configuration.

To create deployment and service run the following command:

- List deployment
  ```bash
  kubectl get deployments
  ```
- Create deployment

  ```bash
  kubectl apply -f deployment/
  ```

- Verify deployment pods
  ```bash
  kubectl get pods
  ```
- Verify deployment svc
  ```bash
   kubectl get svc
  ```
