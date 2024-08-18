import django_filters
from .models import VolunteerOpportunity

class VolunteerOpportunityFilter(django_filters.FilterSet):
    class Meta:
        model = VolunteerOpportunity
        fields = {
            'location': ['exact', 'icontains'],
        }

