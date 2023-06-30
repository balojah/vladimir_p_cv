import json

from django.test import TestCase, override_settings
from django.core import mail
from django.urls import reverse
from unittest.mock import patch

from .models import ContactModel
from .views import BaseHomeView


class HomeURLTestCase(TestCase):

    def test_root_url_return_200(self):
        """
        Test that the root of the site
        return correct response and template
        """
        response = self.client.get(reverse('home_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.view_class, BaseHomeView)
        self.assertTemplateUsed(response, 'my_cv/home/index.html')

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch('vitae.tasks.send_email.delay')
    def test_post_ok_with_email_sent(self, mock_email):
        """
        Test that on model creation, post_save signal
        triggers celery task with proper mail sent
        """
        model = ContactModel.objects.create(title='Greetings!', subject='Contact me.')
        mock_email.assert_called_once_with(model.title, model.subject, None, None)
        mail.send_mail(subject=model.title,
                       message=model.subject,
                       from_email='test@gmail.com',
                       recipient_list=['test@gmail.com'])
        self.assertTrue(mock_email.called)
        response = self.client.post(reverse('home_view'),
                                    data=json.dumps({'title': model.subject,
                                                    'subject': model.title}),
                                    content_type='application/json', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].body, 'Contact me.')
        self.assertEqual(mail.outbox[0].subject, 'Greetings!')
