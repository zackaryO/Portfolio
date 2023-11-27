from django import forms
from .models import Education, Experience, Resume, Skill, Category


class DateInput(forms.DateInput):
    input_type = 'date'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company_name', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'summary', 'education', 'experience', 'skills']  # Include 'skills'
        widgets = {
            'education': forms.CheckboxSelectMultiple,
            'experience': forms.CheckboxSelectMultiple,
            'skills': forms.CheckboxSelectMultiple  # Assuming you want to use checkboxes for skills
        }

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields['education'].queryset = Education.objects.all()
        self.fields['experience'].queryset = Experience.objects.all()
        self.fields['skills'].queryset = Skill.objects.all()


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency_level', 'category']
        widgets = {
            'category': forms.Select()  # Ensure category uses a dropdown select widget
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
