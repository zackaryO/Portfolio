from django.db import models


# Create your models here.

# AboutMe
class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    introduction = models.TextField()

    def __str__(self):
        return self.title


# Resume
class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.school_name


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.job_title


# Skills
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)  # Adding ManyToManyField for skills

    def __str__(self):
        return self.name


# ContactInfo
class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    # Additional fields as necessary

    def __str__(self):
        return self.email


# SocialMediaLinks
class SocialMediaLink(models.Model):
    platform_name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=100)  # Will likely change this to static storage

    def __str__(self):
        return self.platform_name


# Portfolio of Work
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
