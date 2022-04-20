from os import name
from django.http import request
from django.test import TestCase
import pandas as pd
import csv
import json
import html
from django.shortcuts import render
from .models import metro, apt_geo
from .models import apt_sil
from django.http import HttpResponse,JsonResponse
# test_N(request)
# def test_N(request):
a_li=[]

count = 0
# # print(request)






apt_l = []
apt_q = apt_geo.objects.all()
# print(apt_q)
for a in apt_q:
    # print(a)
    apt_d = {
        "code":a.apt_code,
        "price":a.apt_latest,
        "lat":a.apt_lat,
        "lng":a.apt_lng
    }
    apt_l.append(apt_d)
    
aptJson_code = json.dumps(apt_l, ensure_ascii=False)
# # Create your tests here.

apt_list = []
apt_sil_q = apt_sil.objects.all()
for i in apt_sil_q:
    # print(A_price[1][i])
    # print(i)
    apt_data = {
        "code":i.apt_code,
        "name":i.apt_name,
        "year":i.apt_year,
        "price":i.apt_price,
        
    }
    apt_list.append(apt_data)

# print(apt_list)

ls=[]

# with open('front00/static/csv/Apart_price_year.csv',encoding='utf-8') as csvfile:
#     rr = csv.reader(csvfile)
#     for i in rr:
#         # print (i)
#         ls.append(i)
# # print(ls[0])
# # print(ls[1])
# # print(ls[1][0])
# A_price = pd.DataFrame(ls)
# print(A_price)
# print(ls[4064][2])




# print(apt_list)

    
# 클릭한 아파트 코드 받아오기

# def test_N(request):
#     a_li = []
#     print(request , "Navi")
#     for i,apt_cont in enumerate(apt_list):
#             if (apt_cont['dong'] == ('좌동') and apt_cont['name'] == 'SKVIEW'):
#                 print(apt_cont)
#                 a_li.append(apt_cont)

#             # print(len(a_li))

#             global apt_Json
#             apt_Json = json.dumps(a_li)
#     # return render(request, 'apt_test.html','aptJson':aptJson})
#     return render(request, 'text_Navi.html',{'apt_Json':apt_Json})
    # if request.method == 'GET':
    #     for i,apt_cont in enumerate(apt_list):
    #         if (apt_cont['dong'] == ('좌동') and apt_cont['name'] == 'SKVIEW'):
    #             print(apt_cont)
    #             a_li.append(apt_cont)

    #         # print(len(a_li))

    #         global apt_Json
    #         apt_Json = json.dumps(a_li)
    #     return render(request, 'apt_test.html',{'apt_Json':apt_Json})

    # elif request.method == 'POST':
    #     print(request )
    #     print("호호")
    #     a_name = request.POST.get('a_name',None)
    #     # a_name_json = json.load(a_name)
    #     print(a_name)

    #     for i,apt_cont in enumerate(apt_list):
    
    #         if (apt_cont['name'] == a_name):
    #             print(apt_cont)
    #             a_li.append(apt_cont)

    #     print(len(a_li))    
    #     apt_Json = json.dumps(a_li) 
    #     return render(request, 'apt_test.html',{'apt_Json':apt_Json})

# # <!-- {% include "text_Navi.html" %} -->

def apt_test(request):
    global apt_Json
    # test_N(request)
    # def test_N(request):
    a_li=[]

    # print(request)
    apt_q = apt_geo.objects.all()
    # print(apt_q)
    apt_l = []
    for a in apt_q:
        apt_d = {
            "name":a.name,
            "lat":a.lat,
            "lng":a.lng
        }
        apt_l.append(apt_d)
        
    aptJson = json.dumps(apt_l, ensure_ascii=False)
    # Create your tests here.
    # print(request)
    

    apt_q = apt_geo.objects.all()
    # print(apt_q)
    apt_l = []
    for a in apt_q:
        apt_d = {
            "name":a.name,
            "lat":a.lat,
            "lng":a.lng
        }
        apt_l.append(apt_d)
        
    # aptJson = json.dumps(apt_l, ensure_ascii=False)
    if request.method == 'GET':
        for i,apt_cont in enumerate(apt_list):
            if (apt_cont['dong'] == ('좌동') and apt_cont['name'] == 'SKVIEW'):
                print(apt_cont)
                a_li.append(apt_cont)

            # print(len(a_li))

            global apt_Json
            apt_Json = json.dumps(a_li)
        return render(request, 'apt_test.html',{'apt_Json':apt_Json,'aptJson':aptJson})

    # el
    if request.method == 'POST':
        print(request )
        print("호호")
        a_name = request.POST.get('a_name',None)
        # a_name_json = json.load(a_name)
        print(a_name)

        for i,apt_cont in enumerate(apt_list):
    
            if (apt_cont['name'] == a_name):
                print(apt_cont)
                a_li.append(apt_cont)

        print(len(a_li))    
        apt_Json = json.dumps(a_li)
        # print(a_li[5])
        # print(apt_Json[5])
        # return render(request, 'test.html', {'apt_Json':apt_Json})  
        # print(aptJson)
        return render(request, 'apt_test.html',{'aptJson':aptJson,'apt_Json':apt_Json})
# 메인지도
def test(request):
    global count
    
    # # test_N(request)
    # # def test_N(request):
    a_li=[]
    # apt_Json = 0
    # # print(request)
   

    apt_q = apt_geo.objects.all()
    # print(apt_q)
    # apt_l = []
    # for a in apt_q:
    #     apt_d = {
    #         "code":a.apt_code,
    #         "price":a.apt_latest,
    #         "lat":a.apt_lat,
    #         "lng":a.apt_lng
    #     }
    #     apt_l.append(apt_d)
     #url경로에 .py가 존재하는 폴더의 정의한 함수로 이동할 수 있을까?   
    aptJson_code = json.dumps(apt_l, ensure_ascii=False)

    if request.method == 'GET':
        for i,apt_cont in enumerate(apt_list):
            if (apt_cont['name'] == '힐탑더블시티'):
                print(apt_cont)
                a_li.append(apt_cont)

            # print((a_li))

            # print(apt_Json)
            apt_Json = json.dumps(a_li)
            # print(apt_Json)  
        return render(request, 'test.html',{'apt_Json':apt_Json,'aptJson':aptJson_code})
    
    elif request.method == 'POST':
        count += 1
        a = 0
        b = 0
        a_li=[]
        print(request )
        print("호호")
        a_name = request.POST.get('a_name',None)
        # a_name_json = json.load(a_name)
        print(a_name)

        for i,apt_cont in enumerate(apt_list):
            a =+ 1
            if (apt_cont['code'] == a_name):
                print(apt_cont)
                a_li.append(apt_cont)
                b += 1

        #print(len(a_li))    
        print(a,"for문 도는 횟수")
        print(b , "if문 도는 횟수")
        print(count , "POST 요청 횟수")
        apt_Json = json.dumps(a_li)


        # print(a_li)
        # r = html.unescape(a_li)
        # print(apt_Json)
        # return render(request, 'test.html', {'apt_Json':apt_Json})  
        # print(aptJson)
        # return HttpResponse({'aptJson':aptJson,'apt_Json':apt_Json})

        return render(request, 'test.html',{'apt_Json':apt_Json,'aptJson':aptJson_code})

        

#Navi 분리001
def test_c(request):

    return render(request,'test copy.html')

#Navi 분리002
# def test_N(request):
#     return render(request,'test_Navi.html')


    
# apt_Json = json.dumps(apt_list)
# print(apt_list[3]['name'])
# print(apt_Json[0])


# return render(request, 'test.html')

# ,{'apt_Json':apt_Json}
# print(li)
    # df = pd.read_csv('front00/static/csv/jiga_jisu_year.csv')
    # print(df)

# def apt_test(request):
#     apt_q = apt_geo.objects.all()
#     # print(apt_q)
#     apt_l = []
#     for a in apt_q:
#         apt_d = {
#             "name":a.name,
#             "lat":a.lat,
#             "lng":a.lng
#         }
#         apt_l.append(apt_d)
        
#     aptJson = json.dumps(apt_l, ensure_ascii=False)
#     # print(aptJson)
#     return (request, 'apt_test.html',{'aptJson':aptJson})
