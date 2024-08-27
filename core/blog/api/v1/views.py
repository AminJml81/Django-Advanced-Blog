from rest_framework.views import APIView
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly)
from django.shortcuts import get_object_or_404
from blog.api.v1.serializers import PostSerializer
from blog.models import Post


# @api_view(['GET', "POST"])
# @permission_classes([IsAuthenticated])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#         # else:
#         #     return Response(serializer.errors)

# @api_view(['GET','PUT', "DELETE"])
# def post_detail(request, id):
#     #try:
#     post = get_object_or_404(Post, pk=id)
#     if request.method == 'GET':
#         post = PostSerializer(post).data
#         return Response(post)
    
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)

    # except Post.DoesNotExist:
    #     return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)



# class PostListCreate(APIView):
#     """getting a list of posts and creating new posts"""

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request):
#         """getting list of all posts"""
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         """creating a post with provided data"""
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

# class PostDetail(APIView):
#     """Getting Detail of post, edit and delete"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         """getting post"""
#         post = get_object_or_404(Post, pk=id, status=True)
#         post = self.serializer_class(post)
#         return Response(post.data)
    

#     def put(self, request, id):
#         """updating post via put method"""
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

#     def delete(self, request, id):
#         """deleting post"""
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({'detail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
class PostListCreate(ListCreateAPIView):
    """getting a list of posts and creating new posts"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    #serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    lookup_field = 'id'