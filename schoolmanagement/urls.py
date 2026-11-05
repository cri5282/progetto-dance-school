from django.urls import path
from schoolmanagement import views

urlpatterns = [
    path("", views.lista_scuole, name="lista_scuole"),
    path("<int:pk>/", views.dettaglio_scuola, name="dettaglio_scuola"),
    path("nuova/", views.SchoolCreateView.as_view(), name="school_create"),
    path("<int:pk>/modifica/", views.SchoolUpdateView.as_view(), name="school_update"),
    path("<int:pk>/elimina/", views.SchoolDeleteView.as_view(), name="school_delete"),
]
