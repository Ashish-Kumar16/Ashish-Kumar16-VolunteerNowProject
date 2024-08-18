from rest_framework import generics, filters, permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import VolunteerOpportunity, Application, Donation, Organization
# from .serializers import VolunteerOpportunitySerializer, ApplicationSerializer, DonationSerializer, OrganizationSerializer
# from .filters import VolunteerOpportunityFilter

# # class OrganizationListCreate(generics.ListCreateAPIView):
# #     queryset = Organization.objects.all()
# #     serializer_class = OrganizationSerializer
# #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# class OrganizationListCreate(generics.ListCreateAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Optional

# class OrganizationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  
    
# class VolunteerOpportunityListCreate(generics.ListCreateAPIView):
#     queryset = VolunteerOpportunity.objects.all()
#     serializer_class = VolunteerOpportunitySerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#     filterset_class = VolunteerOpportunityFilter
#     search_fields = ['location']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class ApplicationCreate(generics.CreateAPIView):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class DonationCreate(generics.CreateAPIView):
#     queryset = Donation.objects.all()
#     serializer_class = DonationSerializer
#     permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import VolunteerOpportunity, Application, Donation, Organization
from .serializers import VolunteerOpportunitySerializer, ApplicationSerializer, DonationSerializer, OrganizationSerializer
from .filters import VolunteerOpportunityFilter

class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class OrganizationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class VolunteerOpportunityListCreate(generics.ListCreateAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = VolunteerOpportunityFilter
    search_fields = ['location']
    # permission_classes = [permissions.IsAuthenticated]
class VolunteerOpportunityRetrieve(generics.RetrieveAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    
class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DonationCreate(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    # Removed permission_classes, meaning it is open to all
