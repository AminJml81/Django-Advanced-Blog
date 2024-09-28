from django.test import TestCase, SimpleTestCase
from django.utils import timezone

from ..models import Category
from ..forms import PostForm


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category = Category.objects.create(name='test')
        form = PostForm(data={
            'title': 'test title',
            'content': 'test content',
            'status': True,
            'category': category,
            'published_date': timezone.now() 
        })
        self.assertTrue(form.is_valid())


    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())