from rest_framework.test import APIClient

from django.urls import reverse
from django.utils import timezone

from accounts.models import User

import pytest

from blog.models import Post

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email = 'test@mail.com',
        password = 'testtest123321',
        is_verified = True
    )
    return user

@pytest.mark.django_db
class TestPostAPI():


    def test_get_post_response_200_status(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    
    def test_create_post_response_401_status(self, api_client):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title': 'test title' ,
            'content': 'test content',
            'status': True ,
            'published_date': timezone.now()
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 401

    def test_create_post_response_valid_data_201_status(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title': 'test title' ,
            'content': 'test content',
            'status': True ,
            'published_date': timezone.now()
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data=data)
        assert response.status_code == 201

    def test_create_post_response_invalid_data_400_status(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title': 'test title' ,
            'content': 'test content',
            'status': True ,
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data=data)
        assert response.status_code == 400