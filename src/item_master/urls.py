from django.urls import include, re_path
from .views import *

urlpatterns = [
	re_path(r'^api/', include("item_master.api.urls"), name = "item-api"),
	re_path(r'^create/$', CreateItem.as_view(), name = "create"),
	re_path(r'^(?P<pk>\d+)$', RetrieveItem, name = "detail"),
	re_path(r'^(?P<pk>\d+)/edit$', UpdateItem.as_view(), name = "edit"),
	re_path(r'^ajax/search_item$', search_item, name = "search_item"),
	re_path(r'^ajax/get/item_batches$', get_item_batches, name = "get_item_batches"),
	re_path(r'^ajax/delete_item$', DeleteItem, name = "delete_item"),
	re_path(r'^ajax/search/item_info$', search_item_info, name = "search_item_info"),
]
