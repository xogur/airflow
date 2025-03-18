from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *", # 크론 스케줄줄
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to='snsk656@naver.com',
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다'
    )