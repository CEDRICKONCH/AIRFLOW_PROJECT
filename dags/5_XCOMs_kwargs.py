from airflow.sdk import dag, task

@dag( 
        dag_id="xcoms_dag_kwargs",
)
def xcoms_dag_kwargs():
    
    @task.python
    def first_task(**kwargs):
        
        # Extracting 'ti' from kwargs to push data to XComs
        ti = kwargs['ti']   
        
        print("Extracting data ...This is the first task in the first DAG!")
        fectched_data = {"data": [1, 2, 3, 4, 5]}
        ti.xcom_push(key='return_result', value=fectched_data)
       
        
    @task.python
    def second_task(**kwargs):
        
        ti= kwargs['ti']
        
        # Pulling xcoms data from the first task using 'ti'
        
        fectched_data = ti.xcom_pull(task_ids='first_task', key='return_result')['data']
        print("Transforming data ...This is the second task in the first DAG!")
        
        transformed_data = fectched_data*2
        transformed_data_dict = {"transf_data": transformed_data}
        
        ti.xcom_push(key='return_result', value=transformed_data_dict)
        
    @task.python
    def third_task(**kwargs):
        ti = kwargs['ti']
        load_data = ti.xcom_pull(task_ids='second_task', key='return_result')
        return load_data
        
        
    # Define task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    
    first >> second >> third
        

# Instantiate the DAG
xcoms_dag_kwargs()
