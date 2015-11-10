from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payer = models.ForeignKey(User, related_name='payments', null=True)

    class Meta:
        ordering = ('created',)
