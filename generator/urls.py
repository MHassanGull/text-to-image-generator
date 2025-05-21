from django.urls import path
from .views import generate_image_view
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('api/generate-image/', generate_image_view, name='generate_image'),
]
