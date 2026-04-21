from airflow.sdk import dag, task

@dag( 
     dag_id="branch_dag",
)
def branch_dag():
    
    @task.python
    def extract_task(**kwargs):
        print("Extracting data...")
        ti = kwargs['ti']
        extracted_data_dict = {
            "api_extracted_data": [1, 2, 3],
            "db_extracted_data": [4, 5, 6],
            "s3_extracted_data": [7, 8, 9],
            "weekend_flag": "false"
        }
        
        ti.xcom_push(key='return_value', value=extracted_data_dict)
        
    @task.python
    def transform_task_api(**kwargs):
        print("Transforming API data...")
        ti = kwargs['ti']
        api_extracted_data = ti.xcom_pull(task_ids='extract_task', key='return_value')['api_extracted_data']
        print(f"API data before transformation: {api_extracted_data}")
        
        transformed_api_data = [x * 10 for x in api_extracted_data]
        ti.xcom_push(key='return_value', value=transformed_api_data)

    @task.python
    def transform_task_db(**kwargs):
        print("Transforming DB data...")
        ti = kwargs['ti']
        db_extracted_data = ti.xcom_pull(task_ids='extract_task', key='return_value')['db_extracted_data']
        print(f"DB data before transformation: {db_extracted_data}")
        
        transformed_db_data = [x * 100 for x in db_extracted_data]
        ti.xcom_push(key='return_value', value=transformed_db_data)
        
    @task.python
    def transform_task_s3(**kwargs):
        print("Transforming S3 data...")
        ti = kwargs['ti']
        s3_extracted_data = ti.xcom_pull(task_ids='extract_task', key='return_value')['s3_extracted_data']
        print(f"Transforming S3 data: {s3_extracted_data}.......")
        
        transformed_s3_data = [x * 1000 for x in s3_extracted_data]
        ti.xcom_push(key='return_value', value=transformed_s3_data)
        
    
    @task.branch
    def decider_task(**kwargs):
        ti = kwargs['ti']
        weekend_flag = ti.xcom_pull(task_ids='extract_task')['weekend_flag'] 
        if weekend_flag == "true":
            return 'no_load_task'
        else:
            return 'load_task'  
        

    @task.python
    def load_task(**kwargs):
        print("Loading transformed data to destination...")
        api_data = kwargs['ti'].xcom_pull(task_ids='transform_task_api')
        db_data = kwargs['ti'].xcom_pull(task_ids='transform_task_db')
        s3_data = kwargs['ti'].xcom_pull(task_ids='transform_task_s3')
        
        return f"echo 'Loaded data: {api_data},{db_data},{s3_data}'"
    
    
    @task.bash
    def no_load_task(**kwargs):
        print ("No load task executed since it's a weekend...")
        return "echo 'No load task executed...'"

    # Define task dependencies
    
    extract = extract_task()
    transform_api = transform_task_api()    
    transform_db = transform_task_db()
    transform_s3 = transform_task_s3()
    decider = decider_task()
    no_load = no_load_task()
    load = load_task()
    
    extract >> [transform_api, transform_db, transform_s3] >> decider >> [load, no_load]

# Instantiate the DAG
branch_dag()