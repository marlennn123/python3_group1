from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination


class WomenAPIListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permissions_classes = [permissions.IsAuthenticated]
    pagination_class = WomenAPIListPagination


class BetViewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permissions_classes = [permissions.AllowAny]
    pagination_class = WomenAPIListPagination


