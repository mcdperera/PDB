
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^index/', views.index , name = 'index'),

    url(r'^admin/', admin.site.urls),
	url(r'^user/', include('usersite.urls')),
	url(r'^usertype/', include('usertypesite.urls')),
	url(r'^department/', include('departmentsite.urls')),
	url(r'^employee/', include('employeesite.urls')),
	url(r'^customer/', include('customersite.urls')),
	url(r'^supplier/', include('suppliersite.urls')),
	url(r'^producttype/', include('producttypesite.urls')),
	url(r'^product/', include('productsite.urls')),
	url(r'^productsupplier/', include('productsuppliersite.urls')),
	url(r'^order/', include('ordersite.urls')),
	url(r'^orderdetail/', include('orderdetailsite.urls')),
	url(r'^differnetqueries/', include('differnetqueriessite.urls')),
	url(r'^usertitle/', include('usertitlesite.urls')),
]
