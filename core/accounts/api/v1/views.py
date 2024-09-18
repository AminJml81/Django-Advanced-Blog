from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistrationSerializer


class RegistraionAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        user_data = request.data
        serializer = RegistrationSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_email = serializer.validated_data['email']
            data = {
                'email': user_email 
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)