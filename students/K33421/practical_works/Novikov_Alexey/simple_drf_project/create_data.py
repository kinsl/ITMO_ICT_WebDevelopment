import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_drf_project.settings")
django.setup()

from django.utils import timezone
from project_first_app.models import CarOwner, Car, Ownership, DrivingLicence

owners = CarOwner.objects.bulk_create(
    [
        CarOwner(last_name="Иванов", first_name="Иван", birth_date=timezone.now()),
        CarOwner(last_name="Петров", first_name="Петр", birth_date=timezone.now()),
        CarOwner(last_name="Сидоров", first_name="Сидор", birth_date=timezone.now()),
        CarOwner(last_name="Николаев", first_name="Николай", birth_date=timezone.now()),
        CarOwner(last_name="Дмитриев", first_name="Дмитрий", birth_date=timezone.now()),
        CarOwner(last_name="Алексеев", first_name="Алексей", birth_date=timezone.now()),
    ]
)

cars = Car.objects.bulk_create(
    [
        Car(number="А111АА77", brand="Lada", model="Vesta", color="черный"),
        Car(number="В222ВВ77", brand="Ford", model="Focus", color="синий"),
        Car(number="С333СС77", brand="Toyota", model="Camry", color="белый"),
        Car(number="М444ММ77", brand="Hyundai", model="Solaris", color="серый"),
        Car(number="Т555ТТ77", brand="Kia", model="Rio", color="черный"),
        Car(number="О666ОО77", brand="Toyota", model="Camry", color="зеленый"),
    ]
)

ownerships = Ownership.objects.bulk_create(
    [Ownership(owner=owners[i], car=cars[i], start_date=timezone.now()) for i in range(6)]
)

licences = DrivingLicence.objects.bulk_create(
    [DrivingLicence(owner=owners[i], number=str(i + 1) * 10, type="B", issue_date=timezone.now()) for i in range(6)]
)

print(f"Автовладельцы: {owners}", f"Автомобили: {cars}", f"Владения: {ownerships}", f"Лицензии: {licences}", sep="\n\n")
