import os

import django
from django.db.models import Min, Max, Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_drf_project.settings")
django.setup()

from project_first_app.models import CarOwner, Car, Ownership, DrivingLicence

oldest_licence = DrivingLicence.objects.aggregate(max_issue_date=Min("issue_date"))["max_issue_date"]

newest_ownership = Ownership.objects.aggregate(max_start_date=Max("start_date"))["max_start_date"]

ownerships_counts = CarOwner.objects.annotate(count=Count("ownerships"))
ownerships_counts_str = [f"{owner.full_name}: {owner.count}" for owner in ownerships_counts]

cars_count_by_brands = Car.objects.values("brand").annotate(count=Count("id"))
cars_count_by_brands_str = [f"{car['brand']}: {car['count']}" for car in cars_count_by_brands]

sorted_owners = CarOwner.objects.order_by("ownerships__start_date").all()

print(
    f"Дата самого старшего удостоверения: {oldest_licence}",
    f"Самая поздняя дата авто владения: {newest_ownership}",
    f"Количество машин для каждого водителя: {ownerships_counts_str}",
    f"Количество машин каждой марки: {cars_count_by_brands_str}",
    f"Автовладельцы, отсортированные по дате выдачи удостоверения: {sorted_owners}",
    sep="\n\n",
)
