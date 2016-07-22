from django.contrib import admin

from models import GeneralProfile


class GeneralProfileAdmin(admin.ModelAdmin):
    list_display = ('user','operator')

# Register your models here.

admin.site.register(GeneralProfile,GeneralProfileAdmin)
