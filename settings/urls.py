from django.urls import path, include, re_path
from django.conf.urls import url
import settings
from django.contrib import admin
import content.views as views


admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", views.index, name="index"),
    path('rest/clients', views.clients),
    path('rest/clients/', views.clients),
    path('rest/client/<mac_address>', views.client),
    path('rest/client/<mac_address>/', views.client),
    path('rest/ps1installationscript/', views.installation_script),
    path("admin/", admin.site.urls),
    url(r'^([\s\S]*)$', views.web_resource),
]
