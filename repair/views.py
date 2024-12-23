from django.shortcuts import render
from .models import Device, Client, Repair

def home(request):
    return render(request, 'repair/repair_home.html')

def devices(request):
    devices = Device.objects.all()
    return render(request, 'repair/devices.html', {'devices': devices})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'repair/clients.html', {'clients': clients})

def repairs(request):
    repairs = Repair.objects.all()
    return render(request, 'repair/repairs.html', {'repairs': repairs})
