from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

app_name = 'todo'

urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name = 'vonly'),
]
