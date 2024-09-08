from django.contrib import admin
from .models import FixedTermDeposit, CryptocurrencyTransaction, StockInvestment, MutualFund

@admin.register(FixedTermDeposit)
class FixedTermDepositAdmin(admin.ModelAdmin):
    list_display = ('bank', 'initial_amount', 'final_amount', 'interest_rate', 'expiration_date', 'user', 'company')
    search_fields = ('bank', 'user__username', 'company__name')
    list_filter = ('bank', 'interest_rate', 'expiration_date')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CryptocurrencyTransaction)
class CryptocurrencyTransactionAdmin(admin.ModelAdmin):
    list_display = ('currency_bought', 'purchase_amount', 'commission', 'platform', 'purchase_date', 'user', 'company')
    search_fields = ('currency_bought', 'user__username', 'platform')
    list_filter = ('platform', 'purchase_date')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StockInvestment)
class StockInvestmentAdmin(admin.ModelAdmin):
    list_display = ('company', 'current_amount', 'historical_variation', 'total_paid', 'purchase_date', 'user', 'company')
    search_fields = ('company', 'user__username')
    list_filter = ('company', 'purchase_date')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MutualFund)
class MutualFundAdmin(admin.ModelAdmin):
    list_display = ('fund_manager', 'initial_amount', 'current_amount', 'historical_variation', 'investment_date', 'user', 'company')
    search_fields = ('fund_manager', 'user__username')
    list_filter = ('fund_manager', 'investment_date')
    readonly_fields = ('created_at', 'updated_at')