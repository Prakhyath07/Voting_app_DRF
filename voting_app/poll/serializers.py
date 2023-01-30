from rest_framework import serializers

from rest_framework.reverse import reverse

from .models import Poll, Parties


class UserPublicSerializer(serializers.Serializer):

    username = serializers.CharField(read_only = True)
    # id = serializers.IntegerField(read_only = True)

class PartySerializer(serializers.ModelSerializer):

    # owner = UserPublicSerializer( read_only = True)

    class Meta:
        model = Parties

        fields = [
            # 'owner',
            'party',
            'pk',
            # 'public',
            # 'created_at',
            # 'updated_at',
        ]


class PollSerializer(serializers.ModelSerializer):
   
    owner = UserPublicSerializer( read_only = True)
    
    # voted = PartySerializer(read_only = False)
    # voted = serializers.CharField(source = 'voted.party')
    class Meta:
        model = Poll

        fields = [
            'owner',
            'voted',
            'pk',
            'public',
            # 'created_at',
            # 'updated_at',
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        
        rep['voted'] = instance.voted.party
        return rep
    
    
    