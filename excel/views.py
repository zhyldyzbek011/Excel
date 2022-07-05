
from rest_framework import status, generics

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from excel.models import Month, Statistic, Date, Table_1, Table_2
from excel.serializers import StatisticSerializer, MonthSerializer, DateSerializer, StatisticCreateUpdateSerializer, \
    Date_1Serializer, Table_2Serializer, Table_2CreateUpdateSerializer


class DateViewSet(ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

    # def create(self, request, *args, **kwargs):
    #     dates = request.data['dates']
    #     for date in dates:
    #         serializer = self.get_serializer(data=date)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #
    #     return Response('ok', status=status.HTTP_400_BAD_REQUEST)

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


class Date_1ViewSet(ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = Date_1Serializer



class Table_1ViewSet(ModelViewSet):
    queryset = Table_1.objects.all()
    serializer_class = MonthSerializer

    def create(self, request, *args, **kwargs):
        table_1 = request.data['table_1']
        for table in table_1:
            serializer = self.get_serializer(data=table)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response('ok', status=status.HTTP_400_BAD_REQUEST)



class Table_2ViewSet(ModelViewSet):
    queryset = Table_2.objects.all()
    serializer_class = Table_2Serializer

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            return Table_2CreateUpdateSerializer
        else:
            return Table_2Serializer

    def create(self, request, *args, **kwargs):
        table_2 = request.data['table_2']
        for table in table_2:
            serializer = self.get_serializer(data=table)
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
