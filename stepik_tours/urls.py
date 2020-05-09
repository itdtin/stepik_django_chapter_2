from django.contrib import admin
from django.urls import include, path, re_path

from tours.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    re_path(r'^', include('tours.urls')),
]
