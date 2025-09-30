import requests
from opsrampcli.DataSource import DataSource
import pandas as pd
from datetime import datetime
import pytz
import os
import logging
import json

logger = logging.getLogger(__name__)


class ServiceNowDataSource(DataSource):
    SERVICENOW_DISPLAY_VALUE = 'display_value'

    class SnowDataSourceException(DataSource.DataSourceException):
        pass

    def get_resources_df(self):
        job = self.job
        instance_url = os.getenv("SERVICENOW_URL") or job['source']['servicenow']['instance_url']
        url = instance_url + f"/api/now/table/{job['source']['servicenow']['table']}"

        qstrings = {}
        for k, v in job['source']['servicenow']['query_parameters'].items():
            qstrings[f'sysparm_{k}'] = v

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        user = os.getenv("SERVICENOW_USER") or job['source']['servicenow']['auth']['username']
        password = os.getenv("SERVICENOW_PASSWORD") or job['source']['servicenow']['auth']['password']

        auth_type = os.getenv("SERVICENOW_AUTH_TYPE") or job['source']['servicenow']['auth']['type']
        if auth_type == 'oauth2':
            logger.info("Using oauth2 authentication")
            client_id = os.getenv("SERVICENOW_CLIENT_ID") or job['source']['servicenow']['auth']['client_id']
            client_secret = os.getenv("SERVICENOW_CLIENT_SECRET") or job['source']['servicenow']['auth']['client_secret']
            oauth_payload = {
                "grant_type": "password",
                "client_id": client_id,
                "client_secret": client_secret,
                "username": user,
                "password": password
            }
            oauth_get_token_headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            logger.info("Getting oauth2 token")
            oauth_response = requests.post(f"{instance_url}/oauth_token.do", headers=oauth_get_token_headers, data=oauth_payload)
            oauth_response.raise_for_status()
            token = json.loads(oauth_response.content)["access_token"]
            logger.info("Got oauth2 token")
            headers["Authorization"] = f"Bearer {token}"
            logger.info("Executing query")
            response = requests.get(url=url, params=qstrings, headers=headers)
        else:
            logger.info("Using basic authentication")
            auth = requests.auth.HTTPBasicAuth(user, password)
            logger.info("Executing query")
            response = requests.get(url=url, auth=auth, params=qstrings, headers=headers)

        response.raise_for_status()
        try:
            responsedict = response.json()
        except Exception as e:
            msg = f'Failed to retrieve records from ServiceNow datasource: {e}, {response.text}'
            raise ServiceNowDataSource.SnowDataSourceException(msg)
        records = responsedict.get('result', [])
        processed_recs = []
        for record in records:
            newrec = {}
            for key,value in record.items():
                if isinstance(value, dict) and ServiceNowDataSource.SERVICENOW_DISPLAY_VALUE in value:
                    newrec[key] = value[ServiceNowDataSource.SERVICENOW_DISPLAY_VALUE]
                else:
                    newrec[key] = value
            processed_recs.append(newrec)

        self.df = pd.DataFrame(processed_recs)

