from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name='poll'
urlpatterns = [
    path('', views.PollCreateAPIView.as_view(), name='Poll-list'),
    path('<int:pk>/', views.PollDetailAPIView.as_view(), name='Poll-detail'),
    path('<int:pk>/update/', views.PollUpdateAPIView.as_view(), name='Poll-update'),
    path('<int:pk>/delete/', views.PollDeleteAPIView.as_view(), name='Poll-delete'),
    path('parties/', views.PartiesCreateAPIView.as_view(), name='parties-list'),
    path('parties/<int:pk>/', views.PartiesDetailAPIView.as_view(), name='parties-detail'),
    path('parties/<int:pk>/update/', views.PartiesUpdateAPIView.as_view(), name='parties-update'),
    path('parties/<int:pk>/delete/', views.PartiesDeleteAPIView.as_view(), name='parties-delete'),
    

]
