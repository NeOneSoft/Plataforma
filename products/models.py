# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=55, validators=[MinLengthValidator(3)])
    value = models.FloatField(validators=[MaxValueValidator(99998.9), MinValueValidator(1.0)])
    discount_value = models.FloatField(null=True)
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    # Overwriting save() method
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Product, self).save(*args, **kwargs)

    # Define clean() method to validate value and discount fields
    def clean(self):
        super(Product, self).clean()
        if self.value < self.discount_value:
            raise ValidationError({'discount_value': 'Invalid discount value. It has to be minor than value'})

    def __str__(self):
        return self.name
