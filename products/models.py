# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# Validator Function
def validate_discount_value(value, discount_value):
    if discount_value > value:
        return value
    else:
        raise ValidationError("Invalid discount value")


class Product(models.Model):
    name = models.CharField(max_length=55)
    value = models.FloatField(validators=[MaxValueValidator(99998.9), MinValueValidator(1)])
    discount_value = models.FloatField(validators=[validate_discount_value])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
