# Importar  bibliotecas Apache Airflow
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
# Importar bibliotecas Python
from datetime import datetime, timedelta
import requests
import pandas as pd
import csv
import json
 
### Agendador de movimentação dos dados:
### Uma vez por dia à meia-noite  0 0 * * *
 
with DAG('dag_pipeline',
    start_date = datetime(2022, 11, 10),
    schedule_interval='0 0 * * *',
    template_searchpath = '/opt/airflow/sql') as dag:
  
  task1 = PostgresOperator(
        task_id='criar_tabela_postgres',
        postgres_conn_id='postgres_airflow',
        sql='criar_tabela_postgres.sql'
       
    )
 
    task2 = PostgresOperator(
        task_id='criar_tabela_categoria',
        postgres_conn_id='postgres_airflow',
        sql='criar_tabela_categoria.sql'
       
    )
 
    task3 = PostgresOperator(
        task_id='inserir_dados_postgres',
        postgres_conn_id='postgres_airflow',
        sql='inserir_dados_postgres.sql'
    )
 
    task4 = PostgresOperator(
        task_id='inserir_dados_categoria',
        postgres_conn_id='postgres_airflow',
        sql='inserir_dados_categoria.sql'
    )
 
task1 >> task2 >> task3 >> task4
