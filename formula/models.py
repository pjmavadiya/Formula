from django.db import models

# Create your models here.


class Formula(models.Model):
    OPERATOR_CHOICES = (
        ('ADDITION', '+'),
        ('SUBTRACTION', '-'),
        ('DIVISION', '/'),
        ('MULTIPLICATION', '*'),
    )
    name = models.CharField(max_length=10, unique=True)
    operandA = models.CharField(max_length=10)
    operator = models.CharField(max_length=20, choices=OPERATOR_CHOICES, blank=True)
    operandB = models.CharField(max_length=10, blank=True)

