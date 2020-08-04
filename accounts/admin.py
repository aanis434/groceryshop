from django.contrib import admin
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in dispalying the user mdoel
    # These override the definitons on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = ('first_name', 'last_name', 'email', 'admin', 'staff', 'group')
    list_filter = ('admin', 'employee', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'new_password', 'new_password_confirmation')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'employee', 'active', 'group')}),
    )
    filter_horizontal = ()

    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
