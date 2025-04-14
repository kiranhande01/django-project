from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),  # Add more roles as needed
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class District(models.Model):
    name = models.CharField(max_length=100)
    boundary = models.JSONField(null=True, blank=True)  # GeoJSON data for district boundary
    
    def __str__(self):
        return self.name

class Tahsil(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    boundary = models.JSONField(null=True, blank=True)  # GeoJSON data for tahsil boundary
    
    def __str__(self):
        return f"{self.name} ({self.district})"

class Village(models.Model):
    name = models.CharField(max_length=100)
    tahsil = models.ForeignKey(Tahsil, on_delete=models.CASCADE)
    boundary = models.JSONField(null=True, blank=True)  # GeoJSON data for village boundary
    
    def __str__(self):
        return f"{self.name} ({self.tahsil})"

class Project(models.Model):
    name = models.CharField(max_length=200)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, default=1)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    polygon_data = models.JSONField(null=True, blank=True)  # GeoJSON for project polygon
    
    def __str__(self):
        return self.name








