from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import models
from enumfields import Enum, EnumIntegerField


class UUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

class Product(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.name} {self.description}'
