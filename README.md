# DEInfraLocal
## Objective
- Build an end to end example for data and machine learning workflow
- Different components can also be used to building local testing infrastructure
    - This is especially important for lot of Data workflows for quick development and testing using local tests and CI/CD
    - This saves overhead cost of spinning up a cluster in infrastructure to test basic implementation


## Components
- We ll divide the infrastructure into 3 components:
    - Backend (backend)
    - Offline Data Processing (offline_infra)
        - Batch
        - Realtime
    - MLOps (ml_ops)

## Tools (TBD)
- Kafka
- Minio (S3 interface)
- Spark (ETL Process)
- Airflow (Workflow Orchestrator)
- Label Studio (Annotator)
- Mlflow / W&B (Model Registry)

## Docker
You ll need a local docker daemon to initiate the different tooling. I am using Rancher desktop but there is also docker desktop available. 
- Info on Rancher Desktop: https://rancherdesktop.io

## Minio
We ll leverage Minio which provides us with api similar to aws s3 and added benefit it provides UI to nivaigate through objects
- Credentials are default: 
    - username: `minioadmin`
    - password: `minioadmin`
- UI access: localhost:9001
    Ref Link: https://min.io


## Running local container
- To spin up the service:
    - docker compose up -d
- To shut down the service
    - docker compose down