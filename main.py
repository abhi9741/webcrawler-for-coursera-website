import requests
from bs4  import BeautifulSoup
import csv
import time

def urlg(query,pageno):
        p=pageno-1
        #return "https://www.coursera.org/courses?languages=en&query="+query+"&start=" + str(p*20) +"&userQuery="+query
        return "https://www.coursera.org/courses?_facet_changed_=true&query="+query+"&start=" + str(p*20)

def lastpage(s):
    ss=s.find('div',"pagination-controls-container")
    sss=ss.findAll('button')
    return int(sss[-2].text)

def degrees(s) :
    w.writerow(['','','','',''])
    ss=s.find('div',"rc-DegreesUpsell")
    sss=ss.findAll('div')
    #print (ss.h3.text+" : "+'\n')
    i=0
    while i<len(sss) :
        i=i+5
        t1=str(sss[i].text)
        #print(t1 +':')
        i=i+1
        t2=str(sss[i].p.text)
        #print(t2 +'\n')
        i=i+1
        w.writerow(['Degrees / Certificates',t1,t2,'',''])
    return len(sss)/7

def courses(s1,d,l,n) :

        ss1=s1.find('div',"rc-SearchResults bt3-col-xs-9")
        try :
            sss=ss1.findAll('div')
        except :
            #print(str(s1)+'\n')
            #print(str(ss1)+'\n')
            print("error :"+str(n)+str(r))
            l.append(n)
            return
            #print(str(sss)+'\n')
        #print(str(len(sss))+'\n')
        del(sss[0:4])
        #del(sss[0])
        d=int(d)*7
        #print(str(d)+'\n')
        #del(sss[0:d])
        #del(sss[0])
        #del(sss[0])
        del(sss[-1])
        del(sss[-1])
        del(sss[-1])
        i=0

        while i<len(sss):
            courselink = "https://www.coursera.org" +sss[i].a.get('href')
            #print(courselink)
            i=i+5
            coursetitle=sss[i].h2.text
            #print(coursetitle)
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

def correction(l):
    l1=[]
    for i in l :
        url = urlg(query,i)
        r=requests.get(url)
        print('requests done')
        s=BeautifulSoup(r.text,'lxml')
        print("BeautifulSoup done ")
        courses(s,0,l1,i)
    return l1

query = " "
         #query.replace(' ','-')
print("code running")
with open(query+'course details.csv','w') as outputfile :
    print("file opened")
    w =csv.writer(outputfile)
    w.writerow(['Course Type','Course Title','Course Summary','Provider','specialisation'])


    print ("url = "+urlg(query,1)+'\n')
    #r=requests.get(url(query,0))
    #s=BeautifulSoup(r.text,'lxml')
    #print ("lastpage : "+str(lastpage(s))
    url = urlg(query,1)
    #print(url)
    r=requests.get(url)
    print('requests done')
    s=BeautifulSoup(r.text,'lxml')
    print("BeautifulSoup done ")
    lp=lastpage(s)
    print("last page = "+str(lp))
    d=0
    w.writerow(['','','','',''])
    w.writerow(['','','','',''])
    w.writerow(['','','','',''])
    l=[]
    courses(s,d,l,1)
    n=2

    while n < lp:
     print('\n')
     print('\n')
     print(str(n))
     print('\n')
     print('\n')
     url = urlg(query,n)
     print("URL generated")
     r=requests.get(url)
     print('requests done')
     s=BeautifulSoup(r.text,'lxml')
     print("BeautifulSoup done ")
     courses(s,d,l,n)
     n=n+1


        # l=[3, 16, 21, 57, 60, 65, 68, 104, 118, 119]
    print(len(l))
    print(l)
    print("not an infinity loop")
    print("correcting")
    l1=correction(l)
    print("correction done")
    print(l1)
    print(len(l1))
    print("-----------------------------")
    if len(l1)!=0:
        #sleep(100)
        l1=correction(l1)
        print(l1)
        print(len(l1))
    if len(l1)!=0:
        #sleep(100)
        l1=correction(l1)
        print(l1)
        print(len(l1))
