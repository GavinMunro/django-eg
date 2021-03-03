from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person, Vehicle, Ad, Sale
from .serializers import PersonSerializer, VehicleSerializer, AdSerializer, SaleSerializer


def index(request):
    return render(request, 'index.html', {})


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single person
    if request.method == 'GET':
        return Response({})
    # delete a single person
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single person
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_people(request):
    # get all people
    if request.method == 'GET':
        return Response({})
    # insert a new record for a person
    elif request.method == 'POST':
        return Response({})


# def gen_email(models.Model):
#     """ These are the details the web site owner should receive when a sale is agreed.
#     vehicle details
#     seller's details
#     sale price
#     The name of the interested party
#     The mobile number of the interested party
#     The Dodgy Brothers commission (5%) in dollars
#     The net amount that is transferrable to the seller
#     """
#     pass  # This will be generated from existing fields and will be moved into a view.
