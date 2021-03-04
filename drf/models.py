from django.db import models


class Person(models.Model):
    """ Customer details - name phone number etc. """
    id: models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID')
    # id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=80, null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=32, null=False, blank=False)
    lastname = models.CharField(max_length=32, null=False, blank=False)
    mobile = models.CharField(max_length=16, null=False, blank=False)
    # dob = models.DateField()
    # updated_at = models.DateTimeField(auto_now=True)
    
    def get_email(self):
        return self.email
    
    def __repr__(self):
        return self.email + ' is added.'


# class Seller(Person):
#     """ Person subtype for details applicable only to a user selling a vehicle. """
#     pass
#
#
# class Buyer(Person):
#     """ Person subtype for details applicable only to a user buying a vehicle. """
#     pass


class Vehicle(models.Model):
    """ Vehicle details """
    id: models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID')
    # id = models.BigIntegerField(primary_key=True)
    vin: models.CharField(max_length=64, null=False, blank=False, unique=True)
    rego: models.CharField(max_length=6, null=False, blank=False, unique=True)
    make: models.CharField(max_length=32, null=False, blank=False)
    model: models.CharField(max_length=32, null=False, blank=False)
    year: models.IntegerField(max_length=4, null=False, blank=False)
    # If we didn't keep history and cars could only be advertised and sold once:
    # ad_by: models.ForeignKey(Person, on_delete=models.CASCADE)
    # sold_to: models.ForeignKey(Person, on_delete=models.CASCADE)
    # asking_price: models.DecimalField(decimal_places=2, null=False)
    # agreed_price: models.DecimalField(decimal_places=2, null=False)
    
    def get_vin(self):
        return self.vin
    
    def get_rego(self):
        return self.rego

    def get_make(self):
        return self.rego + ' is a ' + self.make
    
    def __repr__(self):
        return self.rego + ' is added.'


class Ad(models.Model):
    seller: models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    vehicle: models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False)
    asking_price: models.DecimalField(decimal_places=2, null=False)
    placed: models.DateField
    

class Sale(models.Model):
    buyer: models.ForeignKey(Person, on_delete=models.CASCADE, null=False, blank=False)
    vehicle: models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False)
    sale_price: models.DecimalField(decimal_places=2)
    bought: models.DateField
