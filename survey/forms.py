from django import forms
from .models import UserSurvey
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SurveyForm(forms.ModelForm):
    class Meta:
        model = UserSurvey
        fields = [
            
            'stress_score',
            'energy_level',
            'emotion_intensity',
            'relationship_discomfort_score',
            'self_care_satisfaction',
            'focus_level',
            'goal_achievement',
            ]
        widgets = {
           
            'stress_score': forms.RadioSelect,
            'energy_level': forms.RadioSelect,
            'emotion_intensity': forms.RadioSelect,
            'relationship_discomfort_score': forms.RadioSelect,
            'self_care_satisfaction': forms.RadioSelect,
            'focus_level': forms.RadioSelect,
            'goal_achievement': forms.RadioSelect,
        }
       
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)