from airflow.sdk import dag, task
from pendulum import datetime, duration, timezone   
from airflow.timetables.trigger import CronTriggerTimetable, DeltaTriggerTimetable

@dag(
    schedule=CronTriggerTimetable("@daily", timezone="America/Halifax"), # This cron expression means the DAG will run once a day at midnight.
    start_date=datetime(year=2026, month=1, day=26, tz="America/Halifax"),
    end_date=datetime(year=2026, month=4, day=30, tz="America/Halifax"),
    catchup=True,
)

def incremental_load_dag():
    
    @task.python
    def incremental_data_fetch(**kwargs):
        date_interval_start = kwargs['data_interval_start']
        date_interval_end = kwargs ['data_interval_end']
        print(f"Fetching incremental data from {date_interval_start} to {date_interval_end}")
        
    
    @task.bash
    def process_incremental_data():
        return "echo 'Processing incremental data from {{ data_interval_start }} to {{ data_interval_end }}'"
    
    
    fetch_task = incremental_data_fetch()
    process_task = process_incremental_data()
    fetch_task >> process_task
    
    #Instantiating the DAG
incremental_load_dag()
