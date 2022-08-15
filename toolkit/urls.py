"""URL paths"""
from django.urls import path
from . import views
from .views import category_view

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('toolkit/', views.ToolList.as_view(), name='tools'),
    path('<slug:slug>/', views.ToolDetail.as_view(), name='tool_detail'),
    path('like/<slug:slug>/', views.ToolLike.as_view(), name='tool_likes'),
    path('toolkit/mytools/', views.MyToolsView.as_view(), name='mytools'),
    path('mytools/addtool/', views.AddTool.as_view(), name='addtool'),
    path('edit/<tool_id>/', views.EditTool.as_view(), name='edit_tool'),
    path('delete/<tool_id>/', views.DeleteTool.as_view(), name='delete_tool'),
    path('category/<slug:slug>/', category_view, name='categories'),
]
