from django.db import models
from PIL import Image

# Create your models here.

class CarouselProducts(models.Model):
    product_title = models.CharField(null=False, max_length=255)
    product_solution = models.CharField(null=False, max_length=255)
    product_img = models.ImageField(upload_to='carouselproducts')

    def __str__(self):
        return self.product_title

    def save(self,  *args, **kwargs):
        super(CarouselProducts, self).save(*args, **kwargs)

        product_img = Image.open(self.product_img.path)

        if product_img.height > 300 or product_img.width > 300:
            output_size = (300, 300)
            product_img.thumbnail(output_size)
            product_img.save(self.product_img.path)

class Quotation(models.Model):
    customer_name = models.CharField(null=False, max_length=255, verbose_name='Full Name')
    customer_email = models.EmailField(null=False, max_length=255)
    message = models.CharField(null=False, max_length=500)

    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_title = models.CharField(null=False, max_length=255)
    product_description = models.CharField(null=False, max_length=255)
    product_img = models.ImageField(upload_to='products')
