from django.views.generic import ListView, DetailView
from school.models import DayOfTheWeek


class DayOfTheWeekListView(ListView):
    model = DayOfTheWeek


class DayOfTheWeekDetailView(DetailView):
    model = DayOfTheWeek
