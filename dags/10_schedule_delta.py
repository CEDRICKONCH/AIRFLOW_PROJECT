from airflow.sdk import dag, task
from pendulum import datetime, duration, timezone
from airflow.timetables.trigger import CronTriggerTimetable, DeltaTriggerTimetable

@dag( 
    dag_id="delta_schedule_dag",
    start_date=datetime(year=2026, month=1, day=26, tz="America/Halifax"),
    schedule=DeltaTriggerTimetable(duration(days=3)), # this schedule means the DAG will run every 3 days starting from the start_date.
    end_date=datetime(year=2026, month=4, day=30, tz="America/Halifax"),
    catchup=False,
    is_paused_upon_creation=False
)
def delta_schedule_dag():
    
    @task.python
    def first_task():
        print("This is the first task in the delta schedule DAG!")
        
    @task.python
    def second_task():
        print("This is the second task in the delta schedule DAG!")
        
    @task.python
    def third_task():
        print("This is the third task in the delta schedule DAG!")
        
    first = first_task()
    second = second_task()
    third = third_task()
        
    first >> second >> third

delta_schedule_dag()