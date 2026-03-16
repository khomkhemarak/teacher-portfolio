from django.db import models

# Note: We removed the admin.site.register lines from here. 
# They belong in admin.py!

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g. Senior English Educator")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_pics/')
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="Teaching")

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    image = models.ImageField(upload_to='education_logo/', blank=True, null=True)
    gif = models.URLField(max_length=500, blank=True, null=True, help_text="Paste a GIF URL here (e.g., Giphy link)")
    
    def __str__(self):
        return self.degree