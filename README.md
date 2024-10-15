# Laptop-Price-Calculator

## Tools
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
- Data link: https://raw.githubusercontent.com/nikhil-xyz/datasets/refs/heads/main/laptop_uncleaned.csv


## Git Commands
git add .

git commit -m "message"

git push origin main





import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='Laptop-Price-Calculator', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


uri = 'https://dagshub.com/nikhil.sonkusare94/Laptop-Price-Calculator'

ecr : 423895530294.dkr.ecr.eu-north-1.amazonaws.com/laptop