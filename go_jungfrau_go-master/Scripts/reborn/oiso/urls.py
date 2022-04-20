from django.urls import path
from . import views, tests

urlpatterns = [
    path('', views.main, name='main'),
    path('test2/', tests.test2, name='test2'), # 아파트마커+클러스터+폴리곤보이기만
    
]