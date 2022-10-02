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

df_1 = pd.read_csv('read_path')[60:217]
df_2 = pd.read_csv('read_path')[260:936]

#%%
#trends from 2009 to 2021

fig, ax = plt.subplots(2, 1,figsize=(20,8))

a1, = ax[0].plot(range(676),df_2['cases'],color='#3C5488FF',label='HFMD cases',linewidth=2)
a2, = ax[1].plot(range(157),df_1['topic'],color='#E64B35FF',label='HFMD RSV',linewidth=2)

ax[1].set_xlabel('Year',fontsize=15,labelpad=15)
ax[0].set_ylabel('Actual cases',fontsize=15,labelpad=13)
ax[1].set_ylabel('RSV',fontsize=15,labelpad=20)
ax[0].set_title('Changes of HFMD actual cases and Internet search RSV from 2009 to 2021',fontsize=20,pad=35,loc='center')

ax[0].patch.set_facecolor('w')
ax[1].patch.set_facecolor('w')

_xticks = [f'200{i}' for i in range(9,10)]
_xticks += [f'20{i}' for i in range(10,23)]
plt.setp(ax[0], xticks=list(range(676))[::52], xticklabels=_xticks)

ax[0].axis('on')
plt.setp(ax[1], xticks=list(range(157))[::12], xticklabels=_xticks)
plt.setp(ax[0], xticks=list(range(676))[::52], xticklabels=[])

ax[0].legend(loc='upper left')
ax[1].legend(loc='upper left')
ax[1].tick_params(axis='both', labelsize=14)

ax[0].spines['bottom'].set_color('black')
ax[0].spines['left'].set_color('black')
ax[1].spines['bottom'].set_color('black')
ax[1].spines['left'].set_color('black')

ax[0].tick_params(axis='both', labelsize=14)
ax[1].tick_params(axis='both', labelsize=14)

ax[0].set_xlim(0,676)
ax[0].set_ylim(bottom=0)
ax[1].set_xlim(0,156)
ax[1].set_ylim(0,101)

# dashline
ax[0].plot((360, 360), (0, 40000), '--',linewidth=2, color='grey')
ax[0].plot((828-260, 828-260), (0, 40000), '--',linewidth=2, color='grey')
ax[0].plot((672, 672), (0, 40000), '--',linewidth=2, color='grey')

ax[1].plot((83, 83), (0, 100), '--',linewidth=2, color='grey')
ax[1].plot((192-61, 192-61), (0, 100), '--',linewidth=2, color='grey')
ax[1].plot((155, 155), (0, 100), '--',linewidth=2, color='grey')

# text
ax[0].text(440,40000,'Period 1',fontsize=16)
ax[0].text(600,40000,'Period 2',fontsize=16)


plt.show()

fig.savefig('save_path',bbox_inches='tight')