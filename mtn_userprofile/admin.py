from django.contrib import admin

# Register your models here.

# Register your models here.
from models import MTN_UserProfile,MTN_ActivationRequest



class MTN_UserProfileAdmin(admin.ModelAdmin):

    model = MTN_UserProfile

    list_display = ('mobile_number',)
    search_fields = ['mobile_number']


class MTN_ActivationRequestAdmin(admin.ModelAdmin):

    model = MTN_ActivationRequest

    list_display = ('user_profile', 'song', 'time_stamp', 'activated', 'where_i_am')
    search_fields = ['user_profile__mobile_number', 'song__song_name']



admin.site.register(MTN_UserProfile,MTN_UserProfileAdmin)
admin.site.register(MTN_ActivationRequest,MTN_ActivationRequestAdmin)
