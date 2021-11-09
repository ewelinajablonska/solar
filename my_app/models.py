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

class Building(models.Model):
    """Information about the place of the instalation"""
    roof_covering_list = [
        ('Blachodachówka Novotegra', 'Blachodachówka Novotegra'),
        ('Dachówka Ceramiczna Novotegra', 'Dachówka Ceramiczna Novotegra'),
        ('Blachotrapez Novotegra', 'Blachotrapez Novotegra'),
        ('Aero Południe Novotegra', 'Aero Południe Novotegra'),
        ('Aero Wschód-Zachód Novotegra','Aero Wschód-Zachód Novotegra'),
        ('Grunt CORAB', 'Grunt CORAB')
    ]
    #client_ID = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='buildings')
    street = models.CharField(max_length=70, blank = True)
    house_number = models.CharField(max_length=10, blank = True)
    flat_number = models.CharField(max_length=10, blank = True)
    code = models.CharField(max_length=6, blank = True)
    city = models.CharField(max_length=70, blank = True)
    province = models.CharField(max_length=70, blank = True)
    roof_covering = models.CharField(max_length=70, choices=roof_covering_list)
    roof_type = models.CharField(max_length=70, blank = True) #choices=roof_type_list
    roof_slope = models.PositiveSmallIntegerField(default=0) #choices=roof_slope_list
    roof_orientation = models.PositiveSmallIntegerField(default=0) #choices=roof_orientation_list
    roof_direction = models.CharField(max_length=70, blank = True) #choices=roof_direction_list
    windows_number = models.IntegerField(default=0)
    chimney_number = models.IntegerField(default=1)

    def __str__(self):
        """Return the string representation of the model."""
        return f"{self.city} {self.street}"

class Installation(models.Model):
    """Information about instalation"""
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name= 'installations')
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    power = models.PositiveSmallIntegerField()
    modules = models.CharField(max_length=70, blank = True) #choices=modules_list
    modules_number = models.PositiveSmallIntegerField(default=1)
    inverter_producer = models.CharField(max_length=70, blank = True) #choices=inverter_producer_list
    inverter_model = models.CharField(max_length=70, blank = True) #choices=inverter_model_list
    inverter_number = models.PositiveSmallIntegerField(default=1)
    optimizer = models.CharField(max_length=70, blank = True) #choices=optimizer_list
    optimizer_number = models.PositiveSmallIntegerField(default=0)
    add_warranty = models.BooleanField(default=False)
    add_component_1 = models.CharField(max_length=70) #choices=add_component_list
    add_component_2 = models.CharField(max_length=70) #choices=add_component_list
    add_component_3 = models.CharField(max_length=70) #choices=add_component_list

    def __str__(self):
        """Return the string representation of the model."""
        return f"{self.power}"