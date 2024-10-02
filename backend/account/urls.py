from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from account.api.viewsets import AccountRegisterViewSet, AccountLogoutViewSet

urlpatterns = [
    path('register/', AccountRegisterViewSet.as_view({'post':'register'}), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', AccountLogoutViewSet.as_view({'post':'logout'}), name='logout'),
]