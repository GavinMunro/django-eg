from django.test import TestCase
from ..models import Vehicle


class VehicleTest(TestCase):
    """ Unit test for Vehicle model - creation of 2 vehicle objects """
    def setUp(self):
        Vehicle.objects.create(
            id=1, vin='JXA5430-1ACB29653-476', rego='TGU973', make='Toyota', model='Camry', year='2008'
        )
        Vehicle.objects.create(
            id=2, vin='VX943184-JB2346-A2', rego='HVS246', make='Holden', model='Commodore', year='2004')
    
    def test_car_store(self):
        # Fist unit test - creation of Vehicle objects
        toyota = Vehicle.objects.get(vin='JXA5430-1ACB29653-476')
        holden = Vehicle.objects.get(vin='VX943184-JB2346-A2')
        self.assertEqual(
            toyota.get_make(), "TGU973 is a Toyota")
        self.assertEqual(
            holden.get_make(), "HVS246 is a Holden")
