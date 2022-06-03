from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['x'] = 'Передача контекстом' # пеерменная в шаблоне <p>{{ x }}</p>
        return context
