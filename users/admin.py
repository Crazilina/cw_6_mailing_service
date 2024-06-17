from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    actions = ['block_users', 'unblock_users']
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    def block_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been blocked.")
    block_users.short_description = "Block selected users"

    def unblock_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users have been unblocked.")
    unblock_users.short_description = "Unblock selected users"
