from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from schoolmanagement.models import School


def lista_scuole(request):
    scuole = School.objects.all()
    return render(request, "schoolmanagement/school_list.html", {"scuole": scuole})


def dettaglio_scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    return render(request, "schoolmanagement/school_detail.html", {"scuola": scuola})


class SchoolCreateView(CreateView):
    model = School
    fields = ["name", "street", "city", "province", "zip_code", "country",
              "website", "phone", "email", "vat"]
    success_url = reverse_lazy("lista_scuole")


class SchoolUpdateView(UpdateView):
    model = School
    fields = ["name", "street", "city", "province", "zip_code", "country",
              "website", "phone", "email", "vat"]
    success_url = reverse_lazy("lista_scuole")


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("lista_scuole")
