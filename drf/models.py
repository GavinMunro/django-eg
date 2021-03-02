from django.db import models


class Vehicle(models.Model):
    """ Vehicle details """
    vin: models.CharField(max_length=64, null=False, primary_key=True)
    rego: models.CharField(max_length=6, null=False, unique=True)
    make: models.CharField(max_length=32, null=False)
    model: models.CharField(max_length=32, null=False)
    year: models.DateField(null=False)

    def get_rego(self):
        return self.rego

    def __repr__(self):
        return self.rego + ' is added.'
    

# Person may need 2 subtypes - Buyer and Seller
class Person(models.Model):
    """ Customer details - name phone number etc. """
    email = models.CharField(max_length=80, null=False, primary_key=True)
    firstname = models.CharField(max_length=32, null=False)
    lastname = models.CharField(max_length=32, null=False)
    mobile = models.CharField(max_length=16, null=False)

    dob = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_email(self):
        return self.email
    
    def __repr__(self):
        return self.email + ' is added.'


class Seller(Person):
    """ Details applicable only to a user selling a vehicle. """
    pass


class Buyer(Person):
    """ Details applicable only to a user buying a vehicle. """
    pass


class Ad(models.Model):
    seller: models.ForeignKey(Seller, on_delete=models.CASCADE, null=False, blank=False)
    vehicle: models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False)
    asking_price: models.DecimalField(decimal_places=2, null=False)


class Sale(models.Model):
    buyer: models.ForeignKey(Buyer, on_delete=models.CASCADE, null=False, blank=False)
    vehicle: models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False)
    sale_price: models.DecimalField(decimal_places=2)


# class Email(models.Model):
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
#


