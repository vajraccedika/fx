from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import permissions
from fx.models import Transaction, Client, ClientType, Currency
from fx.serializers import TransactionSerializer, ClientSerializer, ClientTypeSerializer, CurrencySerializer, UserSerializer
from django.contrib.auth.models import User
from fx.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all().order_by('id')
	serializer_class = UserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all().order_by('date')
	serializer_class = TransactionSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all().order_by('name')
	serializer_class = ClientSerializer

class ClientTypeViewSet(viewsets.ModelViewSet):
	queryset = ClientType.objects.all().order_by('name')
	serializer_class = ClientTypeSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
	queryset = Currency.objects.all().order_by('name')
	serializer_class = CurrencySerializer

"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
      	'users': reverse('user-list', request=request, format=format),
      	'transactions': reverse('transaction-list', request=request, format=format),
	      'currency': reverse('currency-list', request=request, format=format),
	      'clients': reverse('client-list', request=request, format=format),
	      'client-type': reverse('client-type-list', request=request, format=format)
	
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
	
class TransactionList(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class ClientList(generics.ListCreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class ClientTypeList(generics.ListCreateAPIView):
	queryset = ClientType.objects.all()
	serializer_class = ClientTypeSerializer

class ClientTypeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ClientType.objects.all()
	serializer_class = ClientTypeSerializer

class CurrencyList(generics.ListCreateAPIView):
	queryset = Currency.objects.all()
	serializer_class = CurrencySerializer

class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Currency.objects.all()
	serializer_class = CurrencySerializer
"""