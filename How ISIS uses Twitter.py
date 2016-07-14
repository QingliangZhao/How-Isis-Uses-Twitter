
# coding: utf-8

# In[1]:

# I was able to obtain a nice little data set from Kaggle on some pro ISIS twitter users.
# Let's see what the data contains.

# Here are the libraries I am using
import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import re
import numpy as np
from scipy import signal

# Some nice plotting params
mpl.rcParams['figure.figsize'] = (1,0.5)
mpl.rcParams['lines.linewidth'] = 3
plt.style.use('ggplot')


# In[2]:

#Read in the data.  Seems like the dates are the second last column
df = pd.read_csv('tweets.csv', parse_dates = [-2])

df.columns


# In[5]:

#Looks like we have
    # The name the user gave twitter
    # The content of the tweet
    # The time it was posted
    # And some other metadata

#One of the things I like to do for temporal data is visualize what happens over time.  
#That lets me know if something changes drastically.  If something does change, we can investigate why.

def f(x): # I don't really care about the times that the tweets were made, just the dates
    return dt.datetime(x.year,x.month,x.day)

df['time'] = df.time.apply( f)

time_series = pd.DataFrame(df.time.value_counts().sort_index().resample('D').mean().fillna(0))
time_series.columns = ['Tweets']

ax = time_series.plot()
ax.margins(None,0.1)
ax.set_xlabel('Date')
ax.set_ylabel('No. of Tweets')
plt.savefig('images/time_series.png')


# In[7]:

#WOW look at those crazy oscillations.  Pro ISIS tweets start to pick up around September 2015
#But why?  Could it have to do with a major attack?  I managed to scrape some attack data, so let's visualize that too.

attacks = pd.read_csv('attack_dates.csv', index_col = 0, usecols = [0,1])
del attacks.index.name


isis_attacks= time_series.merge(attacks, left_index = True, right_index = True, how = 'left').dropna().rename(columns ={'Tweets':'Major Attacks'})
isis_attacks = time_series.merge(isis_attacks, left_index = True, right_index = True, how = 'left').ix[:,0:2]

ax = isis_attacks.plot(style = ['-','o'], markeredgewidth = 0)
ax.margins(None, 0.1)

brussels = '2016-03-22'
paris = '2015-11-13'


ax.plot(brussels,isis_attacks['Major Attacks'].ix[brussels],color = 'w',
        marker = '^',markersize = 12, linestyle = '',
        label = 'Brussels Bombing', markeredgewidth = 2)

ax.plot(paris,isis_attacks['Major Attacks'].ix[paris],color = 'w',
        marker = 'o', markersize = 12, linestyle = '',
        label = 'Paris Shooting', markeredgewidth = 2)

ax.legend(numpoints = 1, loc = 'upper left')
ax.set_xlabel('Date')
ax.set_ylabel('No. of Tweets')
plt.savefig('images/Attacks.png')


# In[6]:

#Tweets start to pick up after the paris shooting, so that could be the cause of these wild oscillations.


# In[7]:

#I wonder about the nature of these oscillations.  What are they?  How often are they happening?
# What is the content of these tweets contributing to the oscillations.

# The most natural way to study these oscillations is with a periodogram.


# In[9]:

oscillations = time_series.ix['2016-01-31':]

ax = oscillations.plot()
ax.set_xlabel('Date')
ax.set_ylabel('No. of Tweets')
plt.savefig('images/osci.png')



# In[10]:

ossie = oscillations.values.ravel()
fs = np.fft.fftfreq(np.arange(len(ossie)).shape[-1])
x,y = signal.periodogram(ossie)

plt.figure()
plt.plot(x,y,marker = 'o', linestyle = '--')

oneov = [1.0/j for j in range(2,8)]
plt.xticks(oneov,range(2,8))
ax = plt.gca()


ax.grid(True)
ax.set_yticklabels([])
ax.set_xlabel('No. of Days')
plt.savefig('images/periodo.png')


# In[21]:

#Looks like the signal has a frequency of 7 days, suggesting that there are a bunch of tweets happening weekly.  
# Ok, well, on what day do they occur?


# In[30]:

p = signal.find_peaks_cwt(ossie, np.arange(1,4) )

t = np.arange(len(ossie))
plt.plot(t,ossie)
plt.plot(t[p],ossie[p],'o')



# In[31]:

#Looks like we got most of the peaks.  Now let's see what day they occur on.


# In[37]:

r = oscillations.ix[p].reset_index().copy()

r.columns = ['date','tweet']

r['weekday'] = r.date.apply(lambda x: x.weekday())


# In[41]:

r.weekday.mode()


# In[ ]:



