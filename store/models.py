from django.db import models
# Create your models here.


from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=50)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title

