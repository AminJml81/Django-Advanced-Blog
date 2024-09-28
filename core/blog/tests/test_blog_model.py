from django.test import TestCase
from django.utils import timezone

from accounts.models import Profile, User
from blog.models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@mail.com',
            password = 'testpassword'
        ) 
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'first name',
            last_name = 'last name',
            description = 'test description'
        )
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile, 
            title = 'test title',
            content = 'test content',
            status = True,
            category = None,
            published_date = timezone.now()
        )
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.content, 'test content')
        self.assertEqual(post.status, True)