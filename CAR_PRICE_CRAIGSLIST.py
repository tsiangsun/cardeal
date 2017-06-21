#   execfile('CAR_PRICE_CRAIGSLIST.py')
import re
import urllib
import urllib2
import math
import numpy as np
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers = {'User-Agent': user_agent}

url='https://dealsea.com'

req = urllib2.Request(url, None, headers)
page = urllib2.urlopen(req)
html_str = page.read()


mymake='ford'
mymodellist=['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition']

mymake='cheverolet'
mymodellist=['spark', 'cruze' ,'malibu','impala', 'taurus', 'trax', 'equinox', 'traverse', 'tahoe', 'suburban', 'camaro', 'corvette']

mymake='chrysler'
mymodellist=['200', '300' ]

mymake='jeep'
mymodellist=['wrangler', 'compass', 'cherokee', 'renegade', 'patriot' ]

mymake='toyota'
mymodellist=['yaris' ,'corolla','camry', 'avalon', 'rav4', 'highlander', 'prius', 'sienna']

mymake='honda'
mymodellist=['fit' ,'civic','accord', 'crv', 'pilot', 'hrv', 'prius', 'odssey']

mymake='nissan'
mymodellist=['versa', 'sentra' ,'altima','maxima', 'joke', 'rogue', 'murano', 'pathfinder']

mymake='mazda'
mymodellist=['3' ,'6','cx-3', 'cx-5', 'cx-9', 'mx-5']

mymake='mercedes'
mymodellist=['c300' ,'c350','e320', 'e350', 'e500', 'e550', 'e400', 's500','s550','cla250', 'cls550', 'ml320','ml350'  ]

mymake='bmw'
mymodellist=['x1','x2','x3', 'x5', 'x6','328i' ,'328xi','335i', '335xi', '525i', '528i', '525xi', '528xi','545i','545xi', '550i', '550xi','750i', '750xi','750li']

mymake='audi'
mymodellist=['a3' ,'a4','a5', 'a6', 'a7', 'a8', 's3', 'rs3','s7','rs7', 's8', 'q3','q5', 'q7','tt' ]

mymake='vw'
mymodellist=['jetta' ,'passat','cc', 'golf', 'tiguan', 'touareg', 'beetle' ]

mymake='hyundai'
mymodellist=['elantra' ,'sonata','azera', 'tucson', 'santafe', 'accent', 'veloster','genesis' ]

mymake='kia'
mymodellist=['optima' ,'soul','niro', 'sportage', 'sorento', 'cadenza', 'k900','rio','forte', 'sedona' ]



mymakelist = ['ford', 'cheverolet', 'chrysler', 'jeep', 'toyota', 'honda', 'nissan',  'mazda', 'mercedes', 'bmw', 'audi', 'vw', 'hyundai', 'kia']


mymodellistlist = [ ['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition'], ['spark', 'cruze' ,'malibu','impala', 'taurus', 'trax', 'equinox', 'traverse', 'tahoe', 'suburban', 'camaro', 'corvette'], ['200', '300'], ['wrangler', 'compass', 'cherokee', 'renegade', 'patriot'], ['yaris' ,'corolla','camry', 'avalon', 'rav4', 'highlander', 'prius', 'sienna'], ['fit' ,'civic','accord', 'crv', 'pilot', 'hrv', 'prius', 'odssey'], ['versa', 'sentra' ,'altima','maxima', 'joke', 'rogue', 'murano', 'pathfinder'], ['3' ,'6','cx-3', 'cx-5', 'cx-9', 'mx-5'], ['c300' ,'c350','e320', 'e350', 'e500', 'e550', 'e400', 's500','s550','cla250', 'cls550', 'ml320','ml350' ], ['x1','x2','x3', 'x5', 'x6','328i' ,'328xi','335i', '335xi', '525i', '528i', '525xi', '528xi','545i','545xi', '550i', '550xi','750i', '750xi','750li'], ['a3' ,'a4','a5', 'a6', 'a7', 'a8', 's3', 'rs3','s7','rs7', 's8', 'q3','q5', 'q7','tt' ], ['jetta' ,'passat','cc', 'golf', 'tiguan', 'touareg', 'beetle' ], ['elantra' ,'sonata','azera', 'tucson', 'santafe', 'accent', 'veloster','genesis' ], ['optima' ,'soul','niro', 'sportage', 'sorento', 'cadenza', 'k900','rio','forte', 'sedona' ]]


'''
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
page = response.read()  #html text file as string
'''

#nlines = page.count('\n')

#with open("test.txt", "a") as outfile:
#    outfile.write("appended text")

#while line != '':

#page = urllib.urlopen(url)



'''
line = page.readline()  #line is native "str" object

while (line !='') :
    m = re.search(r'', line)







file = '/Users/xiangs/Data/CollegeScorecard_Raw_Data/MERGED2014_15_PP.csv'
print file
df = pd.read_csv(file, low_memory=False)
df0 = df.ix[:,['REGION', 'LOCALE']]
df1 = df0.dropna(how='any')

count_city = np.zeros(11)
count_total = np.zeros(11)

rows, cols = df1.shape
for i in range(rows):
    re = df1.ix[i,'REGION']
    loc = df1.ix[i,'LOCALE']
    count_total[re] += 1.0
    if loc > 10 and loc < 20 :
        count_city[re] += 1.0

for i in range(1,10) :
    count_city[i] /= count_total[i]
    print 'Region # ', i, '  Prob_city = ', count_city[i]

'''




