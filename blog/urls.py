from django.urls import path
from . import views
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
