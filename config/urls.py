from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls), # убрать потом
    path('', RedirectView.as_view(url='mainapp')),
    path("mainapp/", include("mainapp.urls")),
    
]