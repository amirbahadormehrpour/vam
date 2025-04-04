from django.contrib import admin
from .models import ReferralCode, ReferralInvitation

@admin.register(ReferralInvitation)
class ReferralInvitationAdmin(admin.ModelAdmin):
    list_display = ('referrer', 'invited_user', 'referral_code', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('referrer__phone_number', 'invited_user__phone_number')