from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('my-admin/', admin.site.urls),
    path('', include('vitae.urls'))
]
