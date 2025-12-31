from django.contrib import admin
from .models import * # all models import by *
# Register your models here.
admin.site.register(employee)
admin.site.register(feedback)