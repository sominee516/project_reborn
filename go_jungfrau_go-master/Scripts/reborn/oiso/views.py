from django.shortcuts import render
from os import name
from django.http import request
from django.test import TestCase
import pandas as pd
import csv
import json
import html
from django.shortcuts import render

from front00.models import apt_info
from .models import apt_geo
from .models import apt_sil

#아파트 상세정보를 불러오겠습니다.
# geojson 가져오기 :: 폴리곤 그림 구 테두리
with open('oiso/static/json/gu1953.geojson',encoding='utf-8') as json_file:
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
def main(request): 
    
    a_sil_list=[]

    aptJson_geo = json.dumps(apt_geo_list, ensure_ascii=False)

    if request.method == 'GET':
        for i,apt_cont in enumerate(apt_sil_list):
            if (apt_cont['name'] == '힐탑더블시티'):
                print(apt_cont)
                a_sil_list.append(apt_cont)

            aptJson_sil = json.dumps(a_sil_list)  
        return render(request, 'main.html',{'aptJson_sil':aptJson_sil,'aptJson_geo':aptJson_geo})
    
    elif request.method == 'POST':
        a_sil_list=[]
        print(request )
        print("호호")
        a_name = request.POST.get('a_name',None)
        # a_name_json = json.load(a_name)
        print(a_name)

        for i,apt_cont in enumerate(apt_sil_list):
            a =+ 1
            if (apt_cont['code'] == a_name):
                
                print(apt_cont)
                a_sil_list.append(apt_cont)
             


  
        aptJson_sil = json.dumps(a_sil_list)


        return render(request, 'main.html',{'aptJson_sil':aptJson_sil,'aptJson_geo':aptJson_geo})    
