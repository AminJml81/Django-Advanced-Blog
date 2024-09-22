from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.conf import settings

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, PyJWTError

from mail_templated import send_mail
from mail_templated import EmailMessage

from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ActivationResendSerializer,
)
from ...models import Profile
from ..utils import EmailThread


user = get_user_model()


class RegistraionAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        user_data = request.data
        serializer = RegistrationSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_email = serializer.validated_data["email"]
            user = get_object_or_404(get_user_model(), email=user_email)
            token = self.get_tokens_for_user(user)
            email = EmailMessage(
                "email/activation.tpl",
                {"token": token, "user": user},
                "blog@admin.com",
                to=[user_email],
            )
            email_thread = EmailThread(email)
            email_thread.start()
            data = {"email": user_email}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomAuthToken(ObtainAuthToken):
    # this view is for login with simple token
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    # this view is for login with jwt token, which jwt token is created
    # and for each task, token gets validated.
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordGernicView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = user
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            data = {"detail": "password changed successfully"}
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileGenericView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user.id)
        return obj


class AccountSendEmail(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # send_mail(f"Hello {request.user.email}",
        #             "Testing email.",
        #             "blog@gmail.com",
        #             ["aminbest1381@gmail.com"],
        #             fail_silently=False,)

        user = request.user
        user_email = user.email
        # send_mail('email/hello.tpl', {'user': user}, 'blog@admin.com', [user.email])
        token = self.get_tokens_for_user(user)
        email = EmailMessage(
            "email/hello.tpl",
            {"token": token, "user": user},
            "blog@admin.com",
            to=[user_email],
        )
        email_thread = EmailThread(email)
        email_thread.start()
        return Response({"detail": "email sent"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationAPiView(APIView):

    def get(self, reqeust, token, *args, **kwargs):
        try:
            decoded_token = jwt.decode(
                token, key=settings.SECRET_KEY, algorithms=["HS256"]
            )
        except InvalidTokenError:
            return Response(
                {"Token Error": "Token is not Valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ExpiredSignatureError:
            return Response(
                {"Token Error": "Token is Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except PyJWTError as e:
            return Response(
                {"Token Error": type(e).__name__}, status=status.HTTP_400_BAD_REQUEST
            )

        user_id = decoded_token.get("user_id")
        user = get_object_or_404(get_user_model(), pk=user_id)
        if not user.is_verified:
            user.is_verified = True
            user.save()
            message = f"{user.email} your account has been activated"
        else:
            message = f"{user.email} your account has already been activated!!! "
        return Response(message)


class ActivationResendAPIView(GenericAPIView):
    serializer_class = ActivationResendSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        user_email = serializer.validated_data.get("email")
        token = self.get_tokens_for_user(user)
        email = EmailMessage(
            "email/activation.tpl",
            {"token": token, "user": user},
            "blog@admin.com",
            to=[user_email],
        )
        email_thread = EmailThread(email)
        email_thread.start()
        return Response(
            {"detail": "email sent successfully"}, status=status.HTTP_201_CREATED
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
