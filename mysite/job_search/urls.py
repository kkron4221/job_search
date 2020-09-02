from django.urls import path

from . import views

app_name = 'job_search'
urlpatterns = [
    path('', views.index, name='index'),
]