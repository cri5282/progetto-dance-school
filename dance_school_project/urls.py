from django.contrib import admin
from django.urls import path

from dance_school_project import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("chi-siamo/", views.chi_siamo, name="chi_siamo"),
    path("admin/", admin.site.urls),
]
