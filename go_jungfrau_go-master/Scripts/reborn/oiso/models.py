from django.db import models

# Create your models here.

# 아파트 실거래가 테이블
class apt_sil(models.Model):
    apt_code = models.CharField(max_length=20)
    apt_name = models.CharField(max_length=100)
    apt_year = models.CharField(max_length=20)
    apt_price = models.CharField(max_length=50)

# 아파트 좌표 테이블
class apt_geo(models.Model):
    apt_code = models.CharField(max_length=20)
    apt_latest = models.CharField(max_length=100) 
    apt_lat = models.CharField(max_length=50)
    apt_lng = models.CharField(max_length=50)

# 아파트 상세정보 테이블
class apt_info(models.Model):
    apt_code = models.CharField(max_length=20)
    apt_name = models.CharField(max_length=100)
    apt_juso = models.CharField(max_length=300)
    apt_since = models.CharField(max_length=50)
    apt_pop = models.CharField(max_length=50)
