from airflow.sdk import dag, task

@dag( 
        dag_id="xcoms_dag_auto",
)
def xcoms_dag_auto():
    
    @task.python
    def first_task():
        print("Extracting data ...This is the first task in the first DAG!")
        fectched_data = {"data": [1, 2, 3, 4, 5]}
        return fectched_data
        
    @task.python
    def second_task(data: dict):
        fectched_data = data['data']
        transformed_data = fectched_data*2
        transformed_data_dict = {"transf_data": transformed_data}
        return transformed_data_dict
        
    @task.python
    def third_task(data: dict):
        load_data = data
        return load_data
        
        
    # Define task dependencies
    first = first_task()
    second = second_task(first)
    third = third_task(second)
        

# Instantiate the DAG
xcoms_dag_auto()