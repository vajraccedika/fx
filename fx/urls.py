from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fx import views
from fx.views import TransactionViewSet, ClientViewSet, ClientTypeViewSet, CurrencyViewSet, UserViewSet

transaction_list = TransactionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
transaction_detail = TransactionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
client_list = ClientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
client_detail = ClientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
clienttype_list = ClientTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
clienttype_detail = ClientTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
currency_list = CurrencyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
currency_detail = CurrencyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'clients', views.ClientViewSet, basename='client')
router.register(r'client-type', views.ClientTypeViewSet, basename='clienttype')
router.register(r'currency', views.CurrencyViewSet, basename='currency')

urlpatterns = [
    path('', include(router.urls))
]