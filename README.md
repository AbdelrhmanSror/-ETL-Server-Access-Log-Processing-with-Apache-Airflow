#### Project Description
This project demonstrates an ETL (Extract, Transform, Load) pipeline for processing server access logs using Apache Airflow. The pipeline consists of multiple tasks that download, extract, transform, and load data, along with a final check step to ensure the integrity of the processed data. The data is processed from a web server access log file hosted online, and the pipeline is scheduled to run daily.

#### Requirements
```txt
requests
apache-airflow
```

#### How to Run

1. **Create a Virtual Environment:**

   ```sh
   python3 -m venv myenv
   ```

2. **Activate the Virtual Environment:**

   - On Linux/macOS:
     ```sh
     source myenv/bin/activate
     ```
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Start Airflow:**
   Follow the [Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html) to set up and start the Airflow web server and scheduler.

5. **Place the DAG file:**
   Copy `ETL_Server_Access_Log_Processing.py` to your Airflow `dags` directory using the following command:

   ```sh
   cp ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags
   ```

   where `$AIRFLOW_HOME` is the path to the Airflow directory on your machine.

6. **Trigger the DAG:**
   In the Airflow web interface, locate the `ETL_Server_Access_Log` DAG and trigger it manually or wait for the scheduled interval.

#### Author
Abdelrahman Sror - [abdelrahmanasror@gmail.com](mailto:abdelrahmanasror@gmail.com)

Feel free to reach out if you have any questions or need further assistance!
