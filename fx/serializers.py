from rest_framework import serializers
from fx.models import Transaction, Client, ClientType, Currency
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    transactions = serializers.HyperlinkedRelatedField(
	    many=True, 
			view_name='transaction-detail', 
			queryset=Transaction.objects.all()
			)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'transactions']

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
		owner = serializers.ReadOnlyField(source='owner.username')
		
		class Meta:
			model = Transaction
			fields = ['url', 'date', 'client', 'rate', 'currency_in', 'currency_out', 'buy_sell', 
	     'transaction_number', 'amount', 'owner']
		
		def create(self, validated_data):
			#create & return new instance
			return Transaction.objects.create(**validated_data)
		
		def update(self, instance, validated_data):
			#update and return existing transaction instance
			instance.date = validated_data.get('date', instance.date)
			instance.transaction_number = validated_data.get('transaction_number', instance.transaction_number)
			instance.currency_in = validated_data.get('currency_in', instance.currency_in)
			instance.currency_out = validated_data.get('currency_out', instance.currency_out)
			instance.buy_sell = validated_data.get('buy_sell', instance.buy_sell)
			instance.save()
			return instance

class ClientSerializer(serializers.HyperlinkedModelSerializer):
		
		class Meta:
			model = Client
			fields = ['url', 'name', 'client_type']

		def create(self, validated_data):
			return Client.objects.create(**validated_data)
		
		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.client_type = validated_data.get('client_type', instance.client_type)
			instance.save()
			return instance

class ClientTypeSerializer(serializers.HyperlinkedModelSerializer):
		
		class Meta:
			model = ClientType
			fields = ['url', 'name', 'trade_vol']

		def create(self, validated_data):
			return ClientType.objects.create(**validated_data)
		
		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.trade_vol = validated_data.get('trade_vol', instance.trade_vol)
			return instance

class CurrencySerializer(serializers.HyperlinkedModelSerializer):
		
		class Meta:
			model = Currency
			fields = ['url', 'name']

		def create(self, validated_data):
			return Currency.objects.create(**validated_data)
		
		def update(self, instance, validated_data):
			print(validated_data)
			instance.name = validated_data.get('name', instance.name)
			return instance