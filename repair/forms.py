from django import forms
from .models import Client, Device, Worker, SparePart, Repair

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['ID_Client', 'Name', 'Phone_number', 'Email', 'Address']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['ID_Device', 'ID_Client', 'Model', 'Manufacturer', 'Date_of_manufacture', 'Serial_number']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['ID_Worker', 'Name', 'Position', 'Phone_number', 'Email', 'Address']

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['ID_Spare_part', 'Name', 'Quantity_of_spare_parts', 'Price']

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['ID_repair', 'ID_Device', 'ID_Worker', 'ID_Spare_part', 'Date_of_receipt', 'End_date', 'Description_of_the_problem', 'Description_of_repair', 'Price']
