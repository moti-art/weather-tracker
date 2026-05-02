# 📊 Weather Tracker (Data Persistence Service)

[![CI for Weather Tracker](https://github.com/moti-art/weather-tracker/actions/workflows/ci.yaml/badge.svg)](https://github.com/moti-art/weather-tracker/actions)

The **Weather Tracker** is a specialized microservice designed to handle data ingestion and persistence. It monitors weather data and stores historical records in a NoSQL database.

## 🚀 Features
* **AWS Integration:** Native integration with **Amazon DynamoDB** for scalable data storage.
* **Asynchronous Processing:** Designed to run as a background worker.
* **Automated Life-cycle:** Fully integrated into the GitOps ecosystem.

## 🛠️ Tech Stack
* **Language:** Python
* **AWS SDK:** Boto3 (DynamoDB client)
* **Database:** AWS DynamoDB
* **Orchestration:** Kubernetes
* **Deployment:** ArgoCD & Helm

## ☁️ AWS Configuration
The service relies on AWS IAM roles or environment credentials to access DynamoDB. 
* **Table Name:** `weather_history` (Managed via Terraform in `weather-infra`).
* **Region:** `us-east-1` (Default).

## 🔄 GitOps Pipeline
1. **Push:** Code is pushed to `main`.
2. **CI:** GitHub Actions builds a Docker image and pushes it to Docker Hub.
3. **Sync:** The pipeline updates the `weather-gitops` repository with the new Image SHA.
4. **Deploy:** ArgoCD synchronizes the cluster state.

---
*Maintained by [Moti Levi](https://github.com/moti-art)*