from abc import ABC

from celery import shared_task, Task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from my_cv.settings import EMAIL_HOST_USER

logger = get_task_logger(__name__)


class BaseTaskWithRetry(Task, ABC):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True


@shared_task(bind=True, base=BaseTaskWithRetry)
def send_email(self, title, subject, email, contacts, *args):
    send_mail(subject=title,
              message=f'{subject = }\n, {email = }\n, {contacts = }',
              from_email=EMAIL_HOST_USER,
              recipient_list=[EMAIL_HOST_USER])
