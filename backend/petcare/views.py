from rest_framework import routers

from .api.viewsets import *

route = routers.DefaultRouter()

route.register(r'owner', OwnerViewSet, basename="owner")
route.register(r'pet', PetViewSet, basename="pet")
route.register(r'pet', PetMedicalHistoryViewSet, basename="pet-medical-history")
route.register(r'clinic', ClinicNotAuthenticatedViewSet, basename="clinic-notauthenticated")
route.register(r'vet', VetNotAuthenticatedViewSet, basename="vet-notauthenticated")
route.register(r'vet', VetViewSet, basename="vet")
route.register(r'vet/clinic', VetClinicViewSet, basename="vet-clinic")
route.register(r'vet/pets', VetPetViewSet, basename="vet-pets")
