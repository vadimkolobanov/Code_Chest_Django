from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'id_telegramm',
                    'image', 'rating', 'open_profile', 'pro_profile',)
    list_display_links = ('username',)
    # readonly_fields = ('') # только на чтение
    ordering = ('id',)
