from django.db import models
from ckeditor.fields import RichTextField

class Type(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='tourismtypes/', null=True)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='attractions')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='attractions')
    image = models.ImageField(upload_to='attractions/')
    # Add other fields as per your requirements

    def __str__(self):
        return self.name


class AttractionFee(models.Model):
    USD = 'usd'
    TZS = 'tzs'

    CURRENCY = (
        ('USD', 'Usd'),
        ('TZS', 'Tzs'),
    )
    name = models.CharField(max_length=100)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, null=True,
                                   related_name='attractionfees')
    currency = models.CharField(max_length=20, choices=CURRENCY, null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name


class Image(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, null=True,
                                   related_name='attractionimages')
    images = models.ImageField(upload_to='attractions/', blank=True, null=True)

    def __str__(self):
        return self.attraction.name
    
class InterestingFacts(models.Model):
    facts = RichTextField(null=True, blank=True)
    # location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='facts/', null=True, blank=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='interestingfacts')

    # Add other fields as per your requirements

    def __str__(self):
        return self.attraction.name
    

    class Meta:
        verbose_name_plural= 'Interesting Facts'


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField(null=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='hotels')
    # price_per_day = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)

    # Add other fields as per your requirements

    def __str__(self):
        return self.name
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotelrooms')
    room_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='hotels/', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.room_number
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return self.guest_name
    
class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True,
                              related_name='hotelimages')
    images = models.ImageField(upload_to='hotels/', blank=True, null=True)


class TourOperator(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField(null=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='touroperators')
    phone_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='touroperators/', null=True, blank=True)
    email = models.EmailField()
    # Add other fields as per your requirements

    def __str__(self):
        return self.name
    
class OperatorImage(models.Model):
    touroperator = models.ForeignKey(TourOperator, on_delete=models.CASCADE, null=True,
                                     related_name='operatorimages')
    images = models.ImageField(upload_to='touroperators/', blank=True, null=True)

    def __str__(self):
        return self.touroperator.name


class OperatorPackage(models.Model):
    name = models.CharField(max_length=100)
    touroperator = models.ForeignKey(TourOperator, on_delete=models.CASCADE, null=True,
                                     related_name='operatorpackages')
    content = RichTextField(null=True)
    image = models.ImageField(upload_to='touroperators/', null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

    
    