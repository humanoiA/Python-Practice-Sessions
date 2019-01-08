import pandas as pd 
import quandl
df=quandl.get('NSE/ORIENTELEC')
print(df.head())