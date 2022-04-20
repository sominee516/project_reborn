from django.urls import path, include
from . import views
from . import tests

urlpatterns = [
    path('aptt/', tests.apt_test, name='apt_test'),
    path('metrot/', views.metro_test, name='metro_test'),
    path('geot/',views.geo_test, name='geo_test'),
    path('maint/',tests.test,name='test..'), # 메인지도
    path('main/',views.tests),
    # path('testn/',tests.test_N,name='testn'),  # 일반네비
    # path('testn/<str:a_name>',tests.apt_test),  # 아파트네비
]
