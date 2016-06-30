from django.contrib import admin

# Register your models here.
from models import UserProfile, ActivationRequest


class ActivationRequestAdmin(admin.ModelAdmin):

    model = ActivationRequest

    list_display = ('user_profile', 'song', 'time_stamp', 'activated', 'where_am_i')
    search_fields = ['user_profile__mobile_number', 'song__song_name']


admin.site.register(UserProfile)
admin.site.register(ActivationRequest,ActivationRequestAdmin)
