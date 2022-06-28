from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('date', views.DateViewSet)
router.register('month', views.MonthViewSet)
router.register('statistic', views.StatisticViewSet)
urlpatterns = [
    path('', include(router.urls))
]
