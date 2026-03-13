from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='lessons/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
TITLE_CHOICES = [
    ('English Educator', 'English Educator'),
    ('ESL Specialist', 'ESL Specialist'),
    ('Literature Mentor', 'Literature Mentor'),
    ('Writing Coach', 'Writing Coach'),
]
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g. Senior English Educator")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_pics/')
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name