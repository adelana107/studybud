from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name = 'login'),
     path('register/', views.registerPage, name = 'register'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('', views.home, name = 'home'),
    path('room/<int:pk>/', views.room, name = 'room'),
    path('profile/<int:pk>/', views.userProfile, name='user-profile'),
    path('create-room/', views.createRoom, name = 'create-room'),
    path('edit/<int:pk>/', views.editRoom, name='edit'),
    path('delete/<int:pk>/', views.deleteRoom, name='delete'),
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete-message'),
    path('update-user/<int:pk>/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]