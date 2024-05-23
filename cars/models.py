from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=55)
    description=models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        
    def __str__(self):
        return self.name 


class Car(models.Model):
    brand=models.CharField(max_length=55)
    model=models.CharField(max_length=55)
    description=models.TextField(default=None)
    image=models.ImageField(upload_to='cars_images/',blank=True, null=True)
    year = models.IntegerField()
    price=models.FloatField()
    is_sold=models.BooleanField(default=False)
    height = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    width = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name= 'car')

    def __str__(self):
        return f"{self.brand} {self.model}({self.year})"
    

    
class CarDetail(models.Model):
    car=models.OneToOneField(Car,on_delete=models.CASCADE,primary_key=True,related_name='detail')
    color=models.CharField(max_length=20, default="#FFFFFF")
    engine_type=models.CharField(max_length=15,default=None)
    engine_capacity=models.PositiveSmallIntegerField(default=0)
    mileage=models.PositiveBigIntegerField(default=0)
    gearbox_type=models.CharField(max_length=15,default=0)
    number_of_doors=models.PositiveSmallIntegerField(default=0)
    power=models.PositiveSmallIntegerField(default=0)
    top_speed=models.PositiveSmallIntegerField(default=0)
    acceleration=models.PositiveSmallIntegerField(default=0) #разгон
    fuel_consumption=models.PositiveSmallIntegerField(default=0)

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="reviews")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="orders")
    quantity=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
