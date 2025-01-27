from django.urls import path
from .views import (
    OrganizationListCreate,
    OrganizationRetrieveUpdateDestroy,
    VolunteerOpportunityListCreate,
    VolunteerOpportunityRetrieve,
    ApplicationCreate,
    ApplicationAdminView,
    DonationCreate,
)

urlpatterns = [
    path('organizations/', OrganizationListCreate.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroy.as_view(), name='organization-detail'),
    path('volunteer-opportunities/', VolunteerOpportunityListCreate.as_view(), name='volunteer-opportunity-list-create'),
    path('volunteer-opportunities/<int:pk>/', VolunteerOpportunityRetrieve.as_view(), name='volunteer-opportunity-detail'),
    path('applications/', ApplicationCreate.as_view(), name='application-create'),
    path('applications/<int:pk>/', ApplicationAdminView.as_view(), name='application-admin'),
    path('donations/', DonationCreate.as_view(), name='donation-create'),
]
