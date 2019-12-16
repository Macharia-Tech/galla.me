from django.test import TestCase
from .models import location

class locationTestClass(TestCase):
    # set up method
    def setUp(self):
        self.london=location(location_name = 'London')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.london,location))

    # testing Save method
    def test_save_method(self):
        self.london.save_location()
        locations=location.objects.all()
        self.assertTrue(len(locations)> 0)