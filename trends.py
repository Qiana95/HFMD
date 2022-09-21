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
# import data
df_1 = pd.read_csv('/Users/gyuuakane/Documents/projects/statistics/HFMD/HFMD_rsv.csv')
df_2 = pd.read_csv('/Users/gyuuakane/Documents/projects/statistics/HFMD/HFMD_cases.csv')

# %%
df_1
# %%
df_2
# %%
## trends from 2004 to 2021

fig, ax = plt.subplots(2, 1,figsize=(20,8))

a1, = ax[0].plot(range(970),df_2['cases'],color='#3C5488FF',label='HFMD cases',linewidth=2)
a2, = ax[1].plot(range(225),df_1['rsv'],color='#E64B35FF',label='HFMD RSV',linewidth=2)

ax[1].set_xlabel('Year',fontsize=15,labelpad=15)
ax[0].set_ylabel('Actual cases',fontsize=15,labelpad=13)
ax[1].set_ylabel('RSV',fontsize=15,labelpad=20)
ax[0].set_title('Changes of HFMD actual cases and Internet search RSV from 2004 to 2021',fontsize=20,pad=35,loc='center')

ax[0].patch.set_facecolor('w')
ax[1].patch.set_facecolor('w')

_xticks = [f'200{i}' for i in range(4,10)]
_xticks += [f'20{i}' for i in range(10,23)]
plt.setp(ax[0], xticks=list(range(970))[::52], xticklabels=_xticks)

ax[0].axis('on')
plt.setp(ax[1], xticks=list(range(225))[::12], xticklabels=_xticks)
plt.setp(ax[0], xticks=list(range(970))[::52], xticklabels=[])

ax[0].legend(loc='upper left')
ax[1].legend(loc='upper left')
ax[1].tick_params(axis='both', labelsize=14)

ax[0].spines['bottom'].set_color('black')
ax[0].spines['left'].set_color('black')
ax[1].spines['bottom'].set_color('black')
ax[1].spines['left'].set_color('black')

ax[0].tick_params(axis='both', labelsize=14)
ax[1].tick_params(axis='both', labelsize=14)

ax[0].set_xlim(0,950)
ax[0].set_ylim(bottom=0)
ax[1].set_xlim(0,221)
ax[1].set_ylim(0,101)

# dashline
ax[0].plot((568, 568), (0, 40000), '--',linewidth=2, color='grey')
ax[0].plot((828, 828), (0, 40000), '--',linewidth=2, color='grey')
ax[0].plot((949, 949), (0, 40000), '--',linewidth=2, color='grey')

ax[1].plot((132, 132), (0, 100), '--',linewidth=2, color='grey')
ax[1].plot((192, 192), (0, 100), '--',linewidth=2, color='grey')
ax[1].plot((220, 220), (0, 100), '--',linewidth=2, color='grey')

# text
ax[0].text(670,40000,'Period 1',fontsize=16)
ax[0].text(860,40000,'Period 2',fontsize=16)


plt.show()

# fig.savefig('/Users/gyuuakane/Documents/projects/statistics/HFMD/trends.png',bbox_inches='tight')
# %%
