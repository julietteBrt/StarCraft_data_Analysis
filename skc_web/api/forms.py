from django import forms
from .models import SkillModel

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'
