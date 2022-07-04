
from rest_framework import serializers


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
        # representation['ef_bud'] = budget.end_bud / instance.kp_som * 100
        # representation['ef_bud'] = f'{instance.kp_som / budget.end_bud * 100 } %'
        representation['ef_bud'] = f'{round(instance.kp_som / budget.end_bud * 100), 2}%'

        return representation
