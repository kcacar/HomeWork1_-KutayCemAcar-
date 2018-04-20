
# coding: utf-8

# In[71]:


import pandas as pd
import nsfg
import numpy as np
import thinkstats2 as ts2
import thinkplot as tp


# In[100]:


resp=nsfg.ReadFemResp()
resp


# In[63]:


mean = resp["agemomb1"].mean()
median = resp["agemomb1"].median()

print "median : "(mean)
print (median)

agemotherfb=resp.agemomb1
print('1) LESS THAN 18 YEARS 1035')
print('2) 18-19 YEARS 1003') 
print('3) 20-24 YEARS 2076')
print('4) 25-29 YEARS 980')
print('5) 30 OR OLDER 396')


# In[73]:


school=resp[resp.hieduc<=10]
university = resp[resp.hieduc>=10]


# In[87]:


pmf_of_school=thinkstats2.Pmf(school.agemomb1)
pmf_of_university=thinkstats2.Pmf(university.agemomb1)
thinkplot.PrePlot(2)
thinkplot.Pmf(pmf_of_school, label='School',color="red")
thinkplot.Pmf(pmf_of_university, label='University',color="blue")
thinkplot.Config(title='PROBABILITY MASS FUNCTION OF AGES OF MOTHERS AT FIRST BIRTH', xlabel='MOTHER AGE CODE', ylabel='PMF')


# In[89]:


cdf_of_schoolcdf_of_ =ts2.Cdf(school.agemomb1)
cdf_of_university=ts2.Cdf(university.agemomb1)
tp.PrePlot(2)
tp.Cdf(cdf_of_school, label='School',color="red")
tp.Cdf(cdf_of_university, label='University',color="blue")
tp.Config(title='CUMULATIVE MASS FUNCTION OF AGES OF MOTHERS AT FIRST BIRTH', xlabel='mOTHER AGE CODE', ylabel='CDF')


# In[88]:


my_list=[]
for i in pmf_of_school:
    m=pmf_of_school.Prob(i)-pmf_of_university.Prob(i)
    my_list.append(m)


# In[91]:


thinkplot.Bar(pmfofschool,my_list)
thinkplot.Config(title='Difference between 2 group', xlabel='mothers_ages_of_firstbirth', ylabel='discrepancy_btwn_uni_and_school')


# In[95]:


most_birth = resp.cmlastlb
cdf = thinkstats2.Cdf(most_birth, label='Ages')

thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='MOST RECENT LIVE BIRTH ', ylabel='prob', yscale='log')


# In[99]:


x= resp.cmfstprg
y= thinkstats2.Cdf(x,label="information")
thinkplot.Cdf(y)
thinkplot.Config(xlabel='completed preg', ylabel='probabilities')

