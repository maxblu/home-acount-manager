from django.db.models import fields
from rest_framework import serializers
from core.models import Account, Action


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ['id', 'amount', 'act', 'razon', 'account', 'date', 'user']

        read_only_fields = ('id', 'user',)


class AccountSerializer(serializers.ModelSerializer):

    actions = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'tipo', 'saldo', 'actions']

        read_only = ('id',)
