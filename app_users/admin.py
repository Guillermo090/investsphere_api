from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username','email','first_name','last_name','is_staff', 'is_superuser', 'is_active','date_joined')
    ordering = ("email",)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username','email','first_name','last_name','password')}), 
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important dates', {'fields': ()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_date', 'status')
    search_fields = ('name', 'status')
    list_filter = ('name', 'status')