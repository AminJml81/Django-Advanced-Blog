from django.urls import path

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import obtain_auth_token

from ..views import (
    RegistraionAPIView,
    CustomAuthToken,
    CustomDiscardAuthToken,
    CustomTokenObtainPairView,
    ChangePasswordGenericView,
    # ProfileGenericView,
    # AccountSendEmail,
    ActivationAPiView,
    ActivationResendAPIView,
)


urlpatterns = [
    # registration
    path("registration/", RegistraionAPIView.as_view(), name="registarion"),
    # change password
    path(
        "change-password/", ChangePasswordGenericView.as_view(), name="change-password"
    ),
    # reset password
    # user activation
    # path('actiavtion/test/', AccountSendEmail.as_view(), name='send_email'),
    path(
        "activation/confirm/<str:token>/",
        ActivationAPiView.as_view(),
        name="activation",
    ),
    path(
        "activation/resend/",
        ActivationResendAPIView.as_view(),
        name="activation-resend",
    ),
    # login token
    path("token/login/", CustomAuthToken.as_view(), name="token-login"),
    path("token/logout/", CustomDiscardAuthToken.as_view(), name="token-logout"),
    # login jwt
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
