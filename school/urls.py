from django.urls import path
from school import views

urlpatterns = [
    path("giorni/", views.DayOfTheWeekListView.as_view(), name="day_list"),
    path("giorni/<int:pk>/", views.DayOfTheWeekDetailView.as_view(), name="day_detail"),
]
