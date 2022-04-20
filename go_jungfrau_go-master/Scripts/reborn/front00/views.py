from django.shortcuts import render
import json
from .models import metro, apt_geo, Jung
from django.db import connections
from os import name
from django.http import request
from django.test import TestCase
import pandas as pd
import json
from front00.models import apt_info
from .models import apt_geo
from .models import apt_sil


# Create your views here.
ls = []


def geo_test(request):
    # json파일 열기
    with open('front00/static/json/gu1953.geojson',encoding='utf-8') as json_file:
        gu_features = json.load(json_file)['features']
    gu_polygon = []
    for i in range(len(gu_features)):
        gu_dict = {
            "gu_name" : gu_features[i]['properties']['SGG_NM'],
            "gu_code" : gu_features[i]['properties']['ADM_SECT_C'],
            "gu_geo_list" : gu_features[i]['geometry']['coordinates']
        }
        gu_polygon.append(gu_dict)
    guJson = json.dumps(gu_polygon, ensure_ascii=False)
    return render(request, 'geo_test.html', {'guJson':guJson})  

def metro_test(request):
    metro_q = metro.objects.all()
    metro_l = []
    for m in metro_q:
        metro_d = {
            "name":(m.name),
            "lat":(m.lat),
            "lng":(m.lng)
        }
        metro_l.append(metro_d)
        
    metroJson = json.dumps(metro_l, ensure_ascii=False)
    return render(request, 'metro_test.html',{'metroJson':metroJson})

def apt_test(request):
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
    # print(aptJson)
    return render(request, 'apt_test.html',{'aptJson':aptJson})

# Create your views here.
# ls = []
# def test(request):
#     li = pd.DataFrame()
#     # csv를 들고옵니다
#     with open('front00/static/csv/jiga_jisu_year.csv',encoding='utf-8') as csvfile:
#         rr = csv.reader(csvfile)
#         for i in rr:
#             # print (i)
#             ls.append(i)
#     # print(ls[5][2])
#     gu = pd.DataFrame(ls)
#     print(gu)
#     # df = pd.read_csv('front00/static/csv/jiga_jisu_year.csv')
#     # print(df)


#     return render(request,'test.html')

    # li = pd.DataFrame()
    # # csv를 들고옵니다
    # with open('front00/static/csv/jiga_jisu_year.csv',encoding='utf-8') as csvfile:
    #     rr = csv.reader(csvfile)
    #     for i in rr:
    #         # print (i)
    #         ls.append(i)
    # # print(ls[5][2])
    # gu = pd.DataFrame(ls)
    # print(gu)
    # # df = pd.read_csv('front00/static/csv/jiga_jisu_year.csv')
    # # print(df)


    # return render(request,'test.html')



#아파트 상세정보를 불러오겠습니다.
# geojson 가져오기 :: 폴리곤 그림 구 테두리
with open('front00/static/json/gu1953.geojson',encoding='utf-8') as json_file:
    gu_features = json.load(json_file)['features']
gu_list = []
for i in range(len(gu_features)):
    # 딕셔너리에 모아보자
    gu_dict = {
        "gu_name" : gu_features[i]['properties']['SGG_NM'],
        "gu_code" : gu_features[i]['properties']['ADM_SECT_C'],
        "gu_geo_list" : gu_features[i]['geometry']['coordinates']
    }
    gu_list.append(gu_dict)
guJson = json.dumps(gu_list, ensure_ascii=False)

# 아파트 지오 테이블 가져오기
apt_geo_table = apt_geo.objects.all() # 내 컴퓨터 테이블 중복때문에
apt_geo_list = []
for a in apt_geo_table:
    apt_geo_dict = {
        "code":a.apt_code,
        "title":a.apt_latest,
        "lat":a.apt_lat,
        "lng":a.apt_lng
    }
    apt_geo_list.append(apt_geo_dict)
aptJson_geo = json.dumps(apt_geo_list, ensure_ascii=False)

# 아파트 실거래가 테이블 가져오기
apt_sil_table = apt_sil.objects.all()
apt_sil_list = []
for a in apt_sil_table:
    apt_sil_dict = {
        "code" : a.apt_code,
        "name" : a.apt_name,
        "year" : a.apt_year,
        "price" : a.apt_price
    }
    apt_sil_list.append(apt_sil_dict)
aptJson_sil = json.dumps(apt_sil_list, ensure_ascii=False)

# 아파트 상세정보 테이블 가져오기
apt_info_table = apt_info.objects.all()
apt_info_list = []
for a in apt_info_table:
    apt_info_dict = {
        "code":a.apt_code,
        "name":a.apt_name,
        "since":a.apt_since,
        "pop":a.apt_pop
    }
    apt_info_list.append(apt_info_dict)
aptJson_info = json.dumps(apt_info_list, ensure_ascii=False)





# Create your views here.
def tests(request): 
    
    apt_navi_sil=[]
    apt_navi_info=[]
    
    aptJson_geo = json.dumps(apt_geo_list, ensure_ascii=False)

    if request.method == 'GET':
        for i,apt_cont in enumerate(apt_sil_list):
            if (apt_cont['name'] == '힐탑더블시티' ):
                print(apt_cont)
                apt_navi_sil.append(apt_cont)

        aptJson_sil = json.dumps(apt_navi_sil)

        for i,apt_cont in enumerate(apt_info_list):
            # print(apt_cont)
            if (apt_cont['name'] == '힐탑더블시티'):
                print("호호")
                print(apt_cont) 
                apt_navi_info.append(apt_cont)
        
                aptJson_info = json.dumps(apt_cont) 

        print(aptJson_info[0])

        return render(request, 'main_test.html',{'aptJson_sil':aptJson_sil,'aptJson_geo':aptJson_geo,'aptJson_info':aptJson_info})
    
    elif request.method == 'POST':
        print(request )
        
        a_name = request.POST.get('a_name',None)
        # a_name_json = json.load(a_name)
        print(a_name)

        for i,apt_cont in enumerate(apt_sil_list):
            
            if (apt_cont['code'] == a_name):
                
                print(apt_cont)
                apt_navi_sil.append(apt_cont)

        aptJson_sil = json.dumps(apt_navi_sil)

        for i,apt_cont in enumerate(apt_info_list):
            if (apt_cont['code'] == a_name):
                print("호호")
                print(apt_cont) 
                # apt_navi_info.append(apt_cont)
                aptJson_info = json.dumps(apt_cont) 

        return render(request, 'main_test.html',{'aptJson_sil':aptJson_sil,'aptJson_geo':aptJson_geo,'aptJson_info':aptJson_info})    
