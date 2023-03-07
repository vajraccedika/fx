from django.db import models

# Create your models here.
class Transaction(models.Model):

	#only two choices for transaction type	
	class BuySell(models.TextChoices):
		BUY = 'BUY', 'Buy'
		SELL = 'SELL', 'Sell'

	date = models.DateField(auto_now=False, auto_now_add=True)
	
	#clients are from the valid Clients in the Client table
	client = models.ForeignKey(
			'Client',
			on_delete=models.DO_NOTHING
	)
	#CP rate, or exchange rate
	rate = models.DecimalField(max_digits=5, decimal_places=4)
	#the currency coming into the bank
	currency_in = models.ForeignKey(
		'Currency',
		related_name='curr_in',
		on_delete=models.DO_NOTHING)
	#the currency going out of bank
	currency_out = models.ForeignKey(
		'Currency',
		related_name='curr_out',
		on_delete=models.DO_NOTHING)
	#whether this is classified as a BUY or SELL transaction
	buy_sell = models.CharField(
		max_length=4,
		choices=BuySell.choices
	)
	#ticket number
	transaction_number = models.PositiveIntegerField(blank=True)
	#amount of transaction
	amount = models.PositiveIntegerField()
	#keep track of who posted the transaction
	owner = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.DO_NOTHING, default=1)

class Client(models.Model):
	name = models.CharField(
		max_length=128
	)
	client_type = models.ForeignKey(
		'ClientType',
		on_delete=models.DO_NOTHING
	)

	def __str__(self):
		return self.name

class ClientType(models.Model):
	#trade_vol is a bool that tells us if the client type contributes to trade volume or not
	trade_vol = models.BooleanField()
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

class Currency(models.Model):
	name = models.CharField(max_length=8)

	def __str__(self):
		return self.name
