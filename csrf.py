import requests
import re
import os
import sys
from lxml import html
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs

fp = open("csrf.txt","w", encoding = "utf-8") #把以前的紀錄清除 初始化
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

def find_lcsubstr(s1, s2): 
	m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，為方便後續計算，比字串串長度多了一列
	mmax=0   #最長匹配的長度
	p=0  #最長匹配對應在s1中的最後一位
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i]==s2[j]:
				m[i+1][j+1]=m[i][j]+1
				if m[i+1][j+1]>mmax:
					mmax=m[i+1][j+1]
					p=i+1
	return s1[p-mmax:p]   #返回最長子串&長度

"""上面是function"""


#下面是我寫的 csrf referer   
#testURL = "https://xss-quiz.int21h.jp/"
#testURL = "https://anewstip.com/accounts/login/"

fp_allURL = open("allURL.txt", "r+", encoding = "utf-8")
#is_referer 用來辨識 此網站有referer的問題
is_referer = 1
is_referer_array = []

while True:
    testURL = fp_allURL.readline()
    testURL = testURL.strip()
    rightURL = testURL

    #flag1 flag2 用來辨識 此網站是不是要先處理登入才能測試
    needLogin = 0
    needEmail = 0
    #fp.close()
    if not testURL:
        fp_allURL.close()
        
        fp1 = open("csrf.txt", "a", encoding= "utf-8")
        fp1.write("~結束~\n")
        fp1.close() #結束整個csrf程式
        
        print("allURL.txt are all tested!!! END")
        #sys.exit(0)
        break

    print("目前從 allURL.txt 讀出來的 url 為:", testURL)

    if (connetion_is_ok(testURL)):
        #確認 URL 狀態為 200 開始進行檢測 csrf

        #建立一個 session
        same_id = requests.Session()
        GetHtmlResponse = same_id.get(testURL)
        #print(GetHtmlResponse.request.headers)

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

                fp = open("username.txt", "r+", encoding= "utf-8")
                mail = fp.read()
                fp.close()
                
        #print(needEmail)
        #print (needLogin)
        if (needLogin==1): #需要先登入
            if (needEmail==1): #帳號 是 用信箱
                data = {
                    "email" : mail,
                    "password" : password
                }
            if (needEmail==0): #帳號 不是 用信箱
                data = {
                    "username" : usrname,
                    "password" : password
                        }
        if(needLogin==0):
            data={}
            
        testURL = GetHtmlResponse.url # 原本的url因為要登入但未登入，所以被導向登入頁面的url，所以要更新url 變成登入的url
        response = same_id.post(testURL, data) #登入成功
        #開始解析原本要登入的url內的 input點 (如果要登入的話 這是處理完登入後，拿到新的且正確的html)
        soup = BeautifulSoup(response.text, "lxml")
        tag_form = soup.find_all('form')


        for out in tag_form:
            checknum = out['action']
        
        header = {
            "Referer" : "https://YOU/HAVE/CSRF"
        }
        #print(rightURL)
        check_status = same_id.post(rightURL,headers=header)
        #print(check_status.status_code)
        print(check_status.request.body)
        if (check_status.status_code == 200):
            is_referer = 0                          #有referer問題
            is_referer_array.append(is_referer)     #放入referer陣列內
        else :
            is_referer = 1                          #沒有referer問題
            is_referer_array.append(is_referer)     #放入referer陣列內
        print("-------------------")
for i in range(len(is_referer_array)):
    print(is_referer_array[i])
#token id 
print("--------------------------------------------")
fp_allURL = open("allURL.txt", "r+", encoding = "utf-8")
referer_len = 0  # referer list 長度
while True:
    testURL = fp_allURL.readline()
    testURL = testURL.strip()
    #testURL = 'https://anewstip.com/accounts/login/'
    rightURL = testURL
    #fp_allURL.close()
    if not testURL:
        fp_allURL.close()
        
        print("allURL.txt are all tested!!! END")
        sys.exit(0)
        break
    print("目前從 allURL.txt 讀出來的 url 為:", testURL)
    check_list={ }  #build the list for token
    session_requests = requests.session()
    result = session_requests.get(testURL)
    tree = html.fromstring(result.text)
    sp = BeautifulSoup(result.text, "lxml")
    find_type = sp.find_all('input')
    chk = ""
    for i in find_type:
        #print(i['type'])
        if(i['type']=="hidden" and len(i['value']) == 32):
            chk = i['name']
    chk_token = 1
    if(chk !=""):
        authenticity_token = list(set(tree.xpath('//input[@name="' + chk + '"]/@value')))
        check_string=authenticity_token
        #print(check_string)
        #儲存&跟check_string配對
        for i in range (1,11):
            session_requests = requests.session()
            result = session_requests.get(testURL)
            tree = html.fromstring(result.text)
            authenticity_token = list(set(tree.xpath('//input[@name="' + chk + '"]/@value')))
            if(authenticity_token) :
                check_list[i]=authenticity_token
                #print(authenticity_token)
            else:
                chk_token = 0
                print("failed link\n")
                break
                
        lcs_string={}
        lcs_len={}
        if(chk_token == 1):
            for i in range (1,11):
                lcs_string[i]=find_lcsubstr(check_string , check_list[i])
                #print(lcs_string[i])
                lcs_len[i]=len(lcs_string[i])
        
    #判斷重複率
        if(lcs_string and chk_token == 1):
            for i in range(1 , 11):
                if(lcs_string[i] and chk_token == 1):
                    for j in range (1, 11):
                        if (lcs_string[i]==lcs_string[j+1] and j+1<11):
                            chk_token = 0
                        if(chk_token == 0):
                            break


    print (chk_token)
    print (is_referer_array[referer_len])
    if(chk_token == 0 and is_referer_array[referer_len] == 0):
        f_token = open("csrf.txt", "a", encoding= "utf-8")
        f_token.write("\n")
        f_token.write("他同時傭有token id 和referer欄位的問題!!!")
        f_token.write("\n")
        f_token.write("URL = ")
        f_token.write(rightURL)
        f_token.write("\n")
        f_token.write("可以藉由不同網域來訪問此網頁，駭客可誘導被害者點選可以執行此網頁不良動作的腳本來仿冒受害者")
        f_token.write("\n\n")
        f_token.write("\n")
        f_token.write("URL = ")
        f_token.write(rightURL)
        f_token.write("\n")
        f_token.write("token id 的更換率不高所以有可能會被猜中密碼. \n\n")
        f_token.close()
        referer_len = referer_len + 1
    elif(chk_token == 0 and is_referer_array[referer_len] == 1):
        f_token = open("csrf.txt", "a", encoding= "utf-8")
        f_token.write("\n")
        f_token.write("他傭有token id 的問題!!!")
        f_token.write("\n")
        f_token.write("URL = ")
        f_token.write(rightURL)
        f_token.write("\n")
        f_token.write("token id 的更換率不高所以有可能會被猜中密碼. \n\n")
        f_token.close()
        referer_len = referer_len + 1
    elif(chk_token == 1 and is_referer_array[referer_len] == 0):
        f_token = open("csrf.txt", "a", encoding= "utf-8")
        f_token.write("\n")
        f_token.write("他傭有referer欄位的問題!!!")
        f_token.write("\n")
        f_token.write("URL = ")
        f_token.write(rightURL)
        f_token.write("\n")
        f_token.write("可以藉由不同網域來訪問此網頁，駭客可誘導被害者點選可以執行此網頁不良動作的腳本來仿冒受害者")
        f_token.write("\n\n")
        f_token.close()
        referer_len = referer_len + 1
    elif(chk_token == 1 and is_referer_array[referer_len] == 1):
        f_token = open("csrf.txt", "a", encoding= "utf-8")
        f_token.write("他沒有任何問題!!!")
        f_token.write("\n")
        f_token.close()
        referer_len = referer_len + 1
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        