from rest_framework import generics, status
from rest_framework.response import Response



class Helloworld(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
        