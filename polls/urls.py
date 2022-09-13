#!/usr/bin/env python
# coding=utf-8
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
   # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    #path('', views., name='index'),
    path('<int:question_id>', views.detail, name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>', views.detail, name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/results', views.results, name='results')
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('student/',views.student, name='student'),
    path('pyecharts/',views.pyecharts, name='pyecharts'),
    #url('student/', views.student),
]
