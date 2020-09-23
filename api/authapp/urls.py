from django.urls import path,include
from authapp import views
from rest_framework_jwt import views as jwt_views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('',include('djoser.urls.authtoken')),
    
]

