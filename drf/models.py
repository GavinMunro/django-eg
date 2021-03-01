from django.db import models


# Person may need 2 swubtypes - Buyer and Seller
class Person(models.Model):
    """ Customer details - name phone number etc. """
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=16)
    email = models.CharField(max_length=80)
    dob = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_email(self):
        return self.email
    
    def __repr__(self):
        return self.name + ' is added.'


class Seller(Person):
    """ Details applicable only to a user selling a vehicle. """
    pass


class Buyer(Person):
    """ Details applicable only to a user buying a vehicle. """
    pass


class Vehicle(models.Model):
    # Vehicle details
    make: models.CharField(max_length=32)
    model: models.CharField(max_length=32)
    year: models.DateField()


class Sale(models.Model):
    sale_price: models.DecimalField(decimal_places=2)



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


