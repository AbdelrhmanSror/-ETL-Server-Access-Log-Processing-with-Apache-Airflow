import requests
# Import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.python import PythonOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'
downloaded_file = 'web-server-access-log.txt'
extracted_file = 'extracted.txt'
transformed_file = 'transformed.txt'
output_file = 'capitalized.txt'

def download():
    global url
    global downloaded_file
    print("Inside download")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(downloaded_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def extract():
    global downloaded_file
    print("Inside Extract")
    # Read the contents of the file into a string
    with open(downloaded_file, 'r') as infile, \
            open(extracted_file, 'w') as outfile:
        for line in infile:
            fields = line.split('#')
            if len(fields) >= 4:
                timestamp = fields[0]
                visitor_id = fields[3]
                outfile.write(timestamp + "#" + visitor_id + "\n")

def transform():
    global extracted_file, transformed_file
    print("Inside Transform")
    with open(extracted_file, 'r') as infile, \
            open(transformed_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.replace('#',',').upper())

def load():
    global transformed_file, output_file
    print("Inside Load")
    # Save the array to a CSV file
    with open(transformed_file, 'r') as infile, \
            open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line)

def check():
    global output_file
    print("Inside Check")
    # Save the array to a CSV file
    with open(output_file, 'r') as infile:
        for line in infile:
            print(line)

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Sror',
    'start_date': days_ago(0),
    'email': ['abdelrahmanasror@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ETL_Server_Access_Log',
    default_args=default_args,
    description='ETL_Server_Access_Log',
    schedule_interval=timedelta(days=1),
)
# Define the task named execute_download to call the `download` function
execute_download = PythonOperator(
    task_id='download',
    python_callable=download,
    dag=dag,
)
# Define the task named execute_extract to call the `extract` function
execute_extract = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)
# Define the task named execute_transform to call the `transform` function
execute_transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

# Define the task named execute_load to call the `load` function
execute_load = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

# Define the task named execute_load to call the `check` function
execute_check = PythonOperator(
    task_id='check',
    python_callable=check,
    dag=dag,
)

# Task pipeline
execute_download >> execute_extract >> execute_transform >> execute_load >> execute_check