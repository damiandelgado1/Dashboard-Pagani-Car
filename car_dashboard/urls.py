from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('car/', include("car.urls", namespace="car")),
    path('admin/', admin.site.urls),
]
