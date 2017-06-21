#   execfile('analysis_car_TIME.py')
import pandas as pd
import numpy as np
import math
import datetime
import matplotlib.pyplot as plt

file='/Users/xiangs/Dropbox/code/Data_Incubator/project/CAR_PRICE_TIME.csv'
df = pd.read_csv(file) #, low_memory=False
rows, cols = df.shape

#---------------------- Figure 1: Posts in Week -----------------------
weekday = []
for i in range(rows):
    mydate = df.ix[i, 'POSTDATE']
    print mydate
    md = datetime.datetime.strptime(mydate, '%Y-%m-%d').date()
    weekday.append(md.isoweekday())

outfile = open('weekday.txt', 'w')
for i in weekday:
    outfile.write("%d\n" % i)

count = [0,0,0,0,0,0,0] #1-7 Mon-Sun
for i in range(rows):
    count[weekday[i]-1] += 1

for n in range(7):
    count[n] = float(count[n])/rows
    print count[n]

plt.figure(1)
width = 0.45
wdt = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
ind = range(1,8)
p1 = plt.bar(ind, count, width, color='b')
plt.ylabel('Number of posts (normalized)')
plt.title('Probability of posts in a week')
plt.xticks(ind, ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
plt.yticks(np.arange(0, 0.21, 0.05))
#plt.savefig('Posts_week.eps', format='eps', dpi=600)
plt.savefig("Posts_week.png", dpi=600)
plt.show()




#---------------------- Figure 2: Posts in Day -----------------------
hour = []
for i in range(rows):
    mytime = df.ix[i, 'POSTTIME']
    print mytime
    mt = datetime.datetime.strptime(mytime, '%H:%M').time()
    hour.append(mt.hour)

a = np.zeros(24) #1-7 Mon-Sun
for i in range(rows):
    a[hour[i]] += 1

for n in range(24):
    a[n] /= rows
    print a[n]

plt.figure(2)
width = 0.45
ind = range(0,24)
p1 = plt.bar(ind, a, width, color='b')
plt.ylabel('Number of posts (normalized)')
plt.title('Probability of posts in a day')
plt.xticks(np.arange(0, 24, 3), ('0AM', '3AM','6AM', '9AM', '12PM', '3PM', '6PM', '9PM'))
#plt.yticks(np.arange(0, 0.21, 0.05))
#plt.savefig('Posts_week.eps', format='eps', dpi=600)
plt.savefig("Posts_day.png", dpi=600)
plt.show()




#---------------------- Figure 3: Average Price in Week -----------------------
accum = np.zeros(7) #1-7 Mon-Sun
count = np.zeros(7)
for i in range(rows):
    mydate = df.ix[i, 'POSTDATE']
    print mydate
    md = datetime.datetime.strptime(mydate, '%Y-%m-%d').date()
    accum[md.weekday()] += df.ix[i, 'PRICE']
    count[md.weekday()] += 1

for n in range(7):
    accum[n] /= count[n]
    print accum[n]

plt.figure(3)
width = 0.45
wdt = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
ind = range(7)
p1 = plt.bar(ind, accum, width, color='r', alpha=0.75)
plt.ylabel('Average posted price ($)')
plt.title('Average posted price in a week')
plt.xticks(ind, ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
#plt.yticks(np.arange(0, 0.21, 0.05))
#plt.savefig('Posts_week.eps', format='eps', dpi=600)

plt.xlim([-0.5, 7.5])
plt.show()

plt.savefig("Price_avg_week.png", dpi=600)



#---------------------- Figure 4: Average Price in Day -----------------------
accum = np.zeros(24) #0-23 hours
count = np.zeros(24)
for i in range(rows):
    mytime = df.ix[i, 'POSTTIME']
    #print mytime
    mt = datetime.datetime.strptime(mytime, '%H:%M').time()
    accum[mt.hour] += df.ix[i, 'PRICE']
    count[mt.hour] += 1

for n in range(24):
    accum[n] /= count[n]
    print accum[n]

plt.figure(4)
width = 0.45
ind = range(0,24)
p1 = plt.bar(ind, accum, width, color='r', alpha=0.5)
plt.ylabel('Average posted price ($)')
plt.title('Average posted price in a day')
plt.xticks(np.arange(0, 24, 3), ('0AM', '3AM','6AM', '9AM', '12PM', '3PM', '6PM', '9PM'))
plt.xlim([-0.5, 24.5])
#plt.yticks(np.arange(0, 0.21, 0.05))
#plt.savefig('Posts_week.eps', format='eps', dpi=600)
plt.savefig("Price_avg_day.png", dpi=600)
plt.show()



#---------------- Figure 5: Distribution of price(year,mile) --------------
# for example, Toyota Camry
from mpl_toolkits.mplot3d import Axes3D

df1 = df[df.MODEL == 'accord']
mean = df1.ix[:,'PRICE'].mean()
max = df1.ix[:,'PRICE'].max()
min = df1.ix[:,'PRICE'].min()

price = df1.ix[:,'PRICE'].values
mile = df1.ix[:,'MILES'].values
year = df1.ix[:,'YEAR'].values

C = []
sty = []
for p in price:
    if p > mean :
        C.append('r')
        sty.append('o')
    else :
        C.append('b')
        sty.append('^')

x=year.tolist()
y=mile.tolist()
y = map(int, mile.tolist())
z=price.tolist()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z, c=C, marker='o')
#for i in range(price.size):
#    ax.scatter(year[i],mile[i],price[i],c='b')
ax.set_title('Toyota Camry')
ax.set_xlabel('Model Year')
ax.set_ylabel('Miles')
ax.set_zlabel('Price ($)')
ax.set_xlim3d(1995, 2018)
ax.set_ylim3d(0, 300000)
ax.set_zlim3d(0, 25000)
plt.show()


#------------- Figure 6: 2D scatter plot, year and mile ------------
#colors = np.random.rand(N)
df1 = df[df.MODEL == 'fusion']
mean = df1.ix[:,'PRICE'].mean()
max = df1.ix[:,'PRICE'].max()
min = df1.ix[:,'PRICE'].min()

price = df1.ix[:,'PRICE'].values
mile = df1.ix[:,'MILES'].values
year = df1.ix[:,'YEAR'].values

x=year.tolist()
y=mile.tolist()
y = map(int, mile.tolist())
z=price.tolist()

zn=z
area=z
for i in range(len(z)):
    zn[i] = float(z[i]/25000.0)
    area[i] = np.pi * (15 * zn[i] )**2   # 0 to 15 point radii
#l = [x * 2 for x in l]


fig=plt.figure()
plt.scatter(x, y, s=area, c='b', alpha=0.5)
plt.title('Ford Fusion')
plt.xlabel("Model Year")
plt.ylabel("Miles")
plt.xlim([1995, 2020])
plt.ylim([-10000, 350000])
plt.show()


#------------- Output data for linear regression ------------
df1 = df[df.MODEL == 'civic']
rows, cols = df1.shape

price = df1.ix[:,'PRICE'].values
mile = df1.ix[:,'MILES'].values
year = df1.ix[:,'YEAR'].values

x=year.tolist()
y=mile.tolist()
y = map(int, mile.tolist())
z=price.tolist()

outfile = open('YEAR.txt', 'w')
for i in range(rows):
    outfile.write("%d\n" % x[i])

outfile = open('MILE.txt', 'w')
for i in range(rows):
    outfile.write("%d\n" % y[i])

outfile = open('PRICE.txt', 'w')
for i in range(rows):
    outfile.write("%d\n" % price[i])


#----------------------------------------------
#df3 = df.ix[:,['LO_RT', 'MD_RT', 'HI_RT']]
#df3 = df3.convert_objects(convert_numeric=True)

city = 'sfbay'
state = 'CA'

mymakelist = ['toyota', 'honda', 'nissan', 'ford', 'chevrolet']

brandpriceavg = []

df.MAKE = df.MAKE.str.lower()

#2017-2015, 2014-2012, 2011-2009, 2008-
for mymake in mymakelist:
    print mymake
    brandprice = [[], [], [], []]
    for i in range(rows):
        if df.CITY[i] == city :
            if df.MAKE[i] == mymake :
                if df.YEAR[i] >= 2015 :
                    brandprice[0].append(df.PRICE[i])
                else :
                    if df.YEAR[i] >= 2012 and df.YEAR[i] <= 2014 :
                        brandprice[1].append(df.PRICE[i])
                    else:
                        if df.YEAR[i] >= 2009 and df.YEAR[i] <= 2011 :
                            brandprice[2].append(df.PRICE[i])
                        else:
                            brandprice[3].append(df.PRICE[i])
            else :
                continue
        else :
            continue
    ap = []
    for a in range(4):
        if len(brandprice[a]) != 0 :
            ap.append(sum(brandprice[a])/len(brandprice[a]) )
        else :
            ap.append(0)
    brandpriceavg.append(ap)

print brandpriceavg





#if not math.isnan(df.ix[i,'PRICE']) :


with open("sflist.csv", "wb") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sflist)

with open("boslist.csv", "wb") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(boslist)




'''
    if not math.isnan(df3.ix[i,'NAME']) :
    diff.append(df3.ix[i,'HI_INC_COMP_ORIG_YR4_RT'] 
    df3.ix[i,'LO_INC_COMP_ORIG_YR4_RT'])


# two-sample t-test the difference between high and low income completion rate

import random
from scipy import stats

random.shuffle(diff)

diffarray = np.array(diff)
l=len(diffarray)
half = l/2
a = diffarray[0:half]
b = diffarray[half: half*2]

t, p = stats.ttest_ind(a, b, equal_var=True)

math.log10(p)

# Ttest_indResult(statistic=-12.457714659359038, pvalue=5.7045487112816616e-35)
# log10 (p) = -34.243778707065644

'''








