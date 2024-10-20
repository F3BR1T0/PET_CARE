"""
URL configuration for pet_care_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from pet_owners.api import viewsets as petownerviewsets
from account.api import viewsets as accountviewsets
from pet.api import viewsets as petviewsets

route = routers.DefaultRouter()

route.register(r'pets', petviewsets.PetViewSet, basename="pets")
route.register(r'pets/medicalhistory', petviewsets.PetMedicalHistoryViewSet, basename="pets-medical-history")
route.register(r'pets/medicalhistory/vacinas', petviewsets.PetMedicalHistoryVacinaViewSet, basename="pets-medical-history-vacinas")
route.register(r'petowners', petownerviewsets.PetOwnersViewSet , basename="PetOwner")
route.register(r'petowners/address', petownerviewsets.PetOwnerAddressViewSet, basename="PetOwner address")
route.register(r'private/petowners', petownerviewsets.PetOwnersAdminViewSet, basename="PetOwner admin")
route.register(r'petowners/extra', petownerviewsets.PetOwnersExtraViewSet, basename="PetOwner extra")
route.register(r'accounts/public', accountviewsets.AccountNotAuthenticatedViewSet, basename='Account')
route.register(r'accounts/auth', accountviewsets.AccountAuthenticatedViewSet, basename='Account authenticated')
route.register(r'private/accounts', accountviewsets.AccountAdminViewSet, basename="Account admin")

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(route.urls)),
]
