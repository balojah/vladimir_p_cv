from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BaseAbsModel
from .tasks import send_email


class ContactModel(BaseAbsModel):

    subject = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    contacts = models.CharField(max_length=100, blank=True, null=True)


@receiver(post_save, sender=ContactModel)
def create_contact(instance, created, **kwargs):
    if created:
        send_email.delay(instance.title, instance.subject, instance.email, instance.contacts)
