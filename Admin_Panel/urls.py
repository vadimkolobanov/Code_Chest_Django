from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('Admin_Panel.routers')),
    path('', include('main.urls')),

]
