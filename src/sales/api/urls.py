from django.urls import include, re_path
from .views import *


urlpatterns = [
	re_path(r'^party-list/$',	PartyListApiView.as_view(), name = "party-list"),
	re_path(r'^doctor-list/$',	DoctorListApiView.as_view(), name = "doctor-list"),
]
