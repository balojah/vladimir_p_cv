from django.urls import path
from .views import BaseHomeView

urlpatterns = [
    path('', BaseHomeView.as_view(), name='home_view')
]
