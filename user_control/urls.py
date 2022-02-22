from django.urls import path, include
from .views import LoginView, RegisterView, RefreshView, UserProfileView


urlpatterns = [
    path('profile/', UserProfileView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('refresh/', RefreshView.as_view()),
]