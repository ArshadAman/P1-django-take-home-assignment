from django.db import models
import uuid

class FoodTruck(models.Model):
    locationid = models.CharField(max_length=50, blank=True, null=True)
    Applicant = models.CharField(max_length=100, blank=True, null=True)
    FacilityType = models.CharField(max_length=255, blank=True, null=True)
    cnn = models.CharField(max_length=255, blank=True, null=True)
    LocationDescription = models.CharField(max_length=255, blank=True, null=True)
    blocklot = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=255, blank=True, null=True)
    Iot = models.CharField(max_length=255, blank=True, null=True)
    Status = models.CharField(max_length=255, blank=True, null=True)
    FoodItems = models.CharField(max_length=255, blank=True, null=True)
    X = models.CharField(max_length=255, blank=True, null=True)
    Y = models.CharField(max_length=255, blank=True, null=True)
    Schedule = models.CharField(max_length=255, blank=True, null=True)
    dayshours = models.CharField(max_length=255, blank=True, null=True)
    NOISent = models.CharField(max_length=255, blank=True, null=True)
    Approved = models.CharField(max_length=255, blank=True, null=True)
    Received = models.CharField(max_length=255, blank=True, null=True)
    PriorPermit = models.CharField(max_length=255, blank=True, null=True)
    ExpirationDate = models.CharField(max_length=255, blank=True, null=True)
    Location = models.CharField(max_length=255, blank=True, null=True)
    Zip_Codes = models.CharField(max_length=255, blank=True, null=True)
    Neighborhoods = models.CharField(max_length=255, blank=True, null=True)
    Supervisor_Districts = models.CharField(max_length=255, blank=True, null=True)
    Police_Districts = models.CharField(max_length=255, blank=True, null=True)
    Fire_Prevention_Districts = models.CharField(max_length=255, blank=True, null=True)
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    permit = models.CharField(max_length=50, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    
    def __str__(self):
        return f"{self.Applicant} - {self.locationid}"
