from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm


class BaseHomeView(SuccessMessageMixin, CreateView):
    http_method_names = ['get', 'post']
    form_class = ContactForm
    template_name = 'my_cv/home/index.html'
    success_message = 'Thank you. I will contact you as soon as possible.'
    success_url = reverse_lazy('home_view')

    def post(self, request, *args, **kwargs):
        print(f'{[*request]}{args = }{kwargs = }')
        return super().post(request, *args, **kwargs)
