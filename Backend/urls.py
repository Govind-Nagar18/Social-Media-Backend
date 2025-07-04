from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('', lambda request: JsonResponse({'message': 'Welcome to the Social Media API!'})),
    path('post/', include('myapp.urls')),
    path('register/', include('Custom_auth.urls')),
    path('admin/', admin.site.urls),
] 

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

