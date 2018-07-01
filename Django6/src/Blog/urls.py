'''
Created on 2018. 6. 30.

@author: kgitbank31
'''
from django.urls import path
from .views import *
app_name='Blog'
urlpatterns=[
    #클래스뷰.as_view() : 클래스 뷰가 URL 매칭시 사용
    path('',index.as_view(), name='index'),
    path('/<int:post_id>/',detail,name='detail'),
    path('posting/',posting,name='posting'),
    path('searchP/',searchP,name='searchP')
    ]