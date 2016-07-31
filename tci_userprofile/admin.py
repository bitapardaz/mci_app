from django.contrib import admin
from models import UserProfile,MobileDevice


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','is_active','is_active','last_visit']

class MobileDeviceAdmin(admin.ModelAdmin):
    list_display=['user_profile','imei','token_string','sms_verification_code','sms_code_expiery']

# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(MobileDevice,MobileDeviceAdmin)
