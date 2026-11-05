from django.urls import path
from school import views

urlpatterns = [
    path("giorni/", views.DayOfTheWeekListView.as_view(), name="day_list"),
    path("giorni/<int:pk>/", views.DayOfTheWeekDetailView.as_view(), name="day_detail"),
    path("giorni/nuovo/", views.DayOfTheWeekCreateView.as_view(), name="day_create"),
    path("giorni/<int:pk>/modifica/", views.DayOfTheWeekUpdateView.as_view(), name="day_update"),
    path("aule/", views.ClassroomListView.as_view(), name="classroom_list"),
    path("aule/<int:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("corsi/", views.CourseListView.as_view(), name="course_list"),
    path("corsi/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("corsi/nuovo/", views.CourseCreateView.as_view(), name="course_create"),
    path("corsi/<int:pk>/modifica/", views.CourseUpdateView.as_view(), name="course_update"),
    path("corsi/<int:pk>/elimina/", views.CourseDeleteView.as_view(), name="course_delete"),
]
