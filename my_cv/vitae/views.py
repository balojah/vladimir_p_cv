from django.views.generic.base import TemplateView, View
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .utils import to_pdf


class BaseHomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'my_cv/home/index.html'


class ModalFormView(View):
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        return render(self.request, 'my_cv/home/modal_form.html')
