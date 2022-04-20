from django.test import TestCase
from django.shortcuts import render
from .models import apt_geo, apt_info, apt_sil
import json

def test2(request):
    # geojson 가져오기
    with open('static/json/gu1953.geojson',encoding='utf-8') as json_file:
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
            "latest":a.apt_latest,
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
            "juso":a.apt_juso,
            "since":a.apt_since,
            "pop":a.apt_pop
        }
        apt_info_list.append(apt_info_dict)
    aptJson_info = json.dumps(apt_info_list, ensure_ascii=False)


    return render(request,'test2.html',{'guJson':guJson, 'aptJson_geo':aptJson_geo, 'aptJson_sil':aptJson_sil, 'aptJson_info':aptJson_info})

