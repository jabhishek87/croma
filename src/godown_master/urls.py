from django.conf.urls import url
from .views import GodownCreate

urlpatterns = [
	re_path(r'^create/$', GodownCreate, name = "create"),

]
