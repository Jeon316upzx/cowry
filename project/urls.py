''' 

         import the django admin, path and include 

'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Root Url
# which includes the api urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cowrywise/api/v1/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
