#   execfile('re_search.py')
import re
import urllib
import urllib2
import math
import csv
import numpy as np
import random
import time



#mymodel='test'
city = 'sfbay'
state = 'CA'

#mymake='ford'
#mymodellist=['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition']
#for mymodel in mymodellist:



mymake = 'toyota'
mymodel = 'camry'
keyword = mymake + '+' + mymodel

min_year='&min_auto_year=1997'
max_year='&max_auto_year=2017'

url = 'https://'+ city + '.craigslist.org/search/cto?query=' + keyword + '&hasPic=1' + min_year + max_year

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers = {'User-Agent': user_agent}

pid =[]
postdate = []
clcity = []
clstate = []
make = []
model = []
year = []
price = []
miles = []
link = []
title = []

'''
message = []
transmisson = []
color =[]
condition = []
titlestatus = []
fuel = []
'''
#https://sfbay.craigslist.org/search/cto?query=toyota+camry&hasPic=1&min_auto_year=1997&max_auto_year=2017
#https://sfbay.craigslist.org/search/cto?s=120&hasPic=1&min_auto_year=1997&max_auto_year=2017?query=toyota+camry&hasPic=1


PATTERN_SEARCH = r'(<time class=).+(\d{4}-\d{2}-\d{2}) .*\n\n\s+<a href="(\/*\w*)\/cto\/(\d{10}).+result-title hdrlnk">([\w\d\s\-\*\$\.!:\'\,\(\)]+)<\/a>\n\n\s+<span.+\n\s+<span.*\$([0-9]+)<\/span>'

PATTERN_NEXT = r'<link rel="next" href="https\:\/\/\w+\.craigslist\.org\/search\/cto(\?s=\d{3,4})&'

PATTERN_YEAR = r'.*(199\d{1}|20[0-1][0-9]).*'

PATTERN_YEAR_MYPAGE = r'<p class="attrgroup">.*\n\s*<span><b>(199\d{1}|20[0-1][0-9]) [a-zA-Z0-9][a-zA-Z0-9 -]*<\/b><\/span>'

PATTERN_MILES = r'(\d{4,6}|\d{1,3}\,*\w{3}|\d{1,3}\s*[kK])\s*[Mm]iles'

PATTERN_ODOMETER = r'<span>odometer: <b>(\d{4,6})<\/b>'

#page_limit=2
#count=1
#while count <= page_limit :

print '-----------------------------------------'
print 'Getting data for ', mymake, mymodel
print '-----------------------------------------'
#print 'Analyzing search page: ', url


req = urllib2.Request(url, None, headers)
page = urllib2.urlopen(req)
html_str = page.read()

#page = urllib.urlopen(url)
#html_str = page.read()

all = re.findall(PATTERN_SEARCH, html_str)

'''
text_file = open("Output.txt", "w")
text_file.write("%s" % html_str)
text_file.close()
'''

for mline in all:
    
    myurl = 'https://'+ city + '.craigslist.org'+mline[2]+'/cto/'+ mline[3] + '.html'
    link.append(myurl)
    mypage = urllib.urlopen(myurl)
    myhtml_str = mypage.read()
    
    m = re.search(PATTERN_YEAR , mline[4])
    if m :
        year.append(m.group(1))
    #print m.group(1)
    else :
        mm = re.search(PATTERN_YEAR_MYPAGE, myhtml_str)
        if mm :
            year.append(mm.group(1))
        #print 'Found: ', mm.group(1)
        else :
            print '[Skip] YEAR not found:  ', myurl
            continue

    #print mline
    postdate.append(mline[1])
    pid.append(mline[3])
    #print mline[2]
    title.append(mline[4])
    price.append(mline[5])
    
    ml = re.search(PATTERN_MILES ,myhtml_str, flags=re.I)
    if ml :
        mile = ml.group(1)
        mile = mile.replace(' ' , '')
        mile = mile.replace(',' , '')
        mile = mile.replace('x' , '0')
        mile = mile.replace('X' , '0')
        mile = mile.replace('k' , '000')
        mile = mile.replace('K' , '000')
        miles.append(mile)
        print 'Miles = ', mile
    else:
        ml = re.search(PATTERN_ODOMETER, myhtml_str)
        if ml :
            mile = ml.group(1)
            mile = mile.replace(' ' , '')
            mile = mile.replace(',' , '')
            mile = mile.replace('x' , '0')
            mile = mile.replace('X' , '0')
            mile = mile.replace('k' , '000')
            mile = mile.replace('K' , '000')
            miles.append(mile)
            print 'Miles = ', mile
        else :
            miles.append('NA')
            print 'MILES not found : ',myurl
    clstate.append(state)
    clcity.append(city)
    make.append(mymake)
    model.append(mymodel)
    y = random.random(2,6)
    time.sleep(y)

rows = len(pid)
print "add total number = ", rows

alist = []

for i in range(rows):
    alist.append([pid[i], postdate[i], clcity[i], clstate[i], make[i], model[i], year[i], price[i], miles[i], link[i], title[i] ])

with open("CAR_PRICE.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(alist)


'''
    count += 1
    next = re.search(PATTERN_NEXT, html_str)
    if next:
        #print next.group(1)
        url = 'https://'+ city + '.craigslist.org/search/cto' + next.group(1) +'&hasPic=1'+ max_year + min_year + '?query=' + keyword
        #print nexturl
        #problem: CL doesn't show the right search result for the 2nd page using the above url
    else:
        print 'No more next page or Exceeds page limit. Terminate.'
        count = page_limit + 100
'''







map(int, price)
#intlist = [int(x) for x in stringlist]













'''
PATTERN = r'(<a href="\/cto\/)(\d{10}).+result-title hdrlnk">([\w\d\s\-\*]+)<\/a>'
all = re.findall(PATTERN, html_str)
for mline in all:
    print mline
    pid.append(mline[1])
'''


'''
line = page.readline()
while line != '':
    m = re.search(r'(\s*)(<time class)=', line)
    if m:
        print m.group(2) , ' FOUND IN ', line
    line = page.readline()
'''

