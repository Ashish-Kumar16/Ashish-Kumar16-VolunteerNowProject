from rest_framework import serializers
from .models import VolunteerOpportunity, Application, Donation, Organization

# from rest_framework import serializers
# from .models import Organization, VolunteerOpportunity

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def validate(self, data):
        # Example custom validation
        if 'state' not in data:
            raise serializers.ValidationError({"state": "This field is required."})
        return data

class VolunteerOpportunitySerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField()

    class Meta:
        model = VolunteerOpportunity
        fields = [
            'id', 'title', 'organization_name', 'description', 'is_remote', 'location', 'country',
            'address_line_1', 'cause_areas', 'requirement', 'skills', 'city', 'zip_code', 'timezone',
            'start_date', 'end_date', 'start_time', 'end_time'
        ]

    def get_organization_name(self, obj):
        return obj.organization.organization_name if obj.organization else None

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'opportunity', 'applicant_name', 'applicant_email']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'organization', 'amount', 'donor_name', 'donor_email']