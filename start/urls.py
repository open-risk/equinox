from django.conf.urls import url
from . import views

app_name = 'start'

urlpatterns = [
    url(r'^$', views.Front.as_view(), name='Front'),
]