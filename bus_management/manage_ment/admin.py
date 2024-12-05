from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bus, Route, Driver

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Driver)
