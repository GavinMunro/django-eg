from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person, Vehicle, Ad, Sale
from .serializers import PersonSerializer, VehicleSerializer, AdSerializer, SaleSerializer
from .forms import CarForm, CustomerForm


def index(request):
    return render(request, 'index.html', {})


def new_cust(request, email):
    form = CustomerForm(request.POST)
    if form.is_valid():
        person = Person(
            email=form.cleaned_data["email"],
            firstname=form.cleaned_data["firstname"],
            lastname=form.cleaned_data["lastname"],
            mobile=form.cleaned_data["mobile"],
        )
        person.save()
    person = Person.objects.get(email=email)
    context = {
        "person": person,
        "form": form,
    }
    return render(request, "cust_detail.html", context)


def list_car(request, login):
    seller = Person.objects.get(id=login)
    
    form = CarForm(request.POST)
    if form.is_valid():
        car = Vehicle(
            vin=form.cleaned_data["vin"],
            rego=form.cleaned_data["email"],
            make=form.cleaned_data["firstname"],
            model=form.cleaned_data["lastname"],
            year=form.cleaned_data["mobile"],
        )
        car.save()
    cars = Vehicle.objects.get(seller=seller)
    context = {
        "seller": seller,
        "cars": cars,
        "form": form,
    }
    return render(request, "car_detail.html", context)

 
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
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)
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
