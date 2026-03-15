from django.shortcuts import render
from .models import Profile, Skill, Experience, Education

def home(request):

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-id')
    educations = Education.objects.all().order_by('-year')

    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': educations,
    }
    return render(request, 'main/index.html' , context)