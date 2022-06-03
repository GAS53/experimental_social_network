from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path('mainapp', views.MainPageView.as_view(), name="main_page"),
]
