#   execfile('re_search_model_pages.py')
import re
import urllib
import urllib2
import math
import csv
import numpy as np
import random
import time

nextpageflag = 0

#mymodel='test'
city = 'sfbay'
state = 'CA'

#mymake='ford'
#mymodellist=['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition']
#for mymodel in mymodellist:


mymake = 'honda' #'toyota'
mymodel = 'accord' #'camry'
keyword = mymake + '+' + mymodel

min_year='&min_auto_year=1997'
max_year='&max_auto_year=2017'

url = 'https://'+ city + '.craigslist.org/search/cto?query=' + keyword + '&hasPic=1' + min_year + max_year

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30'

headers = {'User-Agent': user_agent}

#https://sfbay.craigslist.org/search/cto?query=toyota+camry&hasPic=1&min_auto_year=1997&max_auto_year=2017
#https://sfbay.craigslist.org/search/cto?s=120&hasPic=1&max_auto_year=2017&min_auto_year=1997&query=toyota%20camry

url = 'https://sfbay.craigslist.org/search/cto?s=240&hasPic=1&max_auto_year=2017&min_auto_year=1997&query=honda%20accord'


PATTERN_SEARCH = r'(<time class=).+(\d{4}-\d{2}-\d{2}) .*\n\n\s+<a href="(\/*\w*)\/cto\/(\d{10}).+result-title hdrlnk">([\w\d\s\-\*\$\.!:\'\,\(\)]+)<\/a>\n\n\s+<span.+\n\s+<span.*\$([0-9]+)<\/span>'

PATTERN_NEXT = r'<link rel="next" href="https\:\/\/\w+\.craigslist\.org\/search\/cto(\?s=\d{3,4})&'

PATTERN_YEAR = r'.*(199\d{1}|20[0-1][0-9]).*'

PATTERN_YEAR_MYPAGE = r'<p class="attrgroup">.*\n\s*<span><b>(199\d{1}|20[0-1][0-9]) [a-zA-Z0-9][a-zA-Z0-9 -]*<\/b><\/span>'

PATTERN_MILES = r'(\d{4,6}|\d{1,3}\,*\w{3}|\d{1,3}\s*[kK])\s*[Mm]iles'

PATTERN_MILEAGE = r'[Mm]ileage\s*\:*\s*(\d{4,6}|\d{1,3}\,*\w{3}|\d{1,3}\s*[kK])'

PATTERN_ODOMETER = r'<span>odometer: <b>(\d{4,6})<\/b>'

PATTERN_RANGE = r'class="rangeFrom">(\d{1,4})<\/span>\n\s*-\n\s+<span class="rangeTo">(\d{1,4})<\/span>\n\s*<\/span>\n\s+\/\n\s+<span class="totalcount">(\d{1,4})<\/span>'

PATTERN_NEXT_LINK = r'<a href="([0-9a-zA-Z =\/\&_\%\;\?]+)" class="button next" '

#page_limit=2
#count=1
#while count <= page_limit :

print '-----------------------------------------'
print ' Getting data for ', mymake, mymodel
print '-----------------------------------------'


while (nextpageflag == 0) :
    
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
    
    print 'Now analyzing search page: '
    print url
    req = urllib2.Request(url, None, headers)
    page = urllib2.urlopen(req)
    html_str = page.read()

    #######################
    
    all = re.findall(PATTERN_SEARCH, html_str)
    wrongcount = 0
    
    for mline in all:
        
        y = random.uniform(15,36)
        time.sleep(y)
        
        if re.search(mymake, mline[4], flags=re.I) and re.search(mymodel, mline[4], flags=re.I) :
            print '+',
        else :
            wrongcount += 1
            if wrongcount > 10:
                print '- Exceed max wrong counts, break'
                break
            else:
                continue
        #check price
        myprice = int(mline[5])
        if myprice > 100000 or myprice < 500:
            print '[Skip] price out of range'
            continue
        
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
        else:
            ml = re.search(PATTERN_MILES, myhtml_str, flags=re.I)
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
                ml = re.search(PATTERN_MILEAGE, myhtml_str, flags=re.I)
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
                    print '[Skip] MILES not found :', myurl
                    continue

        # append information
        postdate.append(mline[1])
        pid.append(mline[3])
        title.append(mline[4])
        price.append(myprice)
        clstate.append(state)
        clcity.append(city)
        make.append(mymake)
        model.append(mymodel)


    # save data of this page
    rows = len(pid)
    print "Add total number = ", rows
    
    alist = []
    
    for i in range(rows):
        alist.append([pid[i], postdate[i], clcity[i], clstate[i], make[i], model[i], year[i], price[i], miles[i], link[i], title[i] ])
        
    with open("CAR_PRICE.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(alist)

    # check next page url
    page_range = re.search(PATTERN_RANGE, html_str)

    if page_range:
        print 'Done Results:', page_range.group(1), '-', page_range.group(2), 'out of', page_range.group(3)
        print '--------------------------------------'
        rangeFrom = int(page_range.group(1))
        rangeTo = int(page_range.group(2))
        totalcount = int(page_range.group(3))

        if rangeTo < totalcount:
            nextpageflag = 0
            next = re.search(PATTERN_NEXT_LINK, html_str)
            if next:
                #print next.group(1)
                href = next.group(1)
                href = href.replace('&amp;', '&')
                url = 'https://'+ city + '.craigslist.org' + href
            else :
                print '--- Link of next page not found, break.'
                break
        else :
            print 'Last page reached'
            nextpageflag = 1
    else :
        print 'Page range error, break'
        break

    time.sleep(80)










#map(int, price)
#intlist = [int(x) for x in stringlist]




