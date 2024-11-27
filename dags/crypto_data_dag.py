from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def fetch_data_task():
    subprocess.run(["python", "scripts/fetch_data.py"])

def preprocess_data_task():
    subprocess.run(["python", "scripts/preprocess_data.py"])

def train_model_task():
    subprocess.run(["python", "scripts/train_model.py"])

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2024, 11, 26),
}

dag = DAG('crypto_data_pipeline', default_args=default_args, schedule_interval='@daily')

fetch_data = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data_task,
    dag=dag
)

preprocess_data = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data_task,
    dag=dag
)

train_model = PythonOperator(
    task_id='train_model',
    python_callable=train_model_task,
    dag=dag
)

fetch_data >> preprocess_data >> train_model
