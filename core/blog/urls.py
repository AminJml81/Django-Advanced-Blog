from django.urls import path, include
from blog.views import (
    PostListView, PostDetailView, PostCreateView, PostEditView, PostDeleteView,)


app_name='blog'

urlpatterns = [
    path('', PostListView.as_view() , name='post-list'),
    path('<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('api/v1/', include('blog.api.v1.urls')),
]
