from django.db import models


# Person may need 2 swubtypes - Buyer and Seller
class Person(models.Model):
    pass


class Seller(models.Model):
    pass


class Buyer(models.Model):
    pass


class Sale(models.Model):
    pass


class Vehicle(models.Model):
    # Vehicle details
    pass


class Email(models.Model):
    pass
    # These are the details the web site owner should receive when a sale is agreed.
    # vehicle details
    # seller's details
    # sale price
    # The name of the interested party
    # The mobile number of the interested party
    # The Dodgy Brothers commission (5%) in dollars
    # The net amount that is transferrable to the seller
