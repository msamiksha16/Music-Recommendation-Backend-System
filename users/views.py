from rest_framework import generics
from .models import UserProfile
from .serializers import UserSerializer
from rest_framework.views import APIView

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserProfile

class UserCreateUpdateView(APIView):
    def post(self, request):
        email = request.data.get("email")

        # Check if user exists
        try:
            user = UserProfile.objects.get(email=email)
            serializer = UserSerializer(user, data=request.data, partial=True)
        except UserProfile.DoesNotExist:
            serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserRetrieveView(generics.RetrieveAPIView):
    """
    GET /users/{user_id}/
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

