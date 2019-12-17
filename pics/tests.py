from django.test import TestCase
from .models import location,Category,Image

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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.one=Category(name='Travel')
        self.two=Category(name='Destination')
    def test_instance(self):
        self.assertTrue(isinstance(self.one,Category))
    def test_save(self):
        self.one.save_category()
        cat=Category.objects.all()
        self.assertTrue(len(cat)>0)
    def test_delete(self):
        self.two.save_category()
        self.one.delete_category()
        cats=Category.objects.all()
        self.assertTrue(len(cats)>0)