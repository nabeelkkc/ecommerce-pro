from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lessi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'), 
)
STATE_CHOICES=(
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Chandigarh ','Chandigarh '),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi ','Delhi '),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Ladakh ','Ladakh '),
    ('Lakshadweep ','Lakshadweep '),
    ('Maharashtra','Maharashtra'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Puducherry','Puducherry'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Tripura','Tripura'),
    ('Telangana','Telangana'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),    
)  
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
    