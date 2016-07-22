from django.contrib import admin

from models import GeneralProfile


class GeneralProfileAdmin(admin.ModelAdmin):
    list_display = ('user','operator')
    search_fields = ('user__username',)

# Register your models here.

admin.site.register(GeneralProfile,GeneralProfileAdmin)
