from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import VolunteerOpportunity, Application, Donation, Organization
from .serializers import VolunteerOpportunitySerializer, ApplicationSerializer, DonationSerializer, OrganizationSerializer
from .permissions import IsAdminOrUserCreateOnly

class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganizationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class VolunteerOpportunityListCreate(generics.ListCreateAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['location']
    permission_classes = [permissions.IsAuthenticated]

class VolunteerOpportunityRetrieve(generics.RetrieveAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAdminOrUserCreateOnly]

class ApplicationAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]

class DonationCreate(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]
