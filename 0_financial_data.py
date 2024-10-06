# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None
#stock_param = None

# -

import yfinance as yf
import datetime

start = datetime.datetime(2018,1,1)
end = datetime.datetime(2020,1,1)

data = yf.download('AAPL')
data.head()

data.to_csv('output/0_financial_data/financial_data.csv', index=False)