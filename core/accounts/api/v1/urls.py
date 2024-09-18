from django.urls import path, include

# from rest_framework.authtoken.views import obtain_auth_token

from . import views


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistraionAPIView.as_view(), name='registarion'),
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    # change password
    # reset password
    # login token
    # login jwt
]
