from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def max_weight(value):
    if value > 500:
        raise ValidationError(
            _('%(value)s is above the accepted limit '),
            params={'value': value},
        )

def max_percentage(value):
    if value > 100:
        raise ValidationError(
            _('%(value)s is above the accepted limit '),
            params={'value': value},
        )

class Drone(models.Model):
    MODEL_CHOICES= [
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),
    ]

    STATE_CHOICES = [
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING','RETURNING')
    ]

    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=20,choices=MODEL_CHOICES)
    weight_limit = models.IntegerField(validators=[max_weight])
    battery_capacity = models.IntegerField(validators=[max_percentage])
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='IDLE')
    

    def __str__(self) -> str:
        return self.serial_number

class Medication(models.Model):
    name = models.CharField(max_length=255, validators=[RegexValidator(r"^[\w-]+$")])
    weight = models.IntegerField()
    code = models.CharField( max_length=255 ,validators=[RegexValidator(r"^[A-Z0-9_]+$")])
    image = models.ImageField( upload_to='images/')

    def __str__(self) -> str:
        return self.name


class Loads(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE) 
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

class EnventLog(models.Model):
    date_checked = models.DateTimeField(auto_now_add=True)
    drone = models.ForeignKey(Drone, on_delete=models.PROTECT)
    battery = models.IntegerField()

