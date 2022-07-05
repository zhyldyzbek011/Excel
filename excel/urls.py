from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('date', views.DateViewSet)
router.register('month', views.MonthViewSet)
router.register('statistic', views.StatisticViewSet)
router.register('date_kp', views.Date_1ViewSet)
router.register('table_1', views.Table_1ViewSet)
router.register('table_2', views.Table_2ViewSet)
urlpatterns = [
    path('', include(router.urls))
]
