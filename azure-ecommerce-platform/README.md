# Azure E-Commerce Microservices Platform

## 1. Project Overview

An enterprise-style E-Commerce application deployed on
Microsoft Azure Kubernetes Service (AKS).

The project demonstrates practical implementation of
microservices, containerization, Kubernetes orchestration,
container registry integration and PostgreSQL deployment.

## 2. Architecture

Customer / Client
       |
       v
Product Service
       |
       v
Cart Service
       |
       v
Order Service
       |
       v
Payment Service

All services run as containers on Azure Kubernetes Service.

PostgreSQL runs separately inside the AKS cluster.

## 3. Technology Stack

- Microsoft Azure
- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Docker
- Kubernetes
- Python
- FastAPI
- PostgreSQL 16
- Linux / Ubuntu
- Azure CLI
- kubectl

## 4. Microservices

### Product Service
Provides product catalogue and product information.

### Cart Service
Manages shopping cart operations and retrieves product details.

### Order Service
Creates customer orders and communicates with Payment Service.

### Payment Service
Simulates payment processing for demonstration purposes.

## 5. Kubernetes Components

- Deployments
- Pods
- ClusterIP Services
- Namespaces
- Persistent Volume Claims
- Storage Classes
- Kubernetes Secrets

## 6. Database

PostgreSQL 16 is deployed inside AKS.

Database:
ecommerce

Database user:
ecommerce_user

Persistent storage:
10 GB PVC

Database credentials are referenced through Kubernetes Secrets.

## 7. Azure Infrastructure

Resource Group:
rg-ecommerce-aks

Region:
Central India

AKS Cluster:
aks-ecommerce-prod

ACR:
acrecommerceprod2026

Virtual Network:
vnet-ecommerce-prod

AKS Subnet:
10.10.2.0/23

## 8. Security

- Managed Identity for AKS
- ACR authentication through managed identity
- Kubernetes Secret for database credentials
- Separate Kubernetes namespace for database
- Private ClusterIP for internal database access

Note: Additional production security controls are required.

## 9. Project Limitations

- Payment processing is simulated.
- Cart, Order and Payment currently use in-memory storage.
- PostgreSQL is deployed but application persistence integration is pending.
- API Gateway and Ingress are not yet implemented.
- Production monitoring and distributed tracing are pending.

## 10. Future Enhancements

- Integrate PostgreSQL with Order and Payment services.
- Implement API Management or an ingress gateway.
- Implement Redis caching.
- Introduce asynchronous messaging using Azure Service Bus.
- Implement centralized monitoring.
- Implement CI/CD using Azure DevOps.
- Implement autoscaling and high availability.
- Integrate Azure Key Vault.

## 11. Project Objective

To demonstrate practical enterprise cloud architecture,
microservices deployment, Kubernetes administration,
security and DevOps implementation on Microsoft Azure.
