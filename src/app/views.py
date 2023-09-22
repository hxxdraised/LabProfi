from django.shortcuts import render
from app import data


def home_page(request):
    return render(request, "home.html")

def services_list_page(request):
    return render(request, "service_select.html", {"specialists": data.specialists})

def service_page(request, id):
    return render(request, "service_info.html", {"specialist": data.specialists[id]})