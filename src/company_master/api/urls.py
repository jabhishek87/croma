from django.urls import include, re_path
from .views import *


urlpatterns = [
	re_path(r'^chain-list/$', ChainListApiView.as_view(), name = "chain-list"),
	re_path(r'^company-list/$',	CompanyListApiView.as_view(), name = "company-list"),
	re_path(r'^supplier-list/$', SupplierListApiView.as_view(), name = "supplier-list"),
]
