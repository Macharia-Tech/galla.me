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
    # setup method
    def setUp(self):
        self.one=Category(name='Travel')
        self.two=Category(name='Destination')

        #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.one,Category))

        # testing save method
    def test_save(self):
        self.one.save_category()
        cat=Category.objects.all()
        self.assertTrue(len(cat)>0)

        #testing delete method
    def test_delete(self):
        self.two.save_category()
        self.one.delete_category()
        cate=Category.objects.all()
        self.assertTrue(len(cate)>0)