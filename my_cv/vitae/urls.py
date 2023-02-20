from django.urls import path
from .views import BaseHomeView, ModalFormView

urlpatterns = [
    path('', BaseHomeView.as_view()),
    path('modalform/', ModalFormView.as_view(), name='modalform')
]
