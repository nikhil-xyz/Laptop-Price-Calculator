# Laptop-Price-Calculator

import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='Laptop-Price-Calculator', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)