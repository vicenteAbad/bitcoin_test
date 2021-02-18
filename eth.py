# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cbpro

import pandas as pd
from datetime import datetime

# pandas solo 4 decimales
pd.set_option('precision', 4)
public_client = cbpro.PublicClient()


df = pd.DataFrame(public_client.get_product_historic_rates('ETH-USD', granularity=86400), columns = [ 'time', 'Low', 'High', 'Open', 'Close', 'Volume' ]) 
df.index  = df['time'].apply(lambda x: datetime.fromtimestamp(x))

df

#%%
import matplotlib.pyplot as plt
import talib

df['Close'].plot(figsize=(10, 8))



#%%
import talib
df2 = df.iloc[::-1]

df2['SMA1'] = talib.SMA(df2['Close'].values, timeperiod=16)
df2['SMA2'] = talib.SMA(df2['Close'].values, timeperiod=25)
df = df2.iloc[::-1]

#%%
df['Close'].plot(figsize=(10, 8))
df['SMA1'].plot(figsize=(10, 8)) 
df['SMA2'].plot(figsize=(10, 8)) 


#%%
import numpy as np
x = df['SMA1'].values
y = df['SMA2'].values
idx = np.argwhere(np.diff(np.sign(x - y))).flatten()

plt.plot(df.index, df['Close'])
plt.plot(df.index, df['SMA1'])
plt.plot(df.index, df['SMA2'])
plt.plot(df.index[idx], y[idx], 'ro')
plt.show()


#%%
df.dropna()
df["x"] = df['SMA1'] - df['SMA2']