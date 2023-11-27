from django.contrib import admin
from .models import AboutMe, Education, Experience, Resume, ContactInfo, Skill, SocialMediaLink, Project

# Register your models here.
# username for admin: admin password: admin
admin.site.register(AboutMe)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Resume)
admin.site.register(ContactInfo)
admin.site.register(Skill)
admin.site.register(SocialMediaLink)
admin.site.register(Project)
