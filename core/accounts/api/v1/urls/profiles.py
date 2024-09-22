from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token

from ..views import ProfileGenericView


urlpatterns = [
    # profile
    path("profile/", ProfileGenericView.as_view(), name="profile"),
]
