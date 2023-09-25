from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from app.forms import RequestForm
from app.models import ServiceRequest, Specialist



def home_page(request):
    return render(request, "home.html")

def services_list_page(request):
    query = request.GET.get("q")
    if query:
        specialists = Specialist.objects.filter(name__icontains=query, is_active=True)
    else:
        specialists = Specialist.objects.filter(is_active=True)
    return render(request, "service_select.html", {"specialists": specialists, "query": query})

def service_page(request, id):
    specialist = Specialist.objects.get(pk=id)
    request_form = RequestForm()
    return render(request, "service_info.html", {"specialist": specialist, "request_form": request_form})


@login_required
def requests_list(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "requests_list.html", {"requests": requests})

@login_required
def send_request(request, id):
    form = RequestForm(request.POST)
    if form.is_valid():
        specialist = Specialist.objects.get(pk=id)
        service_request = ServiceRequest(user=request.user, comment=form.cleaned_data["comment"], specialist=specialist)
        service_request.save()
    return redirect(reverse('requests_list'))