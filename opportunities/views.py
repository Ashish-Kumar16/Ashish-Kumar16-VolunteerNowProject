from rest_framework import generics, filters, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import VolunteerOpportunity, Application, Donation, Organization
from .serializers import (
    VolunteerOpportunitySerializer,
    ApplicationSerializer,
    DonationSerializer,
    OrganizationSerializer,
)
from .permissions import IsAdminOrUserCreateOnly


# Pagination Class
class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Organization Views
class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination

    @swagger_auto_schema(
        operation_summary="List or Create Organizations",
        operation_description="Retrieve all organizations or create a new one.",
        responses={
            200: openapi.Response("List of organizations", OrganizationSerializer(many=True)),
            201: openapi.Response("Organization created successfully", OrganizationSerializer),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a New Organization",
        operation_description="Provide organization details to create a new one.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OrganizationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Retrieve, Update, or Delete an Organization",
        operation_description="Fetch, modify, or remove an organization using its ID.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# Volunteer Opportunity Views
class VolunteerOpportunityListCreate(generics.ListCreateAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['organization']
    search_fields = ['location']
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardPagination

    @swagger_auto_schema(
        operation_summary="List or Create Volunteer Opportunities",
        operation_description="Retrieve all opportunities or create a new one. Filter by organization or search by location.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VolunteerOpportunityRetrieve(generics.RetrieveAPIView):
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer

    @swagger_auto_schema(
        operation_summary="Retrieve a Volunteer Opportunity",
        operation_description="Fetch detailed information about a specific volunteer opportunity using its ID.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# Application Views
class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAdminOrUserCreateOnly]

    @swagger_auto_schema(
        operation_summary="Create a Volunteer Application",
        operation_description="Submit an application for a volunteer opportunity.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ApplicationAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Admin Access to Applications",
        operation_description="Allows admin users to retrieve, update, or delete a volunteer application.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# Donation Views
class DonationCreate(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Create a Donation",
        operation_description="Submit a donation for an organization or cause.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
