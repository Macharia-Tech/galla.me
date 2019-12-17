from django.db import models

class location (models.Model):
    location_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length = 60)

    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()

class Image(models.Model):
    name=models.CharField(max_length=30)
    image_description=models.TextField()
    image_path=models.ImageField(upload_to='images/',blank=True)
    category=models.ForeignKey(Category,null=True)
    location=models.ForeignKey(Location,null=True)

    @classmethod
    def search(cls,search_term):
        categories=cls.objects.filter(category__name__icontains=search_term)
        return categories
    @classmethod
    def London(cls):
        london_images=cls.objects.filter(location__location_name='London')
        return london_images
    @classmethod
    def Amsterdam(cls):
        amsterdam_images=cls.objects.filter(location__location_name='Amsterdam')
        return china_images
    @classmethod
    def SouthAfrica(cls):
        southafrica_images=cls.objects.filter(location__location_name='SouthAfrica')
        return malawi_images
    @classmethod
    def Nairobi(cls):
        nairobi_images=cls.objects.filter(location__location_name='Nairobi')
    def save_image(self):
        self.save()
    def delete_image(self):
        self.remove()
    @classmethod
    def get_image_by_id(cls):
        images=cls.objects.filter(id)
        return images
