from django.db import models

# Create your models here.


class metro(models.Model):
    line = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    doro = models.CharField(max_length=100)
    beonji = models.CharField(max_length=100)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.lat

    def __str__(self):
        return self.name
        


class default(models.Model): 
    ## 여기에 데이터베이스 모델 내용~~ 
    class Meta: 
        managed = False 
        app_label = "default"


class Jung(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=38, decimal_places=9)
    lng = models.DecimalField(max_digits=38, decimal_places=9)

    class Meta:
        managed = False
        app_label = "Jung"
        db_table = 'JUNG_LATLNG'
    def __str__(self):
        return self.name

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
