from django.contrib import admin
from .models import Ad
from .models import Director
from .models import Method


# Register your models here.
admin.site.register(Ad)
admin.site.register(Director)
admin.site.register(Method)

