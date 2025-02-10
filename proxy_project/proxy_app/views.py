from rest_framework import generics
from .models import ResidentialIP, ProxyUsage
from .serializers import ResidentialIPSerializer, ProxyUsageSerializer
from django.shortcuts import render
from .models import ResidentialIP, ProxyUsage

def dashboard(request):
    ips = ResidentialIP.objects.all()
    usage_records = ProxyUsage.objects.all()
    return render(request, 'proxy_app/dashboard.html', {
        'ips': ips,
        'usage_records': usage_records,
    })

class ResidentialIPList(generics.ListAPIView):
    queryset = ResidentialIP.objects.filter(is_active=True)
    serializer_class = ResidentialIPSerializer

#List and create ResidentialIPs
class ResidentialIPListCreate(generics.ListCreateAPIView):
    queryset = ResidentialIP.objects.all()
    serializer_class = ResidentialIPSerializer

# Retrieve, update, or delete a ResidentialIP
class ResidentialIPDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResidentialIP.objects.all()
    serializer_class = ResidentialIPSerializer

# List and create ProxyUsage records
class ProxyUsageListCreate(generics.ListCreateAPIView):
    queryset = ProxyUsage.objects.all()
    serializer_class = ProxyUsageSerializer

# Retrieve, update, or delete a ProxyUsage record
class ProxyUsageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProxyUsage.objects.all()
    serializer_class = ProxyUsageSerializer

class ProxyUsageCreate(generics.CreateAPIView):
    queryset = ProxyUsage.objects.all()
    serializer_class = ProxyUsageSerializer