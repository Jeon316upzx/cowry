''' 
        import models from and uuid

'''

from django.db import models
import uuid


class RandomUUID(models.Model):
    ''' 

       Create a RandomUUID model that has 
       created_date : added automatically 
       id: uuid is set as primary key



    '''
    created_date = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return "{}".format(self.id)
