from django.db import models

# Create your models here.

class CarouselProducts(models.Model):
    product_title = models.CharField(null=False, max_length=255)
    product_solution = models.CharField(null=False, max_length=255)
    product_img = models.ImageField(upload_to='carouselproducts')

    def __str__(self):
        return self.product_title