"""restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toys/', include('toys.urls')),
    path('v1/drones/', include(('drones.urls', 'dronesV1'), namespace='v1')),
    path('v2/drones/', include(('drones.v2.urls', 'dronesV2'), namespace='v2')),
    path('v1/api-auth/', include(('rest_framework.urls', 'authV1'), namespace='rest_framework_v1')),
    path('v2/api-auth/', include(('rest_framework.urls', 'authV2'), namespace='rest_framework_v2')),
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('v2/api-token-auth/', obtain_auth_token, name='api_token_auth')
]
