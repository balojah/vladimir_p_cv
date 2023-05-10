from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BaseAbsModel
from .tasks import send_email


class ContactModel(BaseAbsModel):
    pass


@receiver(post_save, sender=ContactModel)
def create_contact(instance, created, **kwargs):
    if created:
        send_email.delay(instance.title, instance.subject,
                         instance.email, instance.contacts)
