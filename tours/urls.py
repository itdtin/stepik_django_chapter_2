from django.urls import re_path
from .views import DepartureView, TourView

urlpatterns = [
    re_path(r'departure/(?P<departure_name>\D+)/', DepartureView.as_view(), name='departure'),
    re_path(r'tour/(?P<id>\d+)/', TourView.as_view(), name='tour'),
]
