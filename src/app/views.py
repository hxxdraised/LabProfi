from django.shortcuts import render
from app.models import Specialist


def home_page(request):
    return render(request, "home.html")

def services_list_page(request):
    query = request.GET.get("q")
    if query:
        specialists = Specialist.objects.filter(name__icontains=query)
    else:
        specialists = Specialist.objects.all()
    return render(request, "service_select.html", {"specialists": specialists, "query": query})

def service_page(request, id):
    specialist = Specialist.objects.get(pk=id)
    return render(request, "service_info.html", {"specialist": specialist})