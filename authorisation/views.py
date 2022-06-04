from django.views.generic import TemplateView, View, ListView, CreateView, DetailView, DeleteView


class LoginView(TemplateView):
    template_name = 'authorisation/login.html'