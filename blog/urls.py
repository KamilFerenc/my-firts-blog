from django.urls import path
from . import views  # import from localdirectory

urlpatterns = [path('', views.post_list, name='post_list'),
               ]

