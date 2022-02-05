from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^account/', include("accounts.urls", namespace = 'account')),
    re_path(r'^reports/', include("reports.urls", namespace = 'reports')),
	re_path(r'^sales/', include("sales.urls", namespace = 'sales')),
	re_path(r'^purchase/', include("purchase.urls", namespace = 'purchase')),
	re_path(r'^item/', include("item_master.urls", namespace = 'item')),
	re_path(r'^company/', include("company_master.urls", namespace = 'company')),
	re_path(r'^salt/', include("salt_master.urls", namespace = 'salt')),
	re_path(r'^godown/', include("godown_master.urls", namespace = 'godown')),
	re_path(r'^unit/', include("unit_master.urls", namespace = 'unit')),

	re_path(r'^', include("home.urls", namespace = 'home')),

]


