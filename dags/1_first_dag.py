from airflow.sdk import dag, task

@dag( 
     dag_id="first_dag1",
)
def first_dag1():
    
    @task.python
    def first_task():
        print("This is the first task in the first DAG!")
        
    @task.python
    def second_task():
        print("This is the second task in the first DAG!")
        
    @task.python
    def third_task():
        print("This is the third task in the first DAG!")
        
    # Define task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
        
    first >> second >> third

# Instantiate the DAG
first_dag1()
    