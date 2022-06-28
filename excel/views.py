from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from excel.models import Month, Statistic, Date
from excel.serializers import StatisticSerializer, MonthSerializer, DateSerializer, StatisticCreateUpdateSerializer


class DateViewSet(ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer


class MonthViewSet(ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

    def create(self, request, *args, **kwargs):
        branches = request.data['branches']
        for branch in branches:
            serializer = self.get_serializer(data=branch)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response('ok', status=status.HTTP_400_BAD_REQUEST)


class StatisticViewSet(ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            return StatisticCreateUpdateSerializer
        else:
            return StatisticSerializer

    def create(self, request, *args, **kwargs):
        branches = request.data['branches']
        for branch in branches:
            serializer = self.get_serializer(data=branch)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

        return Response('ok', status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
