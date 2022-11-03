from django.urls import re_path
from . import views

app_name = 'bot'

urlpatterns = [
    re_path(r'^run/$', views.BotView.as_view(), name='run'),
]
