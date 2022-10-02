#%%
import numpy as np
from numpy import *
import pandas as pd
from scipy import stats
from scipy.stats import sem
import seaborn as sns; sns.set_theme()
import matplotlib as mpl
import matplotlib.pyplot as plt

#%%
# read data
df_rsv = pd.read_csv('read_path')
df_cases = pd.read_csv('read_path')

df_rsv = df_rsv[1:53]
df_cases = df_cases[1:53]

#%%
# caculate Pearson correlation
ls = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
lr = []
for i in ls:
  r = np.corrcoef(df_rsv[f'topic_{i}'], df_cases[f'{i}'])
  r = round(r[0][1],3)
  lr.append(r)
  print(f'{i}:{r}')
  
#%%

## bar correlation

plt.figure(figsize=(20,8))
plt.rcParams['axes.facecolor'] = 'w'

bar_1 = plt.bar(range(len(lr)),lr,color='#3C5488FF',tick_label=ls)

# lr_1 = [0.562,0,0,0,0.236,0,0,0,0,0,0,0,0,0,0,0,0.338,0]
lr_1 = [0,0,0,0,0,0,0,0,0,0,0,0.338,0]
bar_2 = plt.bar(range(len(lr_1)),lr_1,color='#F39B7FFF',tick_label=ls)

# plt.legend([bar_1,bar_2],['r<0.7','r≥0.7'],loc='upper right')


plt.xlabel('Year',fontsize=18,labelpad=15)
plt.ylabel('Pearson correlation coefficient (r)',fontsize=18,labelpad=15)
plt.title("Correlation between actual HFMD cases and HFMD's Interest search RSV from 2009 to 2021",fontsize=22,pad=40,loc='center')
plt.tick_params(labelsize=15)

my_y_ticks = np.arange(0,1.1,0.1)
plt.yticks(my_y_ticks)
plt.ylim(0,1.0)

plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')

plt.axhline(y=0.7,linewidth=4, color='black',linestyle='--')

# plt.savefig('save_path',bbox_inches='tight')
plt.show()