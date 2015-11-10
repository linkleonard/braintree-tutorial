from .models import Payment
from django.contrib.auth.models import User
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):

    payer = serializers.ReadOnlyField(source='payer.username')

    class Meta:
        model = Payment
        fields = ('url', 'amount', 'payer')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    payments = serializers.HyperlinkedRelatedField(
        view_name='payment-detail',
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'payments')
