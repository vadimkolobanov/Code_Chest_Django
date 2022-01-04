from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.api_views import ProjectModelViewSet, UserProjectCompletedViewSet
from users.api_views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('users_completed_project', UserProjectCompletedViewSet)

urlpatterns = [

    path('', include(router.urls)),

]

