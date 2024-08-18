from django.urls import path
from .views import VolunteerOpportunityListCreate, ApplicationCreate, DonationCreate, OrganizationListCreate, OrganizationListCreate, OrganizationRetrieveUpdateDestroy,VolunteerOpportunityRetrieve

urlpatterns = [
    path('organizations/', OrganizationListCreate.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroy.as_view(), name='organization-detail'),
    path('opportunity/<int:pk>/', VolunteerOpportunityRetrieve.as_view(), name='opportunity-detail'),
    path('opportunities/', VolunteerOpportunityListCreate.as_view(), name='volunteer-opportunity-list-create'),
    path('applications/', ApplicationCreate.as_view(), name='application-create'),
    path('donations/', DonationCreate.as_view(), name='donation-create'),
]