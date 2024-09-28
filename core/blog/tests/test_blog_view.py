from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import Profile, User
from blog.models import Post


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@mail.com", password="testpassword"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="first name",
            last_name="last name",
            description="test description",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test title",
            content="test content",
            status=True,
            category=None,
            published_date=timezone.now(),
        )

    def test_blog_post_list_url_logged_in_user_response(self):
        url = reverse("blog:post-list")
        response = self.client.get(url)
        # 302 because it redirects to login page
        self.assertEqual(response.status_code, 302)

    def test_blog_post_list_url_not_logged_in_user_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertContains(response, "blog posts")
