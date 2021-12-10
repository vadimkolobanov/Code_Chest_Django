from django.urls import path

from main.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name='index')
]