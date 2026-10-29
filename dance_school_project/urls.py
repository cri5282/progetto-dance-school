from django.contrib import admin
from django.urls import include, path

from dance_school_project import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("chi-siamo/", views.chi_siamo, name="chi_siamo"),
    path("gestione-scuole/", include("schoolmanagement.urls")),
    path("configurazione/", include("school.urls")),
    path("admin/", admin.site.urls),
]
