from django.urls import path
from . import views

app_name = 'start'

urlpatterns = [
    path('', views.Front.as_view(), name='Front'),
]
