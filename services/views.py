from django.shortcuts import render
from services.models import Service

# Create your views here.


def service(request):
    services = Service.objects.all()
    return render(request, 'services.html', {"services": services})

