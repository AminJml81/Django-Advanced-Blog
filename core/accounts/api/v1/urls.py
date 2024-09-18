from django.urls import path, include

from . import views


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistraionAPIView.as_view(), name='registarion')
    # change password
    # reset password
    # login token
    # login jwt
]
