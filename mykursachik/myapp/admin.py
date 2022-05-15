from django.contrib import admin
from .models import Feature
from .models import Ad
from .models import Director


# Register your models here.
admin.site.register(Feature)
admin.site.register(Ad)
admin.site.register(Director)

