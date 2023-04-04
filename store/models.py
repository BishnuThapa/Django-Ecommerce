from django.db import models
from category.models import Category
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_name


class HostType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='host_types')
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class HostCategory(models.Model):
    name = name = models.CharField(max_length=100)
    slug = models.SlugField()
    host_type = models.ForeignKey(HostType, on_delete=models.SET_NULL)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


class RegisterProperty(models.Model):
    name = name = models.CharField(max_length=100)
    slug = models.SlugField()
    registration_no = models.CharField(max_length=255, blank=True, null=True)
    pan_vat_no = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    disctict = models.CharField(max_length=100, blank=True)
    local_level = models.CharField(max_length=100)
    ward_no = models.IntegerField()
    address = models.CharField(max_length=100)
    website = models.URLField(max_length=255, blank=True)
    description = models.TextField()
    owners_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    alternative_contact_no = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    citizenship_no = models.CharField(max_length=50, blank=True)
    images = models.ImageField(upload_to='property')
    location = models.CharField(max_length=255)

    # amenities
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    room_service = models.BooleanField(default=False)
    full_package_program = models.BooleanField(default=False)
    pickup_drop = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    long_term_stay = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    bbq_gril = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    ourdoor_services = models.BooleanField(default=False)
    airport = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    shopping_mall = models.BooleanField(default=False)
    hospital = models.BooleanField(default=False)
    famous_place_nearby = models.BooleanField(default=False)
    city_center = models.BooleanField(default=False)

    check_in_time = models.DateTimeField()
    check_out_tiime = models.DateTimeField()
    free_cancellation_of_rooms = models.BooleanField(default=False)

    # payment
    credit_card_accept = models.BooleanField(default=True)
    can_party_in_hotel = models.CharField(
        choices=['Yes', 'No', 'Depends'], default='Yes')
    is_pet_allowed = models.CharField(
        choices=['Yes', 'No', 'Depends'], default='Depends')

    # billing
    account_type = models.CharField(
        choices=['Wallet', 'Bank'], default=None)

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
