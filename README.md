# Criação de Pipeline de dados com Apache Airflow e PostgreSQL

``` python
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
 
### Agendador de movimentação dos dados:
### Uma vez por dia à meia-noite  0 0 * * *
 
with DAG('dag_pipeline',
    start_date = datetime(2022, 11, 10),
    schedule_interval='0 0 * * *',
    template_searchpath = '/opt/airflow/sql') as dag:
    
#### Extrair dados: solicitar dataset mais recente arquivo parquet
    parquet_file = 'https://storage.googleapis.com/challenge_junior/categoria.parquet' 
    df = pd.read_parquet(parquet_file)

#### Transformar dados: converter arquivo parquet em csv (tentar gravar Local)
    csv_output = 'Users\vckon\bixairflow-docker\airflow-docker\categoria.csv'
    df.to_csv(csv_output, index=False, sep='\t')
    print (df)

#### Carregar dados: conexão com o Postgres
    with open('Users\vckon\bixairflow-docker\airflow-docker\categoria.csv','r') as file:
        next(file)
        for row in file:
            file.write(row)
    
    postgres_hook = PostgresHook(postgres_conn_id="postgres_airflow")
    conn = postgres_hook.get_conn()
    cur = conn.cursor()
    with open('Users\vckon\bixairflow-docker\airflow-docker\categoria.csv','r') as file:
        cur.copy_from(
            f,
            "categoria",
            columns=[
                "nome_categoria",
            ],
            sep="\t",
        )
    conn.commit()

#### Extrair dados: solicitar dataset mais recente API
    def get_funcionario():
        url = 'https://us-central1-bix-tecnologia-prd.cloudfunctions.net/api_challenge_junior'
        params = {"id":"1"}
        r = requests.get(url, params)
        data = r.text
    #print(data)
    #output: Rob Carsson
    #print(type(data)) 
    #output: <class 'str'>

#### Transformar dados: converter a string em um object/ Python dictionary
    data_string = '''{"funcionario": [{"nome": "Rob Carsson"},{"nome": "Eli Preston"},{"nome": "Tom Lindwall"},{"nome": "Leif Shine"},{"nome": "Ingrid Hendrix"},{"nome": "Lennart Skoglund"},{"nome": "Rock Rollmann"},{"nome": "Helen Brolin"},{"nome": "Joan Callins"}]}'''
    dictionary = json.loads(data_string)
    #print(type(dictionary))
    #output: <class 'dict'>
    # Acessando o dicionário
    for funcionario in dictionary["funcionario"]:
        print(funcionario["nome"])
 
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
```

# Criação das tabelas e inserção de dados em SQL

``` python
### criar TB_Categoria
 
create table if not exists TB_Categoria (
                id INT generated by default as identity,
                name VARCHAR NOT NULL,
                dt date
            )
 
### criar TB_Funcionario
create table if not exists TB_Funcionario (
                id INT generated by default as identity,
                name VARCHAR NOT NULL,
                dt date
            )
 
### inserir dados TB_Categoria
insert into TB_Categoria (name, dt)
            values('Childrens wear', current_date)
 
### inserir dados TB_Funcionario
insert into TB_Funcionario (name, dt)
            values('Joan Callins', current_date)
```
