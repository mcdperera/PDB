from django.conf.urls import include, url

from . import views

urlpatterns = [

    url(r'^createtable/', views.createTable, name='createtable'),
    url(r'^inserttable/', views.insertTable, name='inserttable'),
    url(r'^selecttable/', views.selectTable, name='selecttable'),
    url(r'^deleterecords/', views.deleterecords, name='deleterecords'),
    url(r'^deletetable/', views.deleteTable, name='deletetable'),
]
