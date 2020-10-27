from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


from core.models import Account, Action
from accounts import serializers


class ActionViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """View Set for action model"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ActionSerializer
    queryset = Action.objects.all()

    def perform_create(self, serializer):
        """Create action"""

        serializer.save(user=self.request.user)

        amount = serializer.data['amount']
        act = serializer.data['act']
        account = serializer.data['account']
        account_to_change = Account.objects.get(id=account)

        if bool(act):
            account_to_change.saldo += amount
        else:
            account_to_change.saldo -= amount

        account_to_change.save()


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Account.objects.all()
