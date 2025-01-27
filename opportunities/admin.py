from django.contrib import admin
from .models import Organization, VolunteerOpportunity, Application, Donation

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'city', 'state', 'country', 'phone', 'website')
    search_fields = ('organization_name', 'city', 'state', 'phone')
    list_filter = ('state', 'country')
    fieldsets = (
        ('General Information', {
            'fields': ('organization_name', 'mission_statement', 'organization_description', 'organization_photo')
        }),
        ('Address', {
            'fields': ('address_line_1', 'city', 'state', 'zip_code', 'country')
        }),
        ('Contact Information', {
            'fields': ('phone', 'website', 'linkedin_url', 'facebook_url', 'twitter_url')
        }),
    )

@admin.register(VolunteerOpportunity)
class VolunteerOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization_name', 'is_remote', 'location', 'start_date', 'end_date')
    search_fields = ('title', 'location', 'organization__organization_name')
    list_filter = ('is_remote', 'start_date', 'end_date', 'country', 'city')
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'organization', 'description', 'is_remote', 'cause_areas', 'requirement', 'skills')
        }),
        ('Location Details', {
            'fields': ('location', 'country', 'address_line_1', 'city', 'zip_code', 'timezone')
        }),
        ('Timing', {
            'fields': ('start_date', 'end_date', 'start_time', 'end_time')
        }),
    )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'applicant_email', 'opportunity')
    search_fields = ('applicant_name', 'applicant_email', 'opportunity__title')
    list_filter = ('opportunity',)
    fieldsets = (
        ('Application Details', {
            'fields': ('opportunity', 'applicant_name', 'applicant_email')
        }),
    )

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_email', 'organization', 'amount')
    search_fields = ('donor_name', 'donor_email', 'organization__organization_name')
    list_filter = ('organization',)
    fieldsets = (
        ('Donation Details', {
            'fields': ('organization', 'amount', 'donor_name', 'donor_email')
        }),
    )
