from django.contrib import admin

# Register your models here.
from models import UserProfile, ActivationRequest


class UserProfileAdmin(admin.ModelAdmin):

    model = UserProfile

    list_display = ('mobile_number',)
    search_fields = ['mobile_number']
    fields = ('mobile_number','token')
    exclude = ('general_profile',)


class ActivationRequestAdmin(admin.ModelAdmin):

    model = ActivationRequest

    list_display = ('user_profile', 'song', 'time_stamp', 'activated', 'where_i_am')
    search_fields = ['user_profile__mobile_number', 'song__song_name']




admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ActivationRequest,ActivationRequestAdmin)
