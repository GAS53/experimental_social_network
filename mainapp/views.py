from django.views.generic import TemplateView, View, ListView, CreateView, DetailView, DeleteView


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class My_pageView(TemplateView):
    template_name = 'mainapp/im.html'

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'



