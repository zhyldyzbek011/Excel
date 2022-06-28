from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import SearchFilter

from excel.models import Month, Statistic, Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'


class StatisticCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        budget = Month.objects.filter(date=instance.month, branch=instance.branch).first()
        representation['month'] = {
            "title": instance.month.title,
            "start_date": instance.month.start_date,
            "end_date": instance.month.end_date,
        } if instance.month else None
        representation['start_cp'] = budget.start_cp
        representation['end_bud'] = budget.end_bud
        representation['es_bud'] = instance.kp_som - budget.end_bud
        representation['es_bud'] = instance.kp_som - budget.end_bud
        return representation
