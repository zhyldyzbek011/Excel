from django.db.models import Avg
from rest_framework import serializers


from excel.models import Month, Statistic, Date, Table_1, Table_2, Date_1


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
        representation['ef_bud'] = f'{round(instance.kp_som / budget.end_bud * 100),2}%'
        representation['Итоговый результат'] = instance.month.aggregate(Avg('ef_bud'))

        return representation


class Date_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Date_1
        fields = '__all__'



class Table_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table_1
        fields = '__all__'


class Table_2CreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table_2
        fields = '__all__'


class Table_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table_2
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        kp = Table_1.objects.filter(date_1=instance.date_1, branch=instance.branch, ).first()
        representation['месяц'] = instance.date_1.title
        representation['дата'] = instance.date_1.date
        representation['кп сом 01'] = kp.som_kp
        representation['кп доллар 01'] = kp.dollar_kp
        representation['В нац валюте'] = instance.som_kp - kp.som_kp
        representation['Долларового'] = instance.dollar_kp - kp.dollar_kp


        return representation