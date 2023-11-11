import logging

from allauth.socialaccount.models import SocialAccount
from django.db import DatabaseError
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.oidc.models import ItmoIdProfile

logger = logging.getLogger("root")


@receiver(post_save, sender=SocialAccount)
def itmo_id_profile_create(sender, instance: SocialAccount, created: bool, **kwargs):
    if not created or instance.provider != "itmo_id":
        return

    data = instance.extra_data
    group = data.get("groups", [{}])[-1]

    try:
        ItmoIdProfile.objects.create(
            user_id=instance.user_id,
            isu=data.get("isu"),
            course=group.get("course"),
            faculty=group.get("faculty", {}).get("short_name", ""),
            group=group.get("name", ""),
        )
    except DatabaseError as exc:
        logger.exception(exc)
