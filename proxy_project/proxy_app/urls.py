from django.urls import path
from .views import ResidentialIPList, ProxyUsageCreate, dashboard
from .views import (
    ResidentialIPListCreate, ResidentialIPDetail,
    ProxyUsageListCreate, ProxyUsageDetail
)

urlpatterns = [
    path('ips/', ResidentialIPList.as_view(), name='ip-list'),
    path('usage/', ProxyUsageCreate.as_view(), name='usage-create'),
    path('dashboard/',dashboard,name='dashboard'),
    # ResidentialIP endpoints
    path('api/ips/', ResidentialIPListCreate.as_view(), name='ip-list-create'),
    path('api/ips/<int:pk>/', ResidentialIPDetail.as_view(), name='ip-detail'),
    # ProxyUsage endpoints
    path('api/usage/', ProxyUsageListCreate.as_view(), name='usage-list-create'),
    path('api/usage/<int:pk>/', ProxyUsageDetail.as_view(), name='usage-detail'),
]