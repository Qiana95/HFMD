#%%
# import packages
from copy import deepcopy
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
import warnings
warnings.simplefilter('ignore')

#%%
# read data
excel = pd.read_excel("../search_terms_rsv.xlsx", sheet_name="lag_0_2020")
X = excel.drop(columns=["time", "cases"])
y = excel.iloc[:,1]


# %% 
# the original model
X0 = sm.add_constant(X)
est = sm.OLS(y, X0)
est0 = est.fit()
# print(est2.summary())
pvs = est0.pvalues.drop(labels=["const"])
pmax = pvs.max()

#%%
# make unrestricted model
X1 = None # Xs of unrestricted model
while (pvs > 0.1).sum() != 0:
    if pmax != -1:
        col = pvs.loc[pvs==pmax].keys()[0]
        X = X.drop(columns=[col])
        # print(f"remove {col}")
    X1 = sm.add_constant(X)
    est = sm.OLS(y, X1)
    est1 = est.fit()
    
    pvs = est1.pvalues.drop(labels=["const"])
    pmax = pvs.max()
    
print(est1.summary())

#%%
# make restricted model
XX = deepcopy(X)
X2 = None # Xs of restricted model
rm_list = [] # list of words removed from unrestricted model
while (pvs > 0.05).sum() != 0:
    if pmax != -1:
        col = pvs.loc[pvs==pmax].keys()[0]
        XX = XX.drop(columns=[col])
        # print(f"remove {col}")
        rm_list.append(col)
    
    XX = XX.select_dtypes(include=[np.number]).dropna().apply(stats.zscore)
    X2 = sm.add_constant(XX)
    y = (y-y.mean())/y.std()
    est = sm.OLS(y, X2)
    est2 = est.fit()
    
    pvs = est2.pvalues.drop(labels=["const"])
    pmax = pvs.max()
    
print(est2.summary())

# %%
# F-test function
def cal_F(est1, est2):
    q = len(est1.pvalues.keys()) - len(est2.pvalues.keys())
    a = (est1.rsquared - est2.rsquared) / q
    b = (1 - est1.rsquared) / est1.df_resid
    
    F = a / b
    level = stats.f.ppf(q=0.95, dfn=q, dfd=est1.df_resid)
    
    reject = "Not all zeros"
    if F <= level:
        reject = "All zeros"
    
    return a / b, level, reject
F0, level0, reject0 = cal_F(est1, est2)
print(F0, level0, reject0)

#%%
# meke the correlation matrix on rm_list and get high correlations
rm_trends = []
for rm_word in rm_list:
    rm_trends.append(X[rm_word].to_numpy())
rm_trends = np.array(rm_trends)
corr_mat = np.corrcoef(rm_trends)
np.fill_diagonal(corr_mat, 0)

# get the high correlating words
corr_mat = np.abs(corr_mat)
high_corrs = []
for i in range(len(corr_mat.flatten())):
    ind = np.argmax(corr_mat)
    a, b = ind // len(rm_list), ind % len(rm_list)
    if corr_mat[a][b] == 0:
        break
    
    corr_mat[a][b] = 0
    corr_mat[b][a] = 0
    high_corrs.append((rm_list[a], rm_list[b]))

# %%
# retrain model with high correlation pairs
not_zero_list = set()
for pair in high_corrs:
    xa, xb = pair
    XX_temp = deepcopy(XX)
    XX_temp[xa] = X[xa]
    XX_temp[xb] = X[xb]
    
    X3 = sm.add_constant(XX_temp)
    est = sm.OLS(y, X3)
    est3 = est.fit()

    F_temp, level_temp, reject_temp = cal_F(est3, est2)
    # print(xa, xb, F_temp, level_temp, reject_temp)
    if reject_temp == "Not all zeros":
        # not_zero_list.append([xa, xb])
        print(xa, xb, F_temp, level_temp, reject_temp)
        not_zero_list.add(xa)
        not_zero_list.add(xb)
    else:
        pass
        # break
    
# print(not_zero_list)

# %%
# check the adjusted model
XX_temp = deepcopy(X)
XX_temp = XX_temp.drop(columns=list(not_zero_list))
X3 = sm.add_constant(XX_temp)
est = sm.OLS(y, X3)
est3 = est.fit()

F_temp, level_temp, reject_temp = cal_F(est3, est2)
print(F_temp, level_temp, reject_temp)

# %%
