from django.shortcuts import render, get_object_or_404
from schoolmanagement.models import School


def lista_scuole(request):
    scuole = School.objects.all()
    return render(request, "schoolmanagement/school_list.html", {"scuole": scuole})


def dettaglio_scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    return render(request, "schoolmanagement/school_detail.html", {"scuola": scuola})
