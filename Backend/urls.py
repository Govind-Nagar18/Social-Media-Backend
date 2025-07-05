from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: JsonResponse({'message': 'Welcome to the Social Media API!'})),
    path('post/', include('myapp.urls')),
    path('register/', include('Custom_auth.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



