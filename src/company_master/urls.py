from django.urls import include, re_path
from .views import *


urlpatterns = [
	re_path(r'^api/', include("company_master.api.urls"), name = "company-api"),
	re_path(r'^create$', CompanyCreate, name = "create"),
	re_path(r'^(?P<pk>\d+)/edit', CompanyEdit, name = "edit"),

	re_path(r'^supplier/create$', SupplierCreate, name = "create"),
	re_path(r'^supplier/(?P<pk>\d+)/edit', SupplierEdit, name = "edit"),

	#AJAX
	re_path(r'^ajax/get_company_id$', get_company_id, name = "get_company_id"),
	re_path(r'^ajax/get_supplier_id$', get_supplier_id, name = "get_supplier_id"),
	re_path(r'^ajax/get_company_info$', get_company_info, name = "get_company_info"),

]