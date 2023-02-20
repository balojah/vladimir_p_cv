import time

from core.models import BaseAbsModel

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ContactModel(BaseAbsModel):

    subject = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    contacts = models.CharField(max_length=100, null=True, blank=True)


@receiver(post_save, sender=ContactModel)
def create_user(instance, created, **kwargs):
    if created:
        time.sleep(60)
