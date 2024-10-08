from django.db import models
from django.urls import reverse

# from django.contrib.auth import get_user_model
# Create your models here.

# getting user model object
# User = get_user_model()


class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="blog/")
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:post-detail', kwargs={"pk":self.id})

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})

    def get_snippet(self):
        return self.content[0:10] + " ..."


class Category(models.Model):
    """
    this is a class to define categories for blog table
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
