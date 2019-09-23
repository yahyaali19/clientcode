from django.urls import path

from adminapp.views import RepresentativeView

urlpatterns = [
    path('', RepresentativeView.as_view(), name='representative-list'),
]