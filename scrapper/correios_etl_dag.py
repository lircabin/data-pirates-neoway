#datetime
from datetime import datetime
from datetime import timedelta

from dag_helpers.extract import extract

from dag_helpers.create import create
from dag_helpers.load import load
from dag_helpers.transform import transform
# The DAG object
from airflow import DAG

# Operators
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# initializing the default arguments
default_args = {
    'owner': 'Matheus Alves',
    'start_date': datetime(2021, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# Instantiate a DAG object
correios_etl = DAG(
    'correios_etl',
    default_args=default_args,
    description=
    'ETL to fetch data about Brazilian Cities in Correio\'s website',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

extract_task = PythonOperator(task_id='extract_task',
                              python_callable=extract,
                              dag=correios_etl)

transform_task = PythonOperator(task_id='transform_task',
                                python_callable=transform,
                                dag=correios_etl)

create_task = PythonOperator(task_id='create_task',
                             python_callable=create,
                             dag=correios_etl)

load_task = PythonOperator(task_id='load_task',
                           python_callable=load,
                           dag=correios_etl)

extract_task >> transform_task >> create_task >> load_task