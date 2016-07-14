#How ISIS Uses Twitter

##Temporal Exploration of the Data

I was able to obtain a nice little dataset from [Kaggle](https://www.kaggle.com/) containing some tweets and metadata from known Pro-ISIS twitter users.  My thesis used twitter as a main source of information, and so this dataset begged for some analysis.

The data contained
	* The user’s username
	* The content of the tweet
	* The time the tweet was posted
	* And other associated metadata

One of the things I like to do is examine temporal aspects of data.  Questions like “How many tweets were made during the first month?” and “What is the general trend as time progresses?” are questions that can be answered by examining the temporal frequency of the data.  Let’s examine the time series of tweets made.  This will tell us how many tweets were made on a particular day.

![Time Series][https://github.com/Dpananos/How-Isis-Uses-Twitter/blob/master/Images/time_series.png?raw=true]

Wow! Activity really picks up in the early weeks of 2016. Then there is some erratic behaviour in the later parts of the data. I wonder why that could be?  Perhaps they are tweeting about an ISIS attack?  Without looking at the text (a problem for future analysis) it is hard to say without attack data.  Fortunately, I managed to find the dates of major ISIS attacks.  Let’s overlay the dates of major attacks on the time series data.

![Attacks][https://github.com/Dpananos/How-Isis-Uses-Twitter/blob/master/Attacks.pdf]

Shown in blue dots are the days where a major attacked occurred.  The height of the dot indicates how many tweets were made that day.  I’ve made special markers for the most memorable ISIS attacks.  It doesn’t look like any particular events cause the oscillations.  

##Oscillations Examined

OK, so the oscillations aren’t caused by any one particular attack.  Let’s try another approach.  

Mathematical epidemiologists usually look at the frequency of outbreaks to try and predict when the next outbreak of a disease will occur.  Let’s do something similar to these oscillations.

Shown below are the time series of the oscillations from January 30 2016 to the end of the data set.

![Osci][https://github.com/Dpananos/How-Isis-Uses-Twitter/blob/master/osci.pdf]

Let’s use a periodogram to examine the frequency of these oscillations.  This will give us insight into how frequent they are.  The horizontal axis on peridograms is measured in 1/Days, and so I’ve marked where a frequency of 2 to 7 days would lay on the horizontal axis.

![perdio][https://github.com/Dpananos/How-Isis-Uses-Twitter/blob/master/periodo.pdf]

OK, so it is pretty clear from the periodogram that the signal has a frequency of about 7 days, which would suggest weekly tweeting.  On what days do these weekly tweets occur?  Since the metadata includes dates, we can easily determine which day of the week the tweets were made.  It can be shown that most of these oscillations occur on a Friday.  In the Islamic faith, [Jumu’ah](https://en.wikipedia.org/wiki/Jumu%27ah) is held on Fridays, and so I highly suspect this is why peaks of oscillations occur on Fridays.

The next step is to examine the contents of these tweets, but that is for another day.
