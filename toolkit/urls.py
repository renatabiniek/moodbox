from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToolList.as_view(), name='home')
]