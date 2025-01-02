from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UploadedFile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'public_visibility', 'birth_year', 'age', 'address', 'is_staff', 'is_active']
    list_filter = ['public_visibility', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'public_visibility', 'birth_year', 'age', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'public_visibility', 'birth_year', 'address', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'visibility', 'cost', 'year_published']
    search_fields = ['title', 'user__username']
    list_filter = ['visibility', 'year_published']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)
