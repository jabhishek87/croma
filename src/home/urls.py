from django.conf.urls import url
from .views import HomePage, takeBackup


urlpatterns = [
    re_path(r'^$', HomePage, name = "home"),
    re_path(r'ajax/backup', takeBackup, name = "takeBackup"),

]