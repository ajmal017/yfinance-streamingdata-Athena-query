# YahooFinance-streamingdata-Athena-Query
In this project, streaming data (near real time)from **Yahoo  Finance** is collected and transformed by provisioning two Lambda functions for downstream processing and interactive querying.
## Data Collector
A lambda function is created to collect data using the [yfinance](https://pypi.org/project/yfinance/) module. Below is a screenshot of the configuration page of the function. And the code is contained in a file named **data_collector.py**.
![image](https://user-images.githubusercontent.com/57573785/82746496-611d0580-9d5e-11ea-97a3-000896b5d060.png)



