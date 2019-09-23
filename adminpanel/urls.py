from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('data/', include('adminapp.urls')),
    path('', admin.site.urls),
]
