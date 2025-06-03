from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

# Define the DAG
with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    schedule_interval='@daily',  # runs daily
    description='A simple hello world DAG with 3 tasks',
    tags=['example']
) as dag:

    def task_1():
        print("Task 1: Hello from task 1")

    def task_2():
        print("Task 2: Hello from task 2")

    def task_3():
        print("Task 3: Hello from task 3")

    t1 = PythonOperator(
        task_id='say_hello_1',
        python_callable=task_1
    )

    t2 = PythonOperator(
        task_id='say_hello_2',
        python_callable=task_2
    )

    t3 = PythonOperator(
        task_id='say_hello_3',
        python_callable=task_3
    )

    # Define task dependencies
    t1 >> t2 >> t3
