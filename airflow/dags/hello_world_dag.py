import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def hello_world():
    return "Hola Mundo"

# Función para imprimir el valor devuelto por la tarea anterior
def print_hello_world(**context):
    value = context['task_instance'].xcom_pull(task_ids='hello_world_task')
    # Print value with DEBUG log level
    logging.info("Valor devuelto por la tarea anterior: %s", value)

# Definición del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Un simple DAG que devuelve Hola Mundo',
    schedule_interval=timedelta(days=1),
)

# Definición de las tareas
hello_world_task = PythonOperator(
    task_id='hello_world_task',
    python_callable=hello_world,
    dag=dag,
)

print_task = PythonOperator(
    task_id='print_task',
    python_callable=print_hello_world,
    provide_context=True,
    dag=dag,
)

# Configurar el orden de las tareas
hello_world_task >> print_task