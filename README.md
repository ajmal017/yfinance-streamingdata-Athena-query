# YahooFinance-streamingdata-Athena-Query
In this project, streaming data (near real time)from **Yahoo  Finance** is collected and transformed by provisioning two Lambda functions for downstream processing and interactive querying.
## Data Collector
A lambda function is created to collect data using the [yfinance](https://pypi.org/project/yfinance/) module. Below is a screenshot of the configuration page of the function. And the code is contained in a file named **data_collector.py**. To access the function URL by clicking [data_collector_URL](https://oisp8znm2c.execute-api.us-east-2.amazonaws.com/default/yf-DataCollector)


![image](https://user-images.githubusercontent.com/57573785/82766813-1946be80-9df0-11ea-9cae-b1cc8af6e625.png)

## Data Transformer
In this part of project, a AWS **Kinesis Firehose Delivery Stream** service is configured to have a lambda function called *DataTransformer* that transforms and places data into S3.


![image](https://user-images.githubusercontent.com/57573785/82766764-9b82b300-9def-11ea-936a-437cecfdbeb9.png)

## Athena Query
Here, **AWS Glue** service is set to direct **AWS Athena** to the S3 bucket where the finance data is stored for the subsequent interative querying. Here, a query for obtaining hourly 'High' stock price per company is conducted.



