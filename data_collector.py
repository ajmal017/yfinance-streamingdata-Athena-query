import boto3
import os
import subprocess
import sys
import json


subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')

import yfinance as yf
def lambda_handler(event, context):

    Sdate = '2020-05-14'
    Edate = '2020-05-15'
    T_interval = '1m'
    CompName= ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    
    for n in range(len(CompName)):
        records = yf.download(CompName[n], start = Sdate, end = Edate, interval = T_interval)
        data = []
        
        for i in range(len(records)):
            output = {"High":records['High'][i],
                        "Low":records['Low'][i],
                        "ts":records.index[i].strftime('%Y-%-m-%d %X'),
                        "Name":CompName[n]}
            
            jsonstr_data = json.dumps(output)
            
            fh = boto3.client("firehose", "us-east-2")
            
            fh.put_record(
                DeliveryStreamName="yfinance-streamdata", 
                Record = {'Data': jsonstr_data.encode('utf-8')})
            data.append(output)
        
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {jsonstr_data}')
    }