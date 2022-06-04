from django.urls import path
from mainapp import views
from django.views.generic import RedirectView

app_name = 'mainapp'

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("my_page/", views.My_pageView.as_view(), name="my_page"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),


    ]