from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *", # 크론 스케줄줄
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=True,
    
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs) :
        from pprint import pprint
        pprint(kwargs)

    show_templates()