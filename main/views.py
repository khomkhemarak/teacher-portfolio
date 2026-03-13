from django.shortcuts import render
from .models import Profile, Lesson

def home(request):

    profile = Profile.objects.first()
    lessons = Lesson.objects.all().order_by('-date_created')


    context = {
        'profile': profile,
        'lessons': lessons,
    }
    return render(request, 'main/index.html' , context)