# Laptop-Price-Calculator

## Overview

Laptop price prediction utilizes machine learning to forecast the price of a laptop based on its specifications such as brand, processor, RAM, storage, display, and other relevant features. This project involves data collection, preprocessing, feature engineering, model training, and evaluation to build a predictive model. The goal is to create a system that can accurately estimate laptop prices, helping both buyers and sellers make informed decisions. It can be beneficial to customers looking for the best deals and to businesses for pricing strategies. By leveraging data analysis and machine learning algorithms, this project aims to provide a valuable tool for navigating the laptop market.

## Project Summary

This project aims to develop a machine learning model for predicting laptop prices based on features like brand, CPU, screen size, RAM, graphics, and disk size. The project involves the following key steps:

**Virtual Environment with Docker:** A Docker image was created to encapsulate all the project dependencies, libraries, and configurations, ensuring consistent execution across different environments. This approach simplifies setup and eliminates potential compatibility issues.

**Data Collection and Preprocessing:** 
Data was collected, cleaned, and preprocessed to handle missing values, outliers, and inconsistencies. Numerical features (screen size, RAM, disk size) were transformed using the Yeo-Johnson method to make their distributions more Gaussian-like. Categorical features (brand, CPU model, graphics) were one-hot encoded for model compatibility.

**Exploratory Data Analysis (EDA):** EDA was conducted to gain insights into the data, identify relationships between variables, and inform feature engineering decisions. Correlation analysis, hypothesis testing (ANOVA and Pearson's), and visualizations like heatmaps and box plots were used. Also, **Evidently AI** were used for the data drift detection.

**Feature Engineering:** New features were created, and existing ones were transformed to improve model accuracy. For example, less frequent laptop brands were grouped into an 'other' category, and numerical features were scaled using PowerTransformer and StandardScaler to improve model performance.

**Model Selection and Training:** Various regression models were evaluated, including Decision Tree, Random Forest, Gradient Boosting, Linear Regression, XGBoost, CatBoost, AdaBoost, Ridge, Lasso, and KNN Regressor. CatBoost was identified as the best-performing model based on R2 score and other evaluation metrics.

**Hyperparameter Tuning:** RandomizedSearchCV was used to fine-tune the hyperparameters of the selected models (CatBoost, XGBoost, Gradient Boosting, Ridge, Lasso) to further enhance performance.

**Model Evaluation:** The final model's performance was assessed using metrics such as R2 score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE) on a held-out test set. Here, parameter tuning continued inside the modular coding with **MLFLOW** leading to identifying the best performing model (in this case, CatBoostRegressor) and retraining the model.

**Data Storage:** The cleaned dataset from notebook experiments was stored in a MongoDB database for persistence and potential future use. The final trained model was stored in an **AWS S3 bucket** for deployment. This enables efficient access and integration with other applications or services.

**CI/CD with GitHub Actions:** A CI/CD pipeline was implemented using **GitHub Actions** to automate the build, testing, and deployment processes. This ensures code quality, facilitates collaboration, and enables continuous integration of new features and updates.

**User Interface with Flask:** A user-friendly interface was developed using Flask to facilitate model interaction and prediction. This allows users to input laptop features and receive predicted prices.

The project successfully developed a robust and accurate laptop price prediction model. This model can be used by consumers to estimate laptop prices, make informed purchasing decisions, and potentially by businesses for pricing strategies.

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
conda create -n <environament_name> python=<version> -y
conda activate <environament_name>
conda deactivate
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

<!--- ![drift](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/main/flowchart/drift.png?raw=true) --->

drift_report : https://nikhil-xyz.github.io/Laptop-Price-Calculator/data_drift_report.html



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
Visit this url to compare all the experiment conducted during the evaluation by yourself.

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
### DVC command for pipeline execution and workflow display
```
# For pipeline execution
dvc repro

# For workflow display
dvc dag
```
### DVC Workflow
![dvc](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/main/flowchart/Screenshot%20(22).png)

## Evaluation
**Scatter Plot:** A scatter plot is a type of graph that uses dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. We are plotting to compare the actual output against the predicted outputs.

![scatter](https://github.com/nikhil-xyz/Laptop-Price-Calculator/blob/main/flowchart/scatter_plot.png?raw=true)


## AWS CI-CD Setup with Github Actions
1. Login to AWS Console
2. Create IAM user for deployment
3. Create ECR repo to store/save docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
### Commands
**Optional**
```
sudo apt-get update -y

sudo apt-get upgrade
```

**Required**
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```
```
sudo usermod -aG docker ubuntu
```
```
newgrp docker
```
6. Configure EC2 as self-hosted runner
7. Setup github secrets

## Training Link:
```
http://13.48.44.119:8080/train
```
## Production Link:
```
http://13.48.44.119:8080
```



<!-- ecr : 423895530294.dkr.ecr.eu-north-1.amazonaws.com/laptop -->
