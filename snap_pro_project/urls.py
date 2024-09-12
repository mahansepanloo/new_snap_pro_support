
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supporter/', include('supporter.urls')),
    path('snap-pro/', include('pro_service.urls')),
]
