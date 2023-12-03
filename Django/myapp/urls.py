from django.urls import path
from .views import (education_list, education_create, education_update, education_delete,
                    experience_list, experience_create, experience_update, experience_delete,
                    resume_detail, resume_create, resume_update, resume_delete, resume_list, skill_list,
                    skill_create, skill_update, skill_delete, category_list, category_create, category_update,
                    category_delete, project_list, project_create, project_detail, project_update, project_delete)

app_name = 'myapp'
urlpatterns = [
    # Education URLs
    path('education/', education_list, name='education_list'),
    path('education/create/', education_create, name='education_create'),
    path('education/<int:pk>/update/', education_update, name='education_update'),
    path('education/<int:pk>/delete/', education_delete, name='education_delete'),

    # Experience URLs
    path('experience/', experience_list, name='experience_list'),
    path('experience/create/', experience_create, name='experience_create'),
    path('experience/<int:pk>/update/', experience_update, name='experience_update'),
    path('experience/<int:pk>/delete/', experience_delete, name='experience_delete'),

    # Resume URLs
    path('resumes/', resume_list, name='resume_list'),
    path('resumes/<int:pk>/', resume_detail, name='resume_detail'),
    path('resumes/create/', resume_create, name='resume_create'),
    path('resumes/<int:pk>/update/', resume_update, name='resume_update'),
    path('resumes/<int:pk>/delete/', resume_delete, name='resume_delete'),

    # Skill URLs
    path('skills/', skill_list, name='skill_list'),
    path('skills/create/', skill_create, name='skill_create'),
    path('skills/<int:pk>/update/', skill_update, name='skill_update'),
    path('skills/<int:pk>/delete/', skill_delete, name='skill_delete'),

    # Category URLs
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/update/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),

    # Project
    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/<int:pk>/update/', project_update, name='project_update'),
    path('projects/<int:pk>/delete/', project_delete, name='project_delete'),
    # Add paths for other models like AboutMe, ContactInfo, SocialMediaLink, Project if needed
]
