from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ticketsystem import views

urlpatterns = [
    path('', include('ticketsystem.urls')),
    path('admin/', admin.site.urls)
     
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
