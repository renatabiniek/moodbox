from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('toolkit/', views.ToolList.as_view(), name='tools'),
]