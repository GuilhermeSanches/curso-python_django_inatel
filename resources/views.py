from datetime import date
from django.shortcuts import render
from .models import UseControl, Driver, Vehicle, Manufacturer


def index(request):
    return render(request, "hello.html")


def usecontrol_add(request):
    driver = Driver(name="Guilherme Sanches")
    driver.save()

    manufacturer = Manufacturer(name="Haha")
    manufacturer.save()

    manufacture_year = date(2007, 1, 1)

    vehicle = Vehicle(name="Camaro", license_plate="gxd1454", \
        manufacturer=manufacturer, description="Carro ruim", manufacture_year=manufacture_year)
    vehicle.save()

    usecontrol = UseControl(
        driver = driver,
        vehicle = vehicle,
        date_started = manufacture_year)
    usecontrol.save()

    return render(request, "usecontrol_add.html")
