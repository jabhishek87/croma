from django.urls import include, re_path
from .views import *


urlpatterns = [
	re_path(r'^api/', include("sales.api.urls"), name = "sales-api"),
	re_path(r'^create/$', CreateSale.as_view(), name = "create"),
	re_path(r'^(?P<pk>\d+)$', RetrieveSale, name = "detail"),
	re_path(r'^(?P<pk>\d+)/edit$', UpdateSale.as_view(), name = "edit"),

	#ajax
	re_path(r'^view_invoice$', ViewInvoice, name = "ViewInvoice"),
	re_path(r'^print_invoice$', PrintInvoice, name = "PrintInvoice"),
	re_path(r'^ajax/search_inv$', SearchInv, name = "SearchInv"),

	re_path(r'^ajax/delete_inv$', DeleteSale, name = "DeleteSaleInv"),

#Doctor Crud System Urls
	re_path(r'^doctor/create$', DoctorCreate, name = "doctor_create"),
	re_path(r'^doctor/(?P<pk>\d+)/edit', DoctorEdit, name = "doctor_edit"),
	#AJAX
	re_path(r'^doctor/ajax/get_doctor_id$', get_doctor_id, name = "get_doctor_id"),
]
