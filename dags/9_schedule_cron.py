from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag( 
    dag_id="cron_schedule_dag",
    start_date=datetime(year=2026, month=1, day=26, tz="America/Halifax"),
    schedule=CronTriggerTimetable(cron="0 16 * * MON-FRI", timezone="America/Halifax"), # This cron expression means the DAG will run at 4:00 PM every weekday (Monday to Friday).
    end_date=datetime(year=2026, month=4, day=30, tz="America/Halifax"),
    catchup=False,
    is_paused_upon_creation=False
)
def cron_schedule_dag():
    
    @task.python
    def first_task():
        print("This is the first task in the cron schedule DAG!")
        
    @task.python
    def second_task():
        print("This is the second task in the cron schedule DAG!")
        
    @task.python
    def third_task():
        print("This is the third task in the cron schedule DAG!")
        
    first = first_task()
    second = second_task()
    third = third_task()
        
    first >> second >> third

cron_schedule_dag()