from django.contrib import admin
from django.urls import path
from .views import ListCar, DetailCar, CreateCar, ModifyCar, DeleteCar


app_name = "car"

urlpatterns = [
    path('list/', ListCar.as_view(), name="list_car"),
    path('detail/', DetailCar.as_view(), name="detail_car"),
    path('create', CreateCar.as_view(), name="create_car"),
    path('modify/', ModifyCar.as_view(), name="modify_car"),
    path('delete/', DeleteCar.as_view(), name="delete_car"),
    path('admin/', admin.site.urls),
]