from django.db import models

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=255) 
    
class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()
    
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)



class Customer(models.Model):
    
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    
    class Meta:
        indexes = [models.Index(fields = ['last_name', 'first_name'])]
    
class Order(models.Model):
    PENDING_PAYMENT_STATUS = 'P'
    COMPLETED_PAYMENT_STATUS = 'C'
    FAILED_PAYMENT_STATUS = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PENDING_PAYMENT_STATUS, 'Pending'),
        (COMPLETED_PAYMENT_STATUS, 'Completed'),
        (FAILED_PAYMENT_STATUS, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING_PAYMENT_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    unit_price = models.PositiveSmallIntegerField()
    
    

    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    
