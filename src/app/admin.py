from django.contrib import admin
from .models import ServiceRequest, Specialist


admin.site.register(Specialist)
admin.site.register(ServiceRequest)