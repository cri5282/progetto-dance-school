from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def chi_siamo(request):
    return render(request, "about.html")
