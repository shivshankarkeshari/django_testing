# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length = 10)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.IntegerField()
    published_on = models.DateField()

    @property
    def is_in_stock(self):
        return self.quantity > 0
