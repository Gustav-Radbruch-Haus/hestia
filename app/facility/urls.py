from django.urls import path
from facility import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('dorm/', views.DormView.as_view(), name='hello'),
]