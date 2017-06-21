#   execfile('re_search.py')
import re
import urllib
import urllib2
import math
import csv
import numpy as np

brands=14

#mymakelist = ['ford', 'cheverolet', 'chrysler', 'jeep', 'toyota', 'honda', 'nissan',  'mazda', 'mercedes', 'bmw', 'audi', 'vw', 'hyundai', 'kia']


#mymodellistlist = [ ['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition'], ['spark', 'cruze' ,'malibu','impala', 'taurus', 'trax', 'equinox', 'traverse', 'tahoe', 'suburban', 'camaro', 'corvette'], ['200', '300'], ['wrangler', 'compass', 'cherokee', 'renegade', 'patriot'], ['yaris' ,'corolla','camry', 'avalon', 'rav4', 'highlander', 'prius', 'sienna'], ['fit' ,'civic','accord', 'crv', 'pilot', 'hrv', 'prius', 'odssey'], ['versa', 'sentra' ,'altima','maxima', 'joke', 'rogue', 'murano', 'pathfinder'], ['3' ,'6','cx-3', 'cx-5', 'cx-9', 'mx-5'], ['c300' ,'c350','e320', 'e350', 'e500', 'e550', 'e400', 's500','s550','cla250', 'cls550', 'ml320','ml350' ], ['x1','x2','x3', 'x5', 'x6','328i' ,'328xi','335i', '335xi', '525i', '528i', '525xi', '528xi','545i','545xi', '550i', '550xi','750i', '750xi','750li'], ['a3' ,'a4','a5', 'a6', 'a7', 'a8', 's3', 'rs3','s7','rs7', 's8', 'q3','q5', 'q7','tt' ], ['jetta' ,'passat','cc', 'golf', 'tiguan', 'touareg', 'beetle' ], ['elantra' ,'sonata','azera', 'tucson', 'santafe', 'accent', 'veloster','genesis' ], ['optima' ,'soul','niro', 'sportage', 'sorento', 'cadenza', 'k900','rio','forte', 'sedona' ]]

#mymodel='test'
city = 'annarbor'
state = 'MI'

#for b in range(brands) :
    
    #mymake = mymakelist[b]
    
    #for mymodel in mymodellistlist[b] :

mymake='ford'
mymodellist=['fiesta' ,'focus','fusion', 'taurus', 'escape', 'edge', 'explorer', 'mustang', 'expedition']

for mymodel in mymodellist:
    
    keyword = mymake + '+' + mymodel

    min_year='&min_auto_year=1997'
    max_year='&max_auto_year=2017'

    url = 'https://'+ city + '.craigslist.org/search/cto?query=' + keyword + '&hasPic=1' + min_year + max_year

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    headers = {'User-Agent': user_agent}

    pid =[]
    link = []
    postdate = []
    title = []
    make = []
    model = []
    year = []
    price = []
    miles = []

    clstate = []
    clcity = []

    '''
    message = []
    transmisson = []
    color =[]
    condition = []
    titlestatus = []
    fuel = []
    '''
    #https://annarbor.craigslist.org/search/cto?query=Ford&hasPic=1&min_auto_year=1997&max_auto_year=2017
    #https://annarbor.craigslist.org/search/cto?s=120&hasPic=1&min_auto_year=1997&max_auto_year=2017?query=Ford&hasPic=1


    PATTERN_SEARCH = r'(<time class=).+(\d{4}-\d{2}-\d{2}) .*\n\n\s+<a href="\/cto\/(\d{10}).+result-title hdrlnk">([\w\d\s\-\*\$\.!:\'\,\(\)]+)<\/a>\n\n\s+<span.+\n\s+<span.*\$([0-9]+)<\/span>'

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

    for mline in all:
        
        myurl = 'https://'+ city + '.craigslist.org/cto/'+ mline[2] + '.html'
        link.append(myurl)
        mypage = urllib.urlopen(myurl)
        myhtml_str = mypage.read()
        
        m = re.search(PATTERN_YEAR , mline[3])
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
        pid.append(mline[2])
        #print mline[2]
        title.append(mline[3])
        price.append(mline[4])
        
        ml = re.search(PATTERN_MILES ,myhtml_str, flags=re.I)
        if ml :
            mile = ml.group(1)
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

    rows = len(pid)
    print "add total number = ", rows

    alist = []

    for i in range(rows):
        alist.append([pid[i], postdate[i], clcity[i], clstate[i], make[i], model[i], year[i], price[i], miles[i], link[i], title[i] ])

    with open("usedcars.csv", "a") as csvfile:
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

