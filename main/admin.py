from django.contrib import admin
from .models import Profile, Skill, Experience, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'duration')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'year','has_logo','has_profile_image')

    def has_logo(self, obj):
        return bool(obj.image)
    has_logo.boolean = True

    def has_profile_image(self, obj):
        return bool(obj.profile_image)
    has_profile_image.boolean = True