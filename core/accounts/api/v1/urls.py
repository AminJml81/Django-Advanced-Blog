from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView,
)
 
# from rest_framework.authtoken.views import obtain_auth_token

from .views import (RegistraionAPIView, CustomAuthToken, CustomDiscardAuthToken,
                    CustomTokenObtainPairView, ChangePasswordGernicView,
                    ProfileGenericView)


app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', RegistraionAPIView.as_view(), name='registarion'),
    # change password
    path('change-password/', ChangePasswordGernicView.as_view(), name='change-password'),
    # reset password

    # login token
    path('token/login/', CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    # login jwt
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    # profile
    path('profile/', ProfileGenericView.as_view(), name='profile'),
]
