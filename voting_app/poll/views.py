from rest_framework import generics

from .models import Parties, Poll
from .serializers import PollSerializer, PartySerializer
from api.permissions import IsStaffEditorPermission

from api.authentication import TokenAuthentication

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin




## listcreate does both list and create
class PollCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Poll.objects.all()
    
    serializer_class = PollSerializer

    

    def perform_create(self, serializer):
        print(self.request.data.get('voted'))
        voted = self.request.data.get('voted')
        voted = Parties(voted)
        serializer.save(owner = self.request.user, voted= voted)
        

class PollDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    

class PollUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'pk'


class PollDeleteAPIView(UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):

    queryset = Poll.objects.all()
    

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class PartiesCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Parties.objects.all()
    
    serializer_class = PartySerializer


    def perform_create(self, serializer):
        
        serializer.save(owner = self.request.user)
        

class PartiesDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):

    queryset = Parties.objects.all()
    serializer_class = PartySerializer
    

class PartiesUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Parties.objects.all()
    serializer_class = PartySerializer
    lookup_field = 'pk'

    



class PartiesDeleteAPIView(UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):

    queryset = Parties.objects.all()
    

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)