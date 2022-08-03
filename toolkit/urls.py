from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('toolkit/', views.ToolList.as_view(), name='tools'),
    path('<slug:slug>/', views.ToolDetail.as_view(), name='tool_detail'),
    path('like/<slug:slug>/', views.ToolLike.as_view(), name='tool_likes'),
    path('toolkit/mytools/', views.MyToolsView.as_view(), name='mytools'),
    path('mytools/addtool/', views.AddTool.as_view(), name='addtool'),
    path('edit/<tool_id>/', views.EditTool.as_view(), name='edit_tool'),
    path('delete/<tool_id>/', views.delete_tool, name='delete_tool'),
]
