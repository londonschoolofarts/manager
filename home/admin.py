from django.contrib import admin
from .models import UserImage

class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'phone_number')

    def user_info(self, obj):
        return obj.username

admin.site.register(UserImage, UserImageAdmin)

