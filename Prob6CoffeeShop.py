#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

data = np.genfromtxt('coffee_shop_50.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

tx = data['transactions']
avg = data['avg_ticket']
refunds = data['refunds']

revenue = tx * avg - refunds

# calculate mean, mediand and standard deviation of revenue
mean=np.mean(revenue)
median=np.median(revenue)
std=np.std(revenue)

print("Mean: ", mean)
print("Median: ", median)
print("StaDev: ", std)

#top 5 revenue

top_5=np.argsort(revenue)[-5:][::-1] #sort number from lower to higher, slice the last 5 and order those 5 from high to low
top_5_dates=data['date'][top_5] #take the date of the picked indexes 
top_5_revenues=revenue[top_5] #take the revenue of the picked indexes 

#print the result from the picked indexes (date and revenue), zip helps to combine 2 lists
print("Top 5 dates revenue:")
for date, rev in zip(top_5_dates, top_5_revenues):
    print(date, rev)

#Broadcasting scenario: A 10-day promo increases foot traffic by +8% transactions but reduces average ticket by −5% on those same days.

#increase 8% to 10 first days 

tx_promo=tx[:10]*1.08

print("Increse transactions:",tx_promo)

#reduce 5% on ticket average in same 10 days

avg_promo=avg[:10]*0.95

print("Reduction avg ticket:",avg_promo)

#Recompute revenue for those days and report the net revenue change over those 10 days

new_revenue= tx_promo*avg_promo-refunds[0:10]
net_rev_change=np.sum(new_revenue-refunds[0:10])

print("Net revenue change over first 10 days:",net_rev_change)

#Count how many days had revenue ≥ the overall median revenue.

high_rev_days= revenue>=median
count_high_rev_days= np.sum(high_rev_days)

print("Days that had higher revenue than the overall median revenue:",count_high_rev_days)







# In[ ]:




