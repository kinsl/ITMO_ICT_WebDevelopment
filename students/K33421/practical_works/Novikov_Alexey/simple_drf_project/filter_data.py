import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_drf_project.settings")
django.setup()

from django.utils import timezone
from project_first_app.models import CarOwner, Car, DrivingLicence


toyota_cars = Car.objects.filter(brand="Toyota").all()

ivan_owners = CarOwner.objects.filter(first_name="Иван").all()

random_owner_id = CarOwner.objects.order_by("?").values_list("id", flat=True).first()
random_owner_licence = DrivingLicence.objects.get(owner_id=random_owner_id)

black_car_owners = CarOwner.objects.filter(ownerships__car__color="черный").all()

this_year_owners = CarOwner.objects.filter(licences__issue_date__year=timezone.now().year).all()


print(
    f"Автомобили Toyota: {toyota_cars}",
    f"Автовладельцы Иваны: {ivan_owners}",
    f"Лицензия случайного автовладельца: {random_owner_licence}",
    f"Владельцы черных автомобилей: {black_car_owners}",
    f"Владельцы, получившие лицензию в этом году: {this_year_owners}",
    sep="\n",
)
