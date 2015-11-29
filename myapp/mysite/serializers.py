from .models import Payment
from django.contrib.auth.models import User
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):

    payer = serializers.ReadOnlyField(source='payer.username')
    payment_method_nonce = serializers.CharField(write_only=True)

    class Meta:
        model = Payment
        fields = ('url', 'amount', 'payer', 'payment_method_nonce')
        extra_kwargs = {'payment_method_nonce': {'write_only': True}}

    def create(self, validated_data):
        # The payment method nonce is only needed to perform
        # transactions. We don't need to store it.
        del validated_data['payment_method_nonce']

        return super(PaymentSerializer, self).create(validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    payments = serializers.HyperlinkedRelatedField(
        view_name='payment-detail',
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'payments')
