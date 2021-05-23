''' 

         import the django admin, path and include 

'''
from django.contrib import admin
from django.urls import path, include


# Root Url
# which includes the api urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cowrywise/api/v1/', include('api.urls')),
]
