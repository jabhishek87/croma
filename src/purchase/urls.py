from django.urls import include, re_path
from .views import *

urlpatterns = [
	re_path(r'^create/$', CreatePurchase.as_view(), name = "create"),
	re_path(r'^(?P<pk>\d+)$', RetrievePurchase, name = "detail"),
	re_path(r'^(?P<pk>\d+)/edit$', UpdatePurchase.as_view(), name = "edit"),
	#re_path(r'^(?P<pk>\d+)/delete$', DeleteSale, name = "delete"),
	re_path(r'^ajax/search_inv$', SearchInv, name = "SearchInv"),

	re_path(r'^ajax/delete_inv$', DeletePurchase, name = "DeletePurInv"),
	re_path(r'^ajax/checkSupplieNameInv$', checkSupplierNameInv, name="checkSupplierNameInv"),

]
