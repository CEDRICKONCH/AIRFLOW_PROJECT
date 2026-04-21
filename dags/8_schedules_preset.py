from airflow.sdk import dag, task
from pendulum import datetime

@dag( 
    dag_id="first_schedule_dag",
    start_date=datetime(year=2024, month=6, day=1, tz="America/Halifax"),
    schedule="@daily",
    catchup=False,
    is_paused_upon_creation=False
)
def first_schedule_dag():
    
    @task.python
    def first_task():
        print("This is the first task in the first DAG!")
        
    @task.python
    def second_task():
        print("This is the second task in the first DAG!")
        
    @task.python
    def third_task():
        print("This is the third task in the first DAG!")
        
    first = first_task()
    second = second_task()
    third = third_task()
        
    first >> second >> third

first_schedule_dag()