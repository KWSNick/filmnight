from django.db import models

# Create your models here.


# Model for common price list
class price_list(models.Model):
    cost_name = models.CharField(max_length=20, null=False, blank=False)
    cost_price = models.DecimalField(max_digits=5,
                                     decimal_places=2,
                                     null=False,
                                     blank=False)

    def __str__(self):
        return self.cost_name
