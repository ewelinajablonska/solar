from django.contrib import admin
from .models import Client, Building, Offer, Installation

# Register your models here.
admin.site.register(Client)
admin.site.register(Building)
admin.site.register(Offer)
admin.site.register(Installation)