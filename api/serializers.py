'''

        import serializers from rest_framework
        and models from api app

'''

from rest_framework import serializers
from api import models


class RandomSerializer(serializers.ModelSerializer):
    '''

        A serializer for the RandonUUID model


    '''
    class Meta:
        model = models.RandomUUID
        fields = '__all__'
