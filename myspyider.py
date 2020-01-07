#http://hueyanchen.myweb.hinet.net/test.html
#https://elearning.ncyu.edu.tw
#https://elearning.ncyu.edu.tw/1072/
#http://xss-quiz.int21h.jp/
#https://en.wikipedia.org/wiki/The_Matrix
#https://killer0001.blogspot.com/2017/12/3-python.html
#http://120.113.173.21/
#https://www.php.net/manual/en/tutorial.firstpage.php
#http://www.eyny.com/
#https://www.pcparty.com.tw/
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import requests
#import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def SimulatedLogin(nurl, firstopenfile):
    driver = webdriver.Chrome("./chromedriver")
    #driver.implicitly_wait(10)
    print("Simulated's nurl= ", nurl)
    driver.get(nurl)
    
    fp = open("password.txt", "r+", encoding = "utf-8")
    password = fp.read()
    fp.close()
    
    fp = open("username.txt", "r+", encoding = "utf-8")
    usrname = fp.read()
    fp.close()
    
    
    try:
        usr = driver.find_element_by_name("username")
        usr.clear()
        usr.send_keys(usrname)
    
        pwd = driver.find_element_by_name("password")
        pwd.clear()
        pwd.send_keys(password)
    
        usr.send_keys(Keys.RETURN)
        time.sleep(4)
        print("------------------------------------------------------------------")

        tag_href = driver.find_elements_by_xpath("//a[@href]")
        if (firstopenfile == 1):
            fp = open("tag-href-http(s).txt", "w", encoding = "utf-8")
            fp.close()
        
        #temp1 = 1
        do = 0  #check where to find tag      ///do=>0 no find
        for out in tag_href:
            #print ("find simulated url= ", temp1, out.get_attribute("href"))
            furl = out.get_attribute("href")
            do = 1   
            fp = open("tag-href-http(s).txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close()
            
            if (furl[4] != 's'):
                furl = furl[:4] + 's' + furl[4:]
                #print("fixed simulated url= ", temp1, furl)
            
            #temp1 = temp1 + 1#####################################################################
                
                
            if (len(furl)>=len(URLL)):
                    #print("furl >= URL")
                    canAppend = 1
                    mm = 0
                    for mm in range(len(URLL)-1):                            # 把不是此網頁的 URL 給去除掉  URLL為 URL修正過後的新URL
                        if (furl[mm] != URLL[mm]):
                            mm = 0
                            canAppend = 0
                            break
                            #do not append to new_urls
                    if (canAppend == 1):
                        mm = 0
                        #print("ADD")
                        buffer1_new_urls.append(furl)
                
            else:   #len(furl)<len(URL)
                    #print("furl < URL")
                canAppend = 1
                mm = 0
                for mm in range(len(furl)-1):
                    if (furl[mm] != URLL[mm]):
                        mm = 0
                        canAppend = 0
                        break
                    #do not append to new_urls
                if (canAppend == 1):
                    mm = 0
                    #print("ADD")
                    buffer1_new_urls.append(furl)
                    
        #os.system("pause")
        ''''目前在找完該頁的all url 但經過過濾後是錯誤的URL'''
        #jjj = 1
        #for k in range(len(buffer1_new_urls)):
            #print(jjj, "not sort url= ", buffer1_new_urls[k])
            #jjj = jjj + 1
        #os.system("pause")
        
        
        
        a = set(buffer1_new_urls).difference(set(alreadyfind_urls)) # 把此網頁的 URL 把可能和以前找過 URL 給刪除 並把裡面剩下有重複的刪除
        b = list(a)
    
        q = 0
        for q in range(len(b)):
            privous_new_urls.append(b[q])
                              
        buffer2_new_urls = list(set(privous_new_urls))    
        for q in range(len(buffer2_new_urls)):
            buffer3_new_urls.append(buffer2_new_urls[q])
            
        a = set(buffer3_new_urls).difference(set(alreadyfind_urls)) # 把此網頁的 URL 把可能和以前找過 URL 給刪除 並把裡面剩下有重複的刪除
        b = list(a)
            
        q = 0
        for q in range(len(b)):
            new_urls.append(b[q])
            
        
        #test_for_alreadySearch()
        
        if (do == 1):
            do = 0
            print("finish to find simulated's herf-http(s)...")
            print("------------------------------------------------------------------")
        else:
            do = 0
            print("not find simulated's href-http(s) tag")
            print("------------------------------------------------------------------")
            
        #os.system("pause")
        
        tag_input = driver.find_element_by_tag_name("input")
        print("tag_input", tag_input)
        #os.system("pause")
        
        if (firstopenfile == 1):
            fp = open("tag-input.txt", "w", encoding = "utf-8")
            fp.close()
            
        do = 0
        for out in tag_input:
            do = 1
            print ("out", str(out))
            fp = open("tag-input.txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close()
        #os.system("pause")
        
        if (do == 1):
            do = 0
            print("finish to find input...")
            print("------------------------------------------------------------------")
            print("start to check login...")
            fp = open("tag-input.txt", "r", encoding = "utf-8")
            loginStr = str(fp.read())
            if ((loginStr.find("username")>-1)):
                if (loginStr.find("password")>-1):
                    do = 0
                    #SimulatedLogin(nurl, firstopenfile)#################################################
                    print("find login page...")
            else:
                print("not find login page")
                print("--------------------------------------------------------------")
                

            #os.system("pause")
        else:
            do = 0
            print("not find input tag")
            print("------------------------------------------------------------------")
        
    except:
        print("i can't not find username and password tag!!!!")
        print("find other's URL")
        #os.system("pause")
    driver.close()
    
def test_for_alreadySearch():
    k = 0
    jjj = 1
    for k in range(len(new_urls)):
        print(jjj,"searched=",new_urls[k])
        jjj += 1
    os.system("pause")
    

def get_url(nurl, firstopenfile):
    print("------------------------------------------------------------------")
    req = requests.get(nurl)
    req.encoding = "utf-8" 
    
    if (req.status_code == requests.codes.ok): #check website where is good
        print("this web is ok : ",req.status_code)
        print("header = ",req.headers['Content-Type'])
        print("finish to check web status...")
        print("------------------------------------------------------------------")
            
        fp = open("Static-Soup.txt", "w", encoding = "utf-8")
        soup = BeautifulSoup(req.text, "lxml")
        fp.write(soup.prettify())
        print("finish to write testStati-Soupc.txt...")
        fp.close()
        print("------------------------------------------------------------------")
        print("\n")
        
        tag_href = soup.find_all('a')
        
        if (firstopenfile == 1):
            fp = open("tag-href-http(s).txt", "w", encoding = "utf-8")
            fp.close()
        do = 0  #check where to find tag      ///do=>0 no find
        for out in tag_href:
            do = 1   
            fp = open("tag-href-http(s).txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close()
            
            furl = urllib.parse.urljoin(nurl, out.get('href'))      #把找到那一頁的 url 的格式填寫完整
            
            #print(furl)
            if (furl[4] != 's'):
                furl = furl[:4] + 's' + furl[4:]
            
            #print(furl)
            #print("furl= ", furl)
            #print("URL= ", URLL)

            if (len(furl)>=len(URLL)):
                #print("furl >= URL")
                canAppend = 1
                mm = 0
                for mm in range(len(URLL)-1):                            # 把不是此網頁的 URL 給去除掉
                    if (furl[mm] != URLL[mm]):
                        mm = 0
                        canAppend = 0
                        break
                        #do not append to new_urls
                if (canAppend == 1):
                    mm = 0
                    #print("ADD")
                    buffer1_new_urls.append(furl)
            
            else:   #len(furl)<len(URL)
                #print("furl < URL")
                canAppend = 1
                mm = 0
                for mm in range(len(furl)-1):
                    if (furl[mm] != URLL[mm]):
                        mm = 0
                        canAppend = 0
                        break
                        #do not append to new_urls
                if (canAppend == 1):
                    mm = 0
                    #print("ADD")
                    buffer1_new_urls.append(furl)
                
                
            '''
            canAppend = 1
            mm = 0
            for mm in range(len(URL)-1):                            # 把不是此網頁的 URL 給去除掉
                if (furl[mm] != URL[mm]):
                    mm = 0
                    canAppend = 0
                    break
                    #do not append to new_urls
            if (canAppend == 1):
                mm = 0
                buffer1_new_urls.append(furl)
            '''

        a = set(buffer1_new_urls).difference(set(alreadyfind_urls)) # 把此網頁的 URL 把可能和以前找過 URL 給刪除 並把裡面剩下有重複的刪除
        b = list(a)

        q = 0
        for q in range(len(b)):
            privous_new_urls.append(b[q])
                          
        buffer2_new_urls = list(set(privous_new_urls))    
        for q in range(len(buffer2_new_urls)):
            buffer3_new_urls.append(buffer2_new_urls[q])
            
        a = set(buffer3_new_urls).difference(set(alreadyfind_urls)) # 把此網頁的 URL 把可能和以前找過 URL 給刪除 並把裡面剩下有重複的刪除
        b = list(a)
        
        q = 0
        for q in range(len(b)):
            new_urls.append(b[q])
            
            
        #test_for_alreadySearch()
        
            
        if (do == 1):
            do = 0
            print("finish to find herf-http(s)...")
            print("------------------------------------------------------------------")
        else:
            do = 0
            print("not find href-http(s) tag")
            print("------------------------------------------------------------------")
        
        tag_form = soup.find_all('form')
        if (firstopenfile == 1):
            fp = open("tag-form.txt", "w", encoding = "utf-8")
            fp.close()
            
        do = 0
        for out in tag_form:
            do = 1
            fp = open("tag-form.txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close() 
        if (do == 1):
            do = 0
            print("finish to find form...")
            print("------------------------------------------------------------------")
        else:
            do = 0
            print("not find form tag")
            print("------------------------------------------------------------------")
                     
        tag_href = soup.find_all('link')
        if (firstopenfile == 1):
            fp = open("tag-link.txt", "w", encoding = "utf-8")
            fp.close()
            
        do = 0
        for out in tag_href:
            do = 1   
            fp = open("tag-link.txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close()
        if (do == 1):
            do = 0
            print("finish to find link...")
            print("------------------------------------------------------------------\n")
        else:
            do = 0
            print("not find link tag")
            print("------------------------------------------------------------------\n")
            
            
        tag_input = soup.find_all('input')
        if (firstopenfile == 1):
            fp = open("tag-input.txt", "w", encoding = "utf-8")
            fp.close()
            
        do = 0
        for out in tag_input:
            do = 1
            
            fp = open("tag-input.txt", "a", encoding = "utf-8")
            fp.write(str(out))
            fp.write(changeline)
            fp.close()
        if (do == 1):
            do = 0
            print("finish to find input...")
            print("------------------------------------------------------------------")
            print("start to check login...")
            fp = open("tag-input.txt", "r", encoding = "utf-8")
            loginStr = str(fp.read())
            if ((loginStr.find("username")>-1)):
                if (loginStr.find("password")>-1):
                    do = 0
                    SimulatedLogin(nurl, firstopenfile)#################################################
                    print("find login page...")
            else:
                print("not find login page")
                print("--------------------------------------------------------------")
                

            #os.system("pause")
        else:
            do = 0
            print("not find input tag")
            print("------------------------------------------------------------------")
            
    else : #check website where is not good
        
        print(req.status_code)
        print("this web is no ok")
        #print(req.raise_for_status())
        
################################################################# here is main

fp = open("getTestURL.txt", "r+", encoding = "utf-8")    #get testURL
URL = fp.read()
URLL = URL
fp.close()
       
#print(URL)
#print(URLL)
rr = 0
nn = 0
for rr in range(len(URLL)):
    if (URLL[rr] == '/'):
        nn = nn + 1
        if (nn >= 3):         
            nns = rr + 1
            substr = URLL[:nns]
            URLL = substr
            break
#print("new URL= ", URLL)
#os.system("pause")



firstOpenfile = 1     
new_urls = [URL]        #存放找到 且 是此網頁下的 URL
buffer1_new_urls = []       #存放還沒爬到的 URL
buffer2_new_urls = []       #存放還沒爬到的 URL
buffer3_new_urls = []
privous_new_urls = []
alreadyfind_urls = []   #存放已經爬過的 URL
alreadyfind_urls.append(new_urls[0])
num = 0
changeline = '\n'
goto2 = 0 #run > 1 times
ggg = 0
while (len(new_urls) > 0):
    num += 1
    if (goto2 != 0):
        
        if (len(new_urls) != 0):
            
            print("new_urls=",len(new_urls))
            new_url = new_urls.pop()
            alreadyfind_urls.append(new_url)
            print(num,"new_url=", new_url)
            #os.system("pause")
            #print(num,"current url=", new_url)
            #print("888888")#########################################
            firstOpenfile = 0
            fp = open("allURL.txt", "a", encoding = "utf-8")
            #fp.write(str(ggg)+" ")
            ggg += 1
            fp.write(new_url)
            fp.write(changeline)
            fp.close()
            get_url(new_url, firstOpenfile)
        else:
            #print("22222finish to spider!!!")
            break
        
        
    else:   #len(alreadyfind_urls) == 0
        goto2 = 1
        print("new_urls=",len(new_urls))
        new_url = new_urls.pop()
        print(num,"new_url=", new_url)
        if (num == 1):
            firstOpenfile = 1
            #print("77777")#########################################
            fp = open("allURL.txt", "w", encoding = "utf-8")
            #fp.write(str(ggg)+" ")
            ggg += 1
            fp.write(new_url)
            fp.write(changeline) #'\n'
            fp.close()
            
            get_url(new_url, firstOpenfile)
    
    if ggg == 20:
        sys.exit(0)

print("finish to spider!!!")
sys.exit(0)
########################################## end to spider

   