from django.contrib import admin
from .models import Client, Device, Worker, SparePart, Repair

admin.site.register(Client)
admin.site.register(Device)
admin.site.register(Worker)
admin.site.register(SparePart)
admin.site.register(Repair)
