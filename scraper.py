import requests
from bs4  import BeautifulSoup
import csv
import time
import random
from selenium import webdriver

user_agent_list = [
#Chrome
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#Firefox
'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)']

def coursecrapper(courselink,errorlinks) :
    #courselink = courselink1+"?action=enroll&authMode=login"
    courseralink="https://www.coursera.org/"
    print(courselink)
    browser.get(courselink)
    html=browser.execute_script("return document.body.innerHTML")
    s=BeautifulSoup(html,'lxml')
    pricing=" "

    try :
        title=s.find('h1','title display-3-text').text
    except :
        errorlinks.append(courselink)
        print("error")
        return


    #print("title : "+str(title))
    #print("--------------------------------------")
    try :
        about=s.find('p',"body-1-text course-description").text
    except :
        about = " "
    #print("about : "+str(about))
    #print("--------------------------------------")
    try :
        target_audience=s.find('div',"target-audience-section").p.text
    except :
        target_audience = " "
    #print("target audience : "+target_audience)
    #print("--------------------------------------")
    try :
        created_by=s.find('div',"headline-1-text creator-names").findAll('span')
        created_by=created_by[1].text
    except :
        created_by=" "
    #print("created by : "+created_by)
    #print("-------------------------------")
    ss=s.find_all('div',"rc-InstructorInfo")
    instructor_details = " "
    for si in ss :
        sss=si.find('span')
        instructor_link=courseralink+ sss.a.get('href')
        #instructor_name=sss.a.text
        s4=sss.text
        s4=list(s4)
        s4=''.join(s4)
        instructor=s4
        #instructor_bio=sss.find('div',"instructor-bio caption-text color-accent-brown").text
        try :
            instructor_bio=si.find('div',"instructor-bio caption-text color-accent-brown").text
        except :
            instructor_bio=" "
        #print("instructor : "+instructor)
        #print("instructor profile : "+instructor_link)
        #print("instructor bio : "+instructor_bio)
        #print("-------------------")
        instructor_details1=instructor+"\n"+instructor_bio+"\n"+instructor_link
        instructor_details=instructor_details + "\n"+instructor_details1
    ss=s.find('div',"rc-BasicInfo")
    sss=ss.findAll('tr')
    #print("length of sss"+str(len(sss)))

    basicinfo="N/A"
    specialisationlink="N/A"
    level="N/A"
    duration="N/A"
    language="N/A"
    howtopass="N/A"
    review="N/A"
    hardware="N/A"

    for i in sss :
        rowtitle = i.find('span',"td-title").text
        #print(rowtitle)
        if rowtitle=='Basic Info':
            #print("if working")
            s5=i.find('td','td-data')
            basicinfo=s5.text
            specialisationlink=courseralink + s5.a.get('href')
        if rowtitle == 'Level':
            s5=i.find('td',"td-data")
            level=s5.text
        if rowtitle == 'Commitment' :
            s5=i.find('td',"td-data")
            duration = s5.text
        if rowtitle ==  'Language':
            s5=i.find('td',"td-data")
            language=s5.text
        if rowtitle == 'How To Pass' :
            s5=i.find('td',"td-data")
            howtopass=s5.text
        if rowtitle == 'User Ratings':
            s6=i.find('div',"ratings-text bt3-hidden-xs")
            s7=s6.text.split('See')
            s7='. See'.join(s7)
            s8 = s6.a.get('href')
            s8=courseralink+s8
            review=s7+' : '+s8
        if rowtitle=="Hardware Req" :
            s5=i.find('td',"td-data")
            hardware=s5.text
    syllabus = "syllabus : \n"
    ss=s.find_all('div','week')
    for si in ss :

        s1=si.find('div',"week-heading body-2-text")
        details=s1.text + " :" +"\n"
        s1=si.find('div',"module-name headline-2-text")
        details =details + s1.text +"\n"
        try :
            s1=si.find('div',"summary horizontal-box")
            s1=s1.text.split('expand')[0]
        except :
            s1=" "
        details=details + s1 +"\n"
        s1=si.find('div',"rc-TogglableContent").text
        details =details + s1 +"\n"
        details=details+"\n"
        syllabus=syllabus+details

    #print("basic info :"+basicinfo)
    #print("specialisationlink :"+specialisationlink)
    #print("level :"+level)
    #print("duration :"+duration)
    #print("language :"+language)
    #print("how to pass :"+howtopass)
    #print("review :"+review)
    #print("hardware :"+hardware)
    print("--------------------------------------------------------")
    #print("syllabus : \n" + str(syllabus))
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    #courselink = courselink1+"?action=enroll&authMode=login"
    courseralink="https://www.coursera.org/"
    #browser.get(courselink)

    #r = browser.execute_script("return document.body.innerHTML")

    #s=BeautifulSoup(r,'lxml')


    try :
        ss=s.find('div',"startdate rc-StartDateString caption-text").text
        startdate = ss
    except :
        startdate = "no start date "

    #print("ssssssssssssssssssssssssssssssssssssssss")
    #print("cost : "+cost)
    #print("ssssssssssssssssssssssssssssssssssssssss")


    url = courselink+"?action=enroll&authMode=login"
    print(url)
    browser.get(url)
    #html=browser.execute_script("return document.body.innerHTML")
    #html=browser.execute_script("return document.body.innerHTML")
    #sets=BeautifulSoup(html,'lxml')
    #setss=sets.find('span',class_='rc-ReactPriceDisplay')
    #print(str(setss))

    wc.writerow([title,courselink,about,target_audience,created_by,instructor_details,basicinfo+"\n"+specialisationlink,level,startdate,duration,language,howtopass,review,hardware,syllabus,pricing])
    print (courselink + "succesfully scraped")


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
        k=0
        while i<len(sss):
            errorlinks=[]
            courselink = "https://www.coursera.org" +sss[i].a.get('href')
            #print(courselink)
            i=i+5
            coursetitle=sss[i].h2.text
            #print(coursetitle)
            i=i+1
            s4=sss[i].findAll('span')
            print("----------------")
            if len(s4)==1:

                ty="course"
                spc=''
                provider=s4[0].text

                coursecrapper(courselink,errorlinks)
                print(n,k)
                k=k+1
                #l1=courselink+"?action=enroll&authMode=login"
                #browser.get(l1)
                #html = html=browser.execute_script("return document.body.innerHTML")
                #soup=BeautifulSoup(html,'lxml')
                #soups=s.find('span',class_='rc-ReactPriceDisplay')
                #print(str(soups))
                #cost = soups.text
                #print(cost)

            else :
                ty='specialisation'
                provider=s4[3].text
                spc=s4[0].text
            w.writerow([ty,coursetitle,courselink,provider,spc])
            i=i+2

        print(errorlinks)

def correction(l):
    l1=[]
    for i in l :
        for i in range(1,6):
        #Pick a random user agent
            user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        url = urlg(query,i)
        #r=requests.get(url)
        r = requests.get(url,headers=headers)
        print('requests done')
        s=BeautifulSoup(r.text,'lxml')
        print("BeautifulSoup done ")
        courses(s,0,l1,i)
    return l1

query = " "
         #query.replace(' ','-')
print("code running")
with open(query+'course details.csv','w') as outputfile :
  with open("courses only.csv",'a') as coursesonlyfile :
    browser=webdriver.Chrome("/home/abhi/Desktop/coursera scrapper/chromedriver")
    browser.maximize_window()
    url="https://www.coursera.org/?authMode=login"
    browser.get(url)#"?action=enroll&authMode=login"
    username = browser.find_element_by_id("emailInput-input") #username form field
    password = browser.find_element_by_id("passwordInput-input") #password form field
    username.send_keys('abhinavreddynimma1@gmail.com')
    password.send_keys('*********')
    button = browser.find_element_by_css_selector('.Button_clbp6a-o_O-primary_cv02ee-o_O-md_1jvotax.w-100')
    button.click()

    wc=csv.writer(coursesonlyfile)
    wc.writerow(["Course Title","Course Link","About","Target Audience","Creators","Instructor Details","Basic Info","Level","Start Date","Duration","Language","How to Pass","Review","Hardware Required","Syllabus","Pricing"])

    print("file opened")
    w =csv.writer(outputfile)
    w.writerow(['Course Type','Course Title','Course Summary','Provider','specialisation'])


    print ("url = "+urlg(query,1)+'\n')
    #r=requests.get(url(query,0))
    #s=BeautifulSoup(r.text,'lxml')
    #print ("lastpage : "+str(lastpage(s))
    url = urlg(query,1)
    #print(url)
    for i in range(1,6):
    #Pick a random user agent
        user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url,headers=headers)
    #r=requests.get(url)

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
    n=81

    while n < lp+1:
     print('\n')
     print('\n')
     print(str(n))
     print('\n')
     print('\n')
     url = urlg(query,n)
     print("URL generated")
     #r=requests.get(url)
     for i in range(1,6):
     #Pick a random user agent
         user_agent = random.choice(user_agent_list)
     headers = {'User-Agent': user_agent}
     r = requests.get(url,headers=headers)
     print('requests done')
     s=BeautifulSoup(r.text,'lxml')
     print("BeautifulSoup done ")

     #sleep(r)
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
