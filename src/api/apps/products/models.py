from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import models
from enumfields import Enum, EnumIntegerField
# Create your models here.a


# class OrderStatusOptions(Enum):
#     NONE = 0
#     INITIAL = 1
#     COMPLETE = 2
#     CANCELED = 3
#     PROCESSING = 4

#     # TODO: Failed state?

#     class Labels:
#         NONE = _('none')
#         INITIAL = _('Initial')
#         COMPLETE = _('Complete')
#         CANCELED = _('Canceled')
#         PROCESSING = _('Processing')


class Product(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.name} {self.description}'
