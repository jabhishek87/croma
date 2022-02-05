from django.urls import include, re_path
from .views import SaltCreate, SaltEdit, get_salt_id


urlpatterns = [
	re_path(r'^api/', include("salt_master.api.urls"), name = "salt-api"),
	re_path(r'^create$', SaltCreate, name = "create"),
	re_path(r'^(?P<pk>\d+)/edit', SaltEdit, name = "edit"),

	#AJAX
	re_path(r'^ajax/get_salt_id$', get_salt_id, name = "get_salt_id"),
]
