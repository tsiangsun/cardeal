#execfile('analysis_car.py')
#import pandas as pd
import numpy as np
import math


file='/Users/xiangs/Dropbox/code/Data_Incubator/project/USED_CARS_DATA.csv'

df = pd.read_csv(file) #, low_memory=False

rows, cols = df.shape

#df3 = df.ix[:,['LO_INC_COMP_ORIG_YR4_RT', 'MD_INC_COMP_ORIG_YR4_RT', 'HI_INC_COMP_ORIG_YR4_RT']]
#df3 = df3.convert_objects(convert_numeric=True)

city = 'sfbay'
state = 'MA'

mymakelist = ['ford', 'cheverolet', 'chrysler', 'jeep', 'toyota', 'honda', 'nissan', 'subaru', 'mazda', 'mercedes', 'bmw', 'audi', 'vw', 'hyundai', 'kia']

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


sflist = [[15252, 11800, 8561, 3973], [0, 14000, 55000, 15685], [13666, 11924, 9557, 5499], [28921, 20911, 19350, 8953], [18248, 12596, 9042, 4780], [18139, 13138, 8918, 4769], [11927, 10274, 7048, 3532], [28460, 18724, 13270, 5883], [14063, 11026, 8103, 4768], [21265, 26274, 14879, 6938], [14673, 26776, 15696, 7194], [29448, 29118, 12851, 5584], [14727, 12631, 5792, 3847], [12361, 10368, 7550, 2455], [11205, 11696, 6651, 2512]]


boslist= [[18067, 25248, 7428, 4353], [0, 0, 15900, 16900], [15000, 7603, 6200, 5015], [28110, 24322, 15161, 6497], [14800, 12409, 8010, 4578], [18298, 12148, 7723, 4963], [14452, 10996, 6080, 3326], [24715, 16573, 10396, 4410], [19500, 12628, 6373, 4330], [30531, 23127, 12166, 7263], [25995, 22986, 13542, 6616], [25053, 26803, 14234, 4629], [15396, 12868, 4728, 3122], [13939, 9885, 6270, 2895], [13516, 10788, 7393, 6518]]


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








