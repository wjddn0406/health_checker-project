from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'survey'

urlpatterns = [
    path('', views.survey_form, name='survey_form'), 
    path('feedback/', views.feedback_view, name='feedback_view'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='survey/login.html'), name='login'),
]