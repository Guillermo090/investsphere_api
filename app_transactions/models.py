from django.db import models


class FixedTermDeposit(models.Model):
    initial_amount = models.DecimalField(max_digits=15, decimal_places=2)
    final_amount = models.DecimalField(max_digits=15, decimal_places=2)
    expiration_date = models.DateField()
    estimated_profit = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Interest rate as a percentage")
    bank = models.CharField(max_length=100) 
    user = models.ForeignKey( 'app_users.User', on_delete=models.CASCADE, related_name='fixed_term_deposits')
    company = models.ForeignKey('app_users.Company', on_delete=models.CASCADE, related_name='fixed_term_deposits' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank} - {self.initial_amount}"


class CryptocurrencyTransaction(models.Model):
    purchase_amount = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_date = models.DateTimeField()
    commission = models.DecimalField(max_digits=15, decimal_places=2)
    base_currency = models.CharField(max_length=10)
    currency_bought = models.CharField(max_length=10)
    amount_of_bought_currency = models.DecimalField(max_digits=16, decimal_places=9)
    platform = models.CharField(max_length=100)
    user = models.ForeignKey( 'app_users.User', on_delete=models.CASCADE, related_name='criptocurrency_transactions')
    company = models.ForeignKey('app_users.Company', on_delete=models.CASCADE, related_name='criptocurrency_transactions' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency_bought} - {self.purchase_amount}"


class StockInvestment(models.Model):
    current_amount = models.DecimalField(max_digits=15, decimal_places=2)
    historical_variation = models.DecimalField(max_digits=15, decimal_places=2, help_text="Historical variation percentage")
    total_paid = models.DecimalField(max_digits=15, decimal_places=2)
    company = models.CharField(max_length=100)  # Company of the stock action
    quantity_of_shares = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField()
    user = models.ForeignKey( 'app_users.User', on_delete=models.CASCADE, related_name='stock_investments')
    company = models.ForeignKey('app_users.Company', on_delete=models.CASCADE, related_name='stock_investments' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.current_amount}"


class MutualFund(models.Model):
    initial_amount = models.DecimalField(max_digits=15, decimal_places=2)
    current_amount = models.DecimalField(max_digits=15, decimal_places=2)
    investment_date = models.DateField()
    historical_variation = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage of variation")
    total_paid = models.DecimalField(max_digits=15, decimal_places=2)
    fund_manager = models.CharField(max_length=100)
    user = models.ForeignKey( 'app_users.User', on_delete=models.CASCADE, related_name='mutual_founds')
    company = models.ForeignKey('app_users.Company', on_delete=models.CASCADE, related_name='mutual_founds' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fund_manager} - {self.initial_amount}"