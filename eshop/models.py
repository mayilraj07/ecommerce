from django.db import models
from django.contrib.auth.models import User
import datetime
import os

status_list = (
    ('Order Placed','Order Placed'),
    ('Shipped','Shipped'),
    ('On the way','On the way'),
    ('Out for delivery','Out for delivery'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

address_choice = [("Home","Home"),("Work","Work")]
state_choice = [
('Andhra Pradesh','Andhra pradesh'),
('Karnataga','karnataga'),
('Tamilnadu','Tamilnadu'),
('Kerala','Kerala')
]

def getFileName(request,filename):
    current_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_fileName = '%s%s'%(current_time,filename)
    return new_fileName

class Category(models.Model):
    category_name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=True,help_text='Show/Hide')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    trending = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    status = models.BooleanField(default=True,help_text='Show/Hide')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
    @property
    def totalCost(self):
        return self.quantity * self.selling_price
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    address = models.TextField(max_length=200,default='')
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50,blank=True)
    mobile = models.BigIntegerField()
    zipcode = models.IntegerField()
    address_type = models.CharField(max_length=10,default='',choices=address_choice)
    state = models.CharField(max_length=200,choices=state_choice)

    def __str__(self):
        return self.name
    
class BuyProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def totalCost(self):
        return self.product_qty * self.product.selling_price
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

    @property
    def totalCost(self):
        return self.product_qty * self.product.selling_price
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50,null=True)
    amount = models.FloatField()
    payment_mode = models.CharField(max_length=50,null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=status_list,default='Order Placed')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.user.username

    @property
    def totalCost(self):
        return self.quantity * self.product.selling_price
    
class Favourite(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     product_qty = models.IntegerField(default=1)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.user.username