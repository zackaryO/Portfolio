import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import pdfkit
from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from django.conf import settings

from .models import AboutMe, Education, Experience, Resume, ContactInfo, Skill, SocialMediaLink, Project, Category
from .forms import EducationForm, ExperienceForm, ResumeForm, SkillForm, CategoryForm, ProjectForm
from .serializers import (AboutMeSerializer, EducationSerializer, ExperienceSerializer,
                          ResumeSerializer, ContactInfoSerializer, SkillSerializer,
                          SocialMediaLinkSerializer, ProjectSerializer, CategorySerializer)


class ReadOnlyForAngularMixin:
    """
    Mixin to make viewset read-only if the request comes from the Angular client.
    """

    def get_permissions(self):
        if self.request.headers.get('X-Requested-With') == 'AngularClient':
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permission() for permission in self.permission_classes]


class AboutMeViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class EducationViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ResumeViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ContactInfoViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class SkillViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SocialMediaLinkViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer


class ProjectViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CategoryViewSet(ReadOnlyForAngularMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@login_required
def education_list(request):
    educations = Education.objects.all()
    return render(request, 'myapp/education_list.html', {'education_list': educations})


@login_required
def education_create(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:education_list')
    return render(request, 'myapp/education_form.html', {'form': form})


@login_required
def education_update(request, pk):
    education = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, instance=education)
    if form.is_valid():
        form.save()
        return redirect('myapp:education_list')
    return render(request, 'myapp/education_form.html', {'form': form})


@login_required
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('myapp:education_list')
    return render(request, 'myapp/education_confirm_delete.html', {'object': education})


@login_required
# Experience Views
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'myapp/experience_list.html', {'experience_list': experiences})


@login_required
def experience_create(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:experience_list')
    return render(request, 'myapp/experience_form.html', {'form': form})


@login_required
def experience_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid():
        form.save()
        return redirect('myapp:experience_list')
    return render(request, 'myapp/experience_form.html', {'form': form})


@login_required
@require_POST
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    experience.delete()
    return redirect('myapp:experience_list')


@login_required
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'myapp/resume_list.html', {'resume_list': resumes})


# Resume Views
@login_required
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'myapp/resume_detail.html', {'resume': resume})


@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:resume_list')
    else:
        form = ResumeForm()
    return render(request, 'myapp/resume_form.html', {'form': form})


@login_required
def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    form = ResumeForm(request.POST or None, instance=resume)
    if form.is_valid():
        form.save()
        return redirect('myapp:resume_detail', pk=pk)
    return render(request, 'myapp/resume_form.html', {'form': form})


@login_required
def download_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    html = render_to_string('myapp/resume_detail.html', {'resume': resume})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'dpi': 400
    }
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "resume.pdf"
    response['Content-Disposition', filename] = 'attachment'

    return response


@login_required
@require_POST
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resume.delete()
    return redirect('myapp:resume_list')


@login_required
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'myapp/skill_list.html', {'skill_list': skills})


@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:skill_list')
    else:
        form = SkillForm()
    return render(request, 'myapp/skill_form.html', {'form': form})


@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('myapp:skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'myapp/skill_form.html', {'form': form})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('myapp:skill_list')
    return render(request, 'myapp/skill_confirm_delete.html', {'object': skill})


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'myapp/category_list.html', {'category_list': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:category_list')
    else:
        form = CategoryForm()
    return render(request, 'myapp/category_form.html', {'form': form})


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('myapp:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'myapp/category_form.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('myapp:category_list')
    return render(request, 'myapp/category_confirm_delete.html', {'object': category})


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'myapp/project_list.html', {'project_list': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'myapp/project_form.html', {'form': form})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'myapp/project_detail.html', {'project': project})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('myapp:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'myapp/project_form.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('myapp:project_list')
    return render(request, 'myapp/project_confirm_delete.html', {'object': project})
