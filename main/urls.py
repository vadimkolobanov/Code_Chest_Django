from django.urls import path
from main.filters import ProjectsLanguageLevelFiltersView
from main.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('api/projects/<str:language>/<str:level>/', ProjectsLanguageLevelFiltersView.as_view()),
]
