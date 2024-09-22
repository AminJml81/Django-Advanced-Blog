from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.api.v1 import views

app_name = "api-v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")

# urlpatterns = [
#     #path('post/', views.post_list, name='post-list'),
#     #path('post/', views.PostListCreate.as_view(), name='post-list-create'),
#     #path('post/', views.PostListCreate.as_view(), name='post-list-create'),
#     #path('post/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post_list'),
#     #path('post/<int:id>/', views.post_detail, name='post-detail'),
#     #path('post/<int:id>/', views.PostDetail.as_view(), name='post-detail'),
#     #path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='post_detail')

# ]

urlpatterns = router.urls
