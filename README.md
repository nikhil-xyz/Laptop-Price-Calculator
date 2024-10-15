# Laptop-Price-Calculator

import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='Laptop-Price-Calculator', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


uri = 'https://dagshub.com/nikhil.sonkusare94/Laptop-Price-Calculator'

ecr : 423895530294.dkr.ecr.eu-north-1.amazonaws.com/laptop