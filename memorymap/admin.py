from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Event)
admin.site.register(models.Location)
admin.site.register(models.Article)
