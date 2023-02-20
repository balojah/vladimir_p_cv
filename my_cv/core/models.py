import uuid
from django.db import models

# Base abstract models for inheritance.


class BaseDateMixin(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseAbsModel(BaseDateMixin):

    title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
