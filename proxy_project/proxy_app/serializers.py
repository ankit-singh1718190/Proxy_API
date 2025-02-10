from rest_framework import serializers
from .models import ResidentialIP, ProxyUsage

class ResidentialIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialIP
        fields = '__all__'

class ProxyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyUsage
        fields = '__all__'