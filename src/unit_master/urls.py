from django.urls import include, re_path
from .views import UnitCreate


urlpatterns = [
	re_path(r'^api/', include("unit_master.api.urls"), name = 'unit-api'),
	re_path(r'^create$', UnitCreate, name = "create"),

]