#%%
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

# comment
#%%
excel = pd.read_excel("2016_lag_select.xlsx", sheet_name="lag_0")
X = excel.drop(columns=["time", "cases"])
y = excel.iloc[:,1]

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

#%%
# pmax = -1
# while True:
#     if pmax != -1:
#         X = X.drop(columns=)
#     X2 = sm.add_constant(X)
#     est = sm.OLS(y, X2)
#     est2 = est.fit()
#     print(est2.summary())

# %%
