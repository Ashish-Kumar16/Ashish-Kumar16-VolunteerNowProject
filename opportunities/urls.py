from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import (
    OrganizationListCreate,
    OrganizationRetrieveUpdateDestroy,
    VolunteerOpportunityListCreate,
    VolunteerOpportunityRetrieve,
    ApplicationCreate,
    ApplicationAdminView,
    DonationCreate,
)

# Swagger schema view configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Volunteer Management and Donation Platform API",
        default_version="v1",
        description="API for managing organizations, volunteer opportunities, applications, and donations.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    path('organizations/', OrganizationListCreate.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroy.as_view(), name='organization-detail'),
    path('volunteer-opportunities/', VolunteerOpportunityListCreate.as_view(), name='volunteer-opportunity-list-create'),
    path('volunteer-opportunities/<int:pk>/', VolunteerOpportunityRetrieve.as_view(), name='volunteer-opportunity-detail'),
    path('applications/', ApplicationCreate.as_view(), name='application-create'),
    path('applications/<int:pk>/', ApplicationAdminView.as_view(), name='application-admin'),
    path('donations/', DonationCreate.as_view(), name='donation-create'),

    # Swagger UI endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
