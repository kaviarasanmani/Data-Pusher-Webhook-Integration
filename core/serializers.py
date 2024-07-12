from rest_framework import serializers
from .models import Account, Destination,IncomingData

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'account_id', 'account_name', 'app_secret_token', 'website']
        read_only_fields = ['account_id', 'app_secret_token']

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'account', 'url', 'http_method', 'headers']

class IncomingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingData
        fields = ['id', 'account', 'data', 'timestamp']