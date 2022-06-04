from django.urls import path
from authorisation import views
from django.views.generic import RedirectView

app_name = 'authorisation'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    ]

