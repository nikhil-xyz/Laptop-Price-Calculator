# Laptop-Price-Calculator

## Overview

Laptop price prediction utilizes machine learning to forecast the price of a laptop based on its specifications such as brand, processor, RAM, storage, display, and other relevant features. This project involves data collection, preprocessing, feature engineering, model training, and evaluation to build a predictive model. The goal is to create a system that can accurately estimate laptop prices, helping both buyers and sellers make informed decisions. It can be beneficial to customers looking for the best deals and to businesses for pricing strategies. By leveraging data analysis and machine learning algorithms, this project aims to provide a valuable tool for navigating the laptop market.

## Tools
![tools](flowchart/logos.png)

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- Evidently: https://www.evidentlyai.com/
- DVC : https://dvc.org/
- MlFlow : https://mlflow.org/ 
- Dagshub : https://dagshub.com/
- Whimsical : https://whimsical.com/
- MongoDB: https://account.mongodb.com/account/login
- AWS: https://aws.amazon.com
- Data link: https://raw.githubusercontent.com/nikhil-xyz/datasets/refs/heads/main/laptop_uncleaned.csv

## Project Flowchart
![project flowchart](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/834f24effdce2036247e0a3c177ba758f2f8fe55/flowchart/project_flowchart.png)


## Git Commands
```
git add .

git commit -m "message"

git push origin main
```

## Conda environment commands
```
conda create -n visa python=3.8 -y

conda activate visa

pip install -r requirements.txt
```

## Environment Variables
```
export MONGODB_URI="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```

## MongoDB for Data Storage and Retrieval
MongoDB is a NoSQL, document-oriented database. It stores data in flexible, JSON-like documents called BSON, making it suitable for handling data that doesn't fit well into traditional rows and columns.
### Connection Syntax
```
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv('MONGODB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```
### Data Storage Syntax
```
data_base = client[DB_NAME]
collection = data_base[COLLECTION_NAME]

rec = collection.insert_many(data)
```
### Data Retrieval Syntax
```
records = collection.find()
```

## Evidently
Evidently AI is an open-source Python library used for machine learning model monitoring and data drift detection. It helps to analyze and understand the behavior of machine learning models. It provides interactive reports and dashboards to visualize data and model metrics, such as data drift, model performance, and feature importance. It also allows you to create test suites to check data and model quality, and it can be integrated into ML pipelines.

![drift]([flowchart\drift.png](https://raw.githubusercontent.com/nikhil-xyz/Laptop-Price-Calculator/refs/heads/main/data_drift_report.html))



## Dagshub
DagsHub is a platform built for data scientists and machine learning engineers to build, manage, and collaborate on machine learning projects. It provides a central hub to version data, track experiments, and share findings, streamlining the development process.
### Syntax
```
import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='Laptop-Price-Calculator', mlflow=True)
```

## MLFLOW
MLflow Experiment Tracking allows you to record and compare different runs of your machine learning experiments. It helps you keep track of parameters, metrics, and artifacts associated with each experiment run, facilitating model comparison, analysis, and selection. By providing a centralized repository for experiment data, MLflow helps data scientists and engineers understand model behavior, reproduce experiments, and collaborate more effectively.
### Syntax
```
import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```

## Experiment Tracking 
![mlflow](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/main/flowchart/mlflow_laptop.png?raw=true)

### mlflow URI
project_mlflow_uri = https://dagshub.com/nikhil.sonkusare94/Laptop-Price-Calculator

## DVC Tracking
DVC (Data Version Control) pipelines are a series of data processing stages that produce a final result, such as a trained machine learning model. DVC pipelines are defined in a dvc.yaml file using a YAML-based syntax. Each stage in the pipeline is defined as a separate entry with properties like cmd, deps, outs, etc.
### Syntax 
```
stages:  
<stage_name>:
    cmd: <command_to_run>
    deps:
      - <dependency_file_or_directory>
      - <another_dependency>
    outs:
      - <output_file_or_directory>
      - <another_output>    
    params:
      - <params_file.yaml:param_name>
      - <another_param_file:another_param>
    metrics:     
      - <metrics_file.json:metric_name>
      - <another_metrics_file:another_metric>
```
### DVC command for pipeline execution
```
dvc repro
```

## Evaluation
![scatter](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/main/flowchart/scatter_plot.png?raw=true)


## AWS CI-CD Setup with Github Actions
1. Login to AWS Console
2. Create IAM user for deployment
3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
### Commands
```
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
6. Configure EC2 as self-hosted runner
7. Setup github secrets


## Training Link:
```
http://16.170.247.15:8080/train
```
## Production Link:
```
http://16.170.247.15:8080
```



<!-- ecr : 423895530294.dkr.ecr.eu-north-1.amazonaws.com/laptop -->
