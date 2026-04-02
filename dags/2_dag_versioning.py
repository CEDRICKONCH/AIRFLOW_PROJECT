from airflow.sdk import dag, task

@dag( 
     dag_id="versioned_dag1",
)
def versioned_dag():
    
    @task.python
    def first_task():
        print("This is the first task in the first DAG!")
        
    @task.python
    def second_task():
        print("This is the second task in the first DAG!")
        
    @task.python
    def third_task():
        print("This is the third task in the first DAG completed!")
        
    @task.python
    def version_task():
        print("This is the version task task, indicating the DAG version!")

        
    # Define task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    version = version_task()
        
    first >> second >> third >> version

# Instantiate the DAG
versioned_dag()