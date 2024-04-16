from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
# from .permissions import IsOwnerOrReadOnly


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permissions_classes = [permissions.IsAuthenticated]


class BetViewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permissions_classes = [permissions.AllowAny]
