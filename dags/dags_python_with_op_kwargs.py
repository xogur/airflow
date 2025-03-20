from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random
from airflow.decorators import task
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *", # 크론 스케줄줄
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable=regist2,
        op_args=['xogur','man','kr','seoul'],
        op_kwargs={'email' : 'snsk656@naver.com', 'phone' : '010-9072-1938'}
    )

    regist2_t1