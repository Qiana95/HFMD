#%%
import numpy as np
import pandas as pd
import statsmodels.api as sm
import re
from pandas.core.frame import DataFrame

#%%
# import data

# excel = pd.read_excel("2020_lag_select.xlsx", sheet_name="lag_0_without2022")
excel = pd.read_excel("2016_lag_select.xlsx", sheet_name="lag_0")
df = excel.drop(columns=["time", "cases"])


#%%
ls = []
for index, column in df.iteritems():
  ls.append(index)

#%%
ls

#%%
lt = []
for index in ls:
  # print(index)

  # define data 
  df_1 = excel['cases']
  df_2 = df[f'{index}']

  # calculate cross correlation
  ar1 = sm.tsa.stattools.ccf(df_1,df_2, adjusted=False)[:20]
  ar2 = sm.tsa.stattools.ccf(df_2,df_1, adjusted=False)[:20]
  ar = np.concatenate((ar2,ar1))
#   print(ar)

  # print lag result
  lag = int(np.where(ar==np.max(ar))[0][0])
#   print(lag)

  if 0 < lag < 20:
    lt.append([f'{index}',"latter",lag, round(np.max(ar),3)])
  elif lag > 10:
    lt.append([f'{index}','earlier',lag-20, round(np.max(ar),3)])
  else:
    lt.append([f'{index}','conincide',0, round(np.max(ar),3)])
    
# %%
data = DataFrame(lt)
# %%
data.to_csv('./cross_2016.csv',encoding= 'utf-8-sig')
# data.to_csv('./cross_2020.csv',encoding= 'utf-8-sig')
# %%
