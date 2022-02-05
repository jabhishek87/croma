from django.urls import include, re_path

from .views import *

urlpatterns = [
    re_path(r'^register', register_view, name = "register_view"),
    re_path(r'^login', loginView.as_view(), name = "login"),
    re_path(r'^logout', logout_view, name = "logout"),
    re_path(r'^company/register', companyRegistrationView, name="company-register"),
    re_path(r'^session/expire', sessionExpireView.as_view(), name="sessionExpireView"),
]
