from django.views.generic import TemplateView, FormView
from django.shortcuts import render


class BaseHomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'my_cv/home/index.html'


class ModalFormView(FormView):
    http_method_names = ['get', 'post']
    form_class = ...

    def get(self, request, *args, **kwargs):
        return render(request, 'my_cv/home/modal_form.html')

    def form_valid(self, form):
        return super().form_valid(form)
