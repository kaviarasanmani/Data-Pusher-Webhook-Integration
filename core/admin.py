from django.contrib import admin
from .models import Account, Destination, IncomingData

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'email', 'account_id', 'website')
    search_fields = ('account_name', 'email', 'account_id')
    readonly_fields = ('account_id', 'app_secret_token')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('account', 'url', 'http_method')
    list_filter = ('http_method', 'account')
    search_fields = ('account__account_name', 'url')

@admin.register(IncomingData)
class IncomingDataAdmin(admin.ModelAdmin):
    list_display = ('account', 'timestamp')
    list_filter = ('account', 'timestamp')
    search_fields = ('account__account_name',)
    readonly_fields = ('account', 'data', 'timestamp')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False