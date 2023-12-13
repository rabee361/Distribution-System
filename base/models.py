# from django.contrib.gis.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from base.api.managers import CustomManagers
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    phonenumber = PhoneNumberField(region='DZ',unique=True)
    username = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',) 
    
    # objects = CustomManagers()

    def __str__(self):
        return self.username
    
    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh':str(refresh),
    #         'access':str(refresh.access_token)
    #     }



class Client(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    # location = 


    
class Client(models.Model):
    CHOICES = (
        ('سوبر ماركت', 'سوبر ماركت'),
        ('مقهى', 'مقهى'),
        ('محل جملة', 'محل جملة'),
        ('محل نصف جملة', 'محل نصف جملة'),
    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    category = models.CharField(max_length=75, choices=CHOICES)
    number = PhoneNumberField(region='DZ')
    info = models.TextField(null=True)

    def __str__(self):
        return self.name
    
    # location






class Driver(models.Model):
    driver = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class SalesEmployee(models.Model):
    representative = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # address = 
    # nots text
    # شاحنة
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    iamge = models.ImageField(upload_to='images\poduct')
    description = models.TextField(max_length=2000)
    quantity = models.IntegerField()
    purch_price = models.FloatField()
    sale_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    num_per_item = models.IntegerField()
    item_per_carton = models.IntegerField()
    limit = models.IntegerField()
    info = models.TextField(max_length=1000)
    added = models.DateTimeField(auto_now_add=True)
    # barcode

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-added']

class Cart(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='Cart_Products')

    @property
    def get_items_num(self):
        return self.items.count()
    
    def __str__(self):
        return f'{self.customer} cart'
    

class Cart_Products(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['-products__added']

    @property
    def add_item(self):
        self.quantity += self.quantity  
        self.save()

    @property
    def sub_item(self):
        self.quantity -= self.quantity
        self.save()

    def __str__(self):
        return self.cart.customer.name





class Order(models.Model):
    # clinet 
    # number order 
    # num prodect
    # full price 
    # date
    # 
    pass




class Notifications(models.Model):
    pass


class Supplier(models.Model):
    # name
    # company name
    # phone number
    # location
    # notes text
    pass