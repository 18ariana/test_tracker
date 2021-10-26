from djoser.views import UserViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from fitness_tracker.models import *
from fitness_tracker.serializers import *
from fitness_tracker.filters import *

 
class ActivateUser(UserViewSet):

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActivityCreateAPIView(generics.CreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

class ActivityListAPIView(generics.ListAPIView):
    serializer_class = ActivityListSerializer
    filter_backends = (ActivityFilterBackend, )
    
    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)