from django import template
from datetime import date
from resources.models import Vehicle

register = template.Library()

@register.simple_tag
def get_vehicle(total_itens):
    date_vehicle = date(2007,1,1)
    v1 = Vehicle(
        name="Uno",
        license_plate="GGF0145",
        manufacture_year=date_vehicle
    )
    v1.save()

    list_vehicle = []
    list_vehicle.append(v1)
    return list_vehicle[:total_itens]
