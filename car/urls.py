from django.contrib import admin
from django.urls import path
from .views import ListCar, DetailCar, CreateCar, ModifyCar, DeleteCar


app_name = "car"

urlpatterns = [
    path('list/', ListCar.as_view(), name="car_list"),
    path('detail/<int:pk>/', DetailCar.as_view(), name="car_detail"),
    path('create/', CreateCar.as_view(), name="create_car"),
    path('modify/<int:pk>/', ModifyCar.as_view(), name="modify_car"),
    path('delete/<int:pk>/', DeleteCar.as_view(), name="delete_car"),
    path('admin/', admin.site.urls),
]