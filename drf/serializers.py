from rest_framework import serializers
from .models import Person, Vehicle, Ad, Sale  # , Seller, Buyer


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('email', 'firstname', 'lastname', 'mobile')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vin', 'rego', 'make', 'model', 'year')


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'vehicle', 'seller', 'asking_price')


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'vehicle', 'buyer', 'sale_price')

