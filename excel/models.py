from sre_constants import BRANCH

from django.db import models

BRANCH = [
    ('1_ГО', '1_ГО'),
    ('2_ОФ', '2_ОФ'),
    ('3_ЖАФ', '3_ЖАФ'),
    ('4_БФ', '4_БФ'),
    ('5_ТФ', '5_ТФ'),
    ('6_НФ', '6_НФ'),
    ('7_КФ', '7_КФ'),
    ('8_БатФ', '8_БатФ'),
]


class Date(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, null=True)
    start_date = models.DateField(verbose_name='Начало месяца')
    end_date = models.DateField(verbose_name='Конец месяца')

    def __str__(self):
        return f'c {self.start_date} по {self.end_date}'


class Month(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='month')
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал')
    start_cp = models.IntegerField(default=0, verbose_name='Сумма КП, сом')
    end_bud = models.IntegerField(default=0, verbose_name='Бюджет на это число')

    def __str__(self):
        return f'{self.date} {self.branch}'


class Statistic(models.Model):
    month = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='date', null=True)
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал', null=True)
    date = models.DateField(verbose_name='Дата')
    kp_som = models.IntegerField(default=0, verbose_name='КП, сом')
    kp_kol = models.IntegerField(default=0, verbose_name='КП, кол-во')

    def __str__(self):
        return f'{self.date}'
