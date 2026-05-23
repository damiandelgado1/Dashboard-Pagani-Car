from django.shortcuts import render
from car.models import Car

# Dashboard page
def dashboard(request):
    cars = Car.objects.all()
    return render(request, "dashboard/dashboard.html", {"cars": cars})