from django.test import TestCase, override_settings, RequestFactory
from django.urls import reverse
from django.contrib.messages.storage.fallback import FallbackStorage

from unittest.mock import patch

from .models import ContactModel
from .views import BaseHomeView


class HomeURLTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()

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
    @patch('vitae.tasks.send_mail')
    def test_post_ok_with_email_sent(self, mock_email):
        """
        Test that on model creation post_save signal
        triggers celery task with proper mail sent
        """

        request = self.factory.post(reverse('home_view'),
                                    data={'title': "Greetings!",
                                          'subject': "Contact me."})

        setattr(request, 'session', 'session')
        setattr(request, '_messages', FallbackStorage(request))

        response = BaseHomeView.as_view()(request)
        args, kwargs = mock_email.call_args

        self.assertEqual(ContactModel.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(mock_email.called)
        self.assertEqual(kwargs['subject'], 'Greetings!')
        self.assertIn('Contact me', kwargs['message'])
