from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register', views.AccountRegister.as_view(), name='register'),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('logout', views.AccountLogout.as_view(), name='logout')
]