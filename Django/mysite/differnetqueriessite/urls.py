from django.conf.urls import include, url

from . import views

urlpatterns = [

    url(r'^callUserCountProc/', views.callUserCountProc, name='callUserCountProc'),
    url(r'^callEmployeeDetailsProc/', views.callEmployeeDetailsProc, name='callEmployeeDetailsProc'),
    url(r'^getCurrentDayOrders/', views.getCurrentDayOrders, name='getCurrentDayOrders'),
    url(r'^getNumberOfProducts/', views.getNumberOfProducts, name='getNumberOfProducts'),
    url(r'^callSupplierDetailsProc/', views.callSupplierDetailsProc, name='callSupplierDetailsProc'),
    url(r'^callProductDetailsProc/', views.callProductDetailsProc, name='callProductDetailsProc'),
    url(r'^callBuyingPatternProc/', views.callBuyingPatternProc, name='callBuyingPatternProc'),

]
