from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random
from airflow.decorators import task
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *", # 크론 스케줄줄
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    
) as dag:
    
    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable=regist,
        op_args=['xogur', 'man', 'kr', 'seoul']
    )


    regist_t1