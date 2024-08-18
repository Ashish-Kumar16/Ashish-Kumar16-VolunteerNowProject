from django.db import models

# Create your models here.
from django.db import models

# class Organization(models.Model):
#     name = models.CharField(max_length=255)
#     about = models.TextField()

#     def __str__(self):
#         return self.name

class Organization(models.Model):
    STATE_CHOICES = [
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CT', 'Chhattisgarh'),
        ('DD', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HP', 'Himachal Pradesh'),
        ('HR', 'Haryana'),
        ('JH', 'Jharkhand'),
        ('JK', 'Jammu and Kashmir'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PY', 'Puducherry'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UT', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]

    COUNTRY_CHOICES = [
        ('IN', 'India'),
        # Add more countries as needed
    ]

    organization_name = models.CharField(max_length=255, verbose_name="Organization Name")
    address_line_1 = models.CharField(max_length=255, verbose_name="Address Line 1")
    mission_statement = models.TextField(blank=True, null=True, verbose_name="Mission Statement")
    organization_description = models.TextField(blank=True, null=True, verbose_name="Organization Description")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name="State")
    zip_code = models.CharField(max_length=10, verbose_name="Zip Code")
    country = models.CharField(max_length=2,blank=True, null=True, choices=COUNTRY_CHOICES, verbose_name="Country")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    website = models.URLField(blank=True, null=True, verbose_name="Website")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn URL")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook URL")
    twitter_url = models.URLField(blank=True, null=True, verbose_name="Twitter URL")
    organization_photo = models.URLField(blank=True, null=True, verbose_name="organization_photo")

    
    def __str__(self):
        return self.organization_name



class VolunteerOpportunity(models.Model):
    title = models.TextField(blank=True, null=True, verbose_name="title")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, verbose_name="description")
    is_remote = models.BooleanField(default=False)  # Corresponds to the virtual checkbox
    location = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, default='India')  # New field for country
    address_line_1 = models.CharField(max_length=255, blank=True)  # Address fields
    cause_areas = models.CharField(max_length=255, blank=True)  # Address fields
    requirement = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)  # Zip code field
    timezone = models.CharField(max_length=255, default='Asia/Calcutta')  # New field for timezone
    start_date = models.DateField(null=True)  # Start and end date fields
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True, blank=True)  # Start and end time fields
    end_time = models.TimeField(null=True, blank=True)

    @property
    def organization_name(self):
        return self.organization.organization_name
    
    def __str__(self):
        return self.title

class Application(models.Model):
    opportunity = models.ForeignKey(VolunteerOpportunity, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()

class Donation(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()