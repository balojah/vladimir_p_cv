from django.views.generic import CreateView
from .forms import ContactForm


class BaseHomeView(CreateView):
    http_method_names = ['get', 'post']
    form_class = ContactForm
    template_name = 'my_cv/home/index.html'
    success_url = '/'
