from django.test import TestCase
from .models import Client, Device, Worker, SparePart, Repair

class ClientModelTest(TestCase):
    def setUp(self):
        Client.objects.create(Name="John Doe", Phone_number="1234567890", Email="john@example.com", Address="123 Main St")

    def test_client_name(self):
        client = Client.objects.get(Name="John Doe")
        self.assertEqual(client.Name, "John Doe")