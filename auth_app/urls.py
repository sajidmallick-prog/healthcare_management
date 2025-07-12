# auth_app/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProtectedView, LogoutView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),
]