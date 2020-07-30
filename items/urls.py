from django.contrib import admin
from django.urls import path, re_path
from items import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/items/$', views.items_list),
    re_path(r'^api/items/([0-9]+)$', views.items_detail),
]