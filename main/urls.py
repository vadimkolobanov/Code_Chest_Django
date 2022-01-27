from django.urls import path
from main.filters import ProjectsLanguageLevelFiltersView
from main.views import index, main

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('main/', main, name='main'),
    path('api/projects/<str:language>/<str:level>/', ProjectsLanguageLevelFiltersView.as_view()),
]
