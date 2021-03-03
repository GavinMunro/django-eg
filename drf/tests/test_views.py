import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Vehicle, Person, Ad, Sale
from ..serializers import PersonSerializer, VehicleSerializer, AdSerializer, SaleSerializer


# initialize the APIClient app
client = Client()
