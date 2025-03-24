from airflow.models.baseoperator import BaseOperator
from airflow.hooks.base import BaseHook
import pandas as pd

class SeoulApiToCsvOperator(BaseOperator) :
    template_fields = ('endpoint', 'path', 'file_name', 'base_dt')

    def __init__(self, dataset_nm, path, file_name, base_dt=None, **kwargs) :
        super().__init__(**kwargs)
        self.http_conn_id = 'openapi.seoul.go.kr'
        self.path = path
        self.file_name = file_name
        self.endpoint = '{{var.value.api_key_openapi_seoul_go_kr}}/json/' + dataset_nm
        self.base_dt = base_dt

    def execute(self, context):
        import os
        connection = BaseHook.get_connection(self.http_conn_id)
        self.base_url = f'http://{connection.host}:{connection.port}/{self.endpoint}'

        total_row_df = pd.DataFrame()
        start_row = 1
        end_row = 1000

        while True:
            self.log.info(f'시작:{start_row}')
            self.log.info(f'끝:{end_row}')
            row_df = self._call_api(self.base_url, start_row, end_row)
            total_row_df = pd.concat([total_row_df, row_df])

            if len(row_df) < 1000:
                break
            else:
                start_row = end_row + 1
                end_row += 1000




    def _call_api(self, base_url, start_now, end_now) :
        import requests
        import json

        headers = {
            'Content-Type' : 'application/json',
            'charset' : 'utf-8',
            'Accept' : '*/*'
        }

        requests_url = f'{base_url}/{start_now}/{end_now}/'
        if self.base_dt is not None :
            requests_url = f'{base_url}/{start_now}/{end_now}/{self.base_dt}'
        response = requests.get(requests_url, headers)
        contents = json.loads(response.text)

        key_nm = list(contents.keys())[0]
        row_data = contents.get(key_nm).get('row')
        row_df = pd.DataFrame(row_data)

        return row_df