from django.urls import path

from .views import DepartureView, TourView

urlpatterns = [
    path('departure/<str:departure_name>/', DepartureView.as_view(), name='departure'),
    path('tour/<int:id>/', TourView.as_view(), name='tour'),
]
