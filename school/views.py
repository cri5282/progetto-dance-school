from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from school.models import DayOfTheWeek, Classroom, Course


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek


class DayOfTheWeekCreateView(CreateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    success_url = reverse_lazy("day_list")


class DayOfTheWeekUpdateView(UpdateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    success_url = reverse_lazy("day_list")


class ClassroomListView(ListView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseUpdateView(UpdateView):
    model = Course
    fields = ["subject", "starting_hour", "day_of_the_week", "classroom", "school"]
    success_url = reverse_lazy("course_list")


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course_list")
