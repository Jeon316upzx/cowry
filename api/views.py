
''' 
    
    import rest_framework(permissions, Response , APIView ) 
    serializers and models

'''

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from api import models


class GenerateRandomUUID(APIView):
    """

       API endpoint creates a new instance of random RandomUUID with 
       id and created_date and returns the data in the format.

       {

        "2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"

        "2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",

        "2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",

      }

    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.RandomSerializer

    def get(self, request, *args, **kwargs):

        # serialize and save data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Retrieve all the instances of RandomUUID
        # and order in a descending manner
        queryset = models.RandomUUID.objects.all().order_by('-created_date')

        # create a dictionary
        my_dict = dict()

        # using a for loop or list comprehension
        # format each instance of data from queryset
        for data in queryset:
            my_dict[data.created_date.strftime(
                "%Y-%m-%d %H:%M:%S")] = str(data.id)
        return Response(my_dict)
