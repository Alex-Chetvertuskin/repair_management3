from django.db import models
from django.utils import timezone

class Client(models.Model):
    ID_Client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Default Name')
    phone_number = models.CharField(max_length=20, default='Default Phone Number')
    email = models.EmailField(unique=True, default='default@example.com')
    address = models.CharField(max_length=100, default='Default Address')

    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return self.name

class Device(models.Model):
    ID_Device = models.AutoField(primary_key=True, db_column='ID_Device')
    ID_Client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='devices', db_column='ID_Client')
    model = models.CharField(max_length=100, db_column='Model')
    manufacturer = models.CharField(max_length=100, db_column='Manufacturer')
    date_of_manufacture = models.DateField(db_column='Date_of_manufacture')
    serial_number = models.CharField(max_length=100, db_column='Serial_number')

    class Meta:
        managed = False
        db_table = 'device'

    def __str__(self):
        return self.model

class Worker(models.Model):
    ID_Worker = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default='Default Phone Number')
    email = models.EmailField(unique=True, default='default@example.com')
    address = models.CharField(max_length=100, default='Default Address')

    class Meta:
        managed = False
        db_table = 'worker'

    def __str__(self):
        return self.name

class SparePart(models.Model):
    ID_Spare_part = models.AutoField(primary_key=True, db_column='ID_Spare_part')
    name = models.CharField(max_length=100, db_column='Name')
    quantity = models.IntegerField(db_column='Quantity_of_spare_parts')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='Price')

    class Meta:
        managed = False
        db_table = 'spare_part' 

    def __str__(self):
        return self.name


class Repair(models.Model):
    ID_repair = models.AutoField(primary_key=True, db_column='ID_repair')
    ID_Device = models.ForeignKey('Device', on_delete=models.CASCADE, db_column='ID_Device')
    ID_Worker = models.ForeignKey('Worker', on_delete=models.CASCADE, db_column='ID_Worker')
    ID_Spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE, db_column='ID_Spare_part')
    Date_of_receipt = models.DateField(default=timezone.now, db_column='Date_of_receipt')
    End_date = models.DateField(default=timezone.now, db_column='End_date')
    Description_of_the_problem = models.TextField(default='Default Description', db_column='Description_of_the_problem')
    Description_of_repair = models.TextField(default='Default Description', db_column='Description_of_repair')
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, db_column='Price')

    class Meta:
        managed = False
        db_table = 'repair'

    def __str__(self):
        return f"Repair for {self.ID_Device.model} by {self.ID_Worker.name}"
