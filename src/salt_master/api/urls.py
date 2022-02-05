from django.urls import include, re_path
from .views import *


urlpatterns = [
	re_path(r'^list/$', SaltListApiView.as_view(), name = "list"),
]
