from django.contrib import admin

    #My imports
from .models import Setting,About,History

# Register your models here.
admin.site.register(Setting)
admin.site.register(About)
admin.site.register(History)

