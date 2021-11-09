from django.db import models

# Create your models here.
class Client(models.Model):
    """Information about client"""
    first_name = models.CharField(max_length=70, blank = True)
    last_name = models.CharField(max_length=70, blank = True)
    street = models.CharField(max_length=70, blank = True)
    house_number = models.CharField(max_length=10, blank = True)
    flat_number = models.CharField(max_length=10, blank = True)
    code = models.CharField(max_length=6, blank = True)
    city = models.CharField(max_length=70, blank = True)
    province = models.CharField(max_length=20, blank = True)
    id_number = models.CharField(max_length=8, blank=True)
    PESEL = models.PositiveSmallIntegerField(max_length=11, default=0)
    phone_number = models.CharField(max_length=70, blank = True)
    email = models.EmailField(blank = True)
    first_contact_date = models.DateField(auto_now_add=True, blank = True)
    last_contact_date = models.DateField(auto_now=True, blank = True)
    company = models.BooleanField(default=False)

    def __str__(self):
        """Return the string representation of the model."""
        return f"{self.first_name} {self.last_name}"