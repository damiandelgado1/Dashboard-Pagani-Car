from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car


# Display all Car availability
class ListCar(ListView):
    model = Car
    template_name = "car/list_car.html"
    context_object_name = "cars"


# Show all detail by a Car
class DetailCar(DetailView):
    model = Car
    template_name = "car/detail_car.html"
    context_object_name = "car"


# Create new Car for Sale
class CreateCar(CreateView):
    model = Car
    fields = [
        "brand",
        "model",
        "photo",
        "preview",
        "description",
        "photo_interior",
        "tires",
        "max_speed",
        "tire",
        "external_color",
        "internal_color",
        "stock",
        "availability",
        "price"
    ]
    template_name = "car/car_create.html"
    success_url = reverse_lazy("dashboard")


# Modify stated of the Car
class ModifyCar(UpdateView):
    model = Car
    fields = [
        "external_color",
        "internal_color",
        "stock",
        "availability",
        "price",
    ]
    template_name = "car/car_modify.html"
    success_url = reverse_lazy("dashboard")


class DeleteCar(DeleteView):
	model = Car
	template_name = "car/car_delete.html"
	success_url = reverse_lazy("dashboard")