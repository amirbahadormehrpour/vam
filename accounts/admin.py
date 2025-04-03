# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Profile

class CustomUserAdmin(BaseUserAdmin):
    # نیازی به فرم سفارشی نیست چون UserAdmin خودش پسورد رو مدیریت می‌کنه
    list_display = ('phone_number', 'national_id', 'is_staff', 'is_active', 'is_approved_by_admin','last_login','date_joined',)
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_approved_by_admin')
    
    fieldsets = (
        (None, {'fields': ('phone_number', 'national_id', 'password',)}),
        ('مجوزها', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_approved_by_admin')}),
        ('times', {'fields': ('last_login','date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'national_id', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'is_approved_by_admin','last_login','date_joined',),
        }),
    )
    
    search_fields = ('phone_number', 'national_id')
    ordering = ('phone_number',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'credit_score', 'coins')
    list_filter = ('credit_score',)
    search_fields = ('user__phone_number', 'first_name', 'last_name')
    
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'father_name', 'job', 'address', 'postal_code')}),
        ('مدارک', {'fields': ('profile_picture', 'front_national_card', 'back_national_card')}),
        ('امتیازات', {'fields': ('credit_score', 'coins', 'sheba_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)