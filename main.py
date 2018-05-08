import requests
from bs4  import BeautifulSoup
import csv

def urlg(query,pageno):


        p=pageno-1
        return "https://www.coursera.org/courses?languages=en&query="+query+"&start=" + str(p*20) +"&userQuery="+query

def lastpage(s):
    ss=s.find('div',"pagination-controls-container")
    sss=ss.findAll('button')
    return int(sss[-2].text)

def degrees(s) :
    w.writerow(['','','','',''])
    ss=s.find('div',"rc-DegreesUpsell")
    sss=ss.findAll('div')
    print (ss.h3.text+" : "+'\n')
    i=0
    while i<len(sss) :
        i=i+5
        t1=str(sss[i].text)
        print(t1 +':')
        i=i+1
        t2=str(sss[i].p.text)
        print(t2 +'\n')
        i=i+1
        w.writerow(['Degrees / Certificates',t1,t2,'',''])
    return len(sss)/7

def courses(s1,d) :

        ss1=s1.find('div',"rc-SearchResults bt3-col-xs-9")
        sss=ss1.findAll('div')
        #print(str(len(sss))+'\n')
        del(sss[0:9])
        del(sss[0])
        d=int(d)*7
        #print(str(d)+'\n')
        del(sss[0:d])
        del(sss[0])
        del(sss[-1])
        del(sss[-1])
        del(sss[-1])
        i=0

        while i<len(sss):
            courselink = "https://www.coursera.org" +sss[i].a.get('href')
            print(courselink)
            i=i+5
            coursetitle=sss[i].h2.text
            print(coursetitle)
            i=i+1
            s4=sss[i].findAll('span')
            if len(s4)==1:
                ty="course"
                spc=''
                provider=s4[0].text
            else :
                ty='specialisation'
                provider=s4[3].text
                spc=s4[0].text
            w.writerow([ty,coursetitle,courselink,provider,spc])
            i=i+2



query = str(input("Enter course name "))
    #query.replace(' ','-')
with open(query+'course details.csv','w') as outputfile :
    w =csv.writer(outputfile)
    w.writerow(['Course Type','Course Title','Course Summary','Provider','specialisation'])
    print (urlg(query,1)+'\n')
    #r=requests.get(url(query,0))
    #s=BeautifulSoup(r.text,'lxml')
    #print ("lastpage : "+str(lastpage(s))
    url = urlg(query,1)
    print(url)
    r=requests.get(url)
    print('requests done')
    s=BeautifulSoup(r.text,'lxml')
    print("BeautifulSoup done ")
    lp=lastpage(s)
    print("last page = "+str(lp))
    d=degrees(s)
    w.writerow(['','','','',''])
    w.writerow(['','','','',''])
    w.writerow(['','','','',''])
    courses(s,d)
    n=2

    while n <20 :
     url = urlg(query,n)
     r=requests.get(url)
     s=BeautifulSoup(r.text,'lxml')
     courses(s,d)
     n=n+1
     print('\n')
     print('\n')
     print(str(n))
     print('\n')
     print('\n')


print("not an infinity loop")
