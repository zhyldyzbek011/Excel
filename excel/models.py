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

    class Meta:
        verbose_name_plural = 'Дата (Исполнение бюджета)'


class Month(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='month')
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал')
    start_cp = models.IntegerField(default=0, verbose_name='Сумма КП, сом')
    end_bud = models.IntegerField(default=0, verbose_name='Бюджет на это число')

    def __str__(self):
        return f'{self.date} {self.branch}'

    class Meta:
        verbose_name_plural = 'Ежемесячные данные(Исполнение бюджета)'


class Statistic(models.Model):
    month = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='date', null=True)
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал', null=True)
    date = models.DateField(verbose_name='Дата')
    kp_som = models.IntegerField(default=0, verbose_name='КП, сом')
    kp_kol = models.IntegerField(default=0, verbose_name='КП, кол-во')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name_plural = 'Ежедневные данные(Исполнение бюджета)'


class Date_1(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50, null=True)
    date = models.DateField(verbose_name='дата')

    def __str__(self):
        return f'Сомовый и Долларовый КП на число {self.date} '
    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Дата Сомовый, Долларовый КП'

class Table_1(models.Model):
    date_1 = models.ForeignKey(Date_1, on_delete=models.CASCADE, related_name='date_1', verbose_name='Дата')
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал', null=True)
    som_kp = models.IntegerField(default=0, verbose_name='Сомовый КП, KGS')
    dollar_kp = models.IntegerField(default=0, verbose_name='долларовый КП, USD')


    def __str__(self):
        return str(self.date_1)

    class Meta:
        verbose_name_plural = 'Ежемесячный Сом, Долларовый Кп'


class Table_2(models.Model):
    date_1 = models.ForeignKey(Date_1, on_delete=models.CASCADE, related_name='date_KP2', verbose_name='Ежемесячные данные')
    date = models.DateField(verbose_name='дата')
    branch = models.CharField(max_length=300, choices=BRANCH, verbose_name='Филиал', null=True)
    som_kp = models.IntegerField(default=0, verbose_name='Сомовый КП, KGS')
    dollar_kp = models.IntegerField(default=0, verbose_name='долларовый КП, USD')


    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = 'Ежедневный Сом, Долларовый Кп'

