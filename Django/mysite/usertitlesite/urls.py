from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^createTable/', views.createTable, name='createTable'),
    url(r'^addColumnToTable/', views.addColumnToTable, name='addColumnToTable'),
    url(r'^dropColumnInTable/', views.dropColumnInTable, name='dropColumnInTable'),
    url(r'^deleteTable/', views.deleteTable, name='deleteTable'),
    url(r'^insertDataToTable/', views.insertDataToTable, name='insertDataToTable'),
    url(r'^selectTable/', views.selectTable, name='selectTable'),
]
