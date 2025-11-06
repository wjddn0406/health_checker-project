from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg 
from datetime import timedelta, date, datetime
from .forms import SurveyForm
from .models import UserSurvey
from .forms import CustomUserCreationForm 


@login_required
def survey_form(request):
    if request.method == 'POST':
      form = SurveyForm(request.POST)
      if form.is_valid():
         survey_instance = form.save(commit=False)
         survey_instance.user = request.user
         survey_instance.save()
         return redirect('survey:feedback_view')
      
         return redirect('survey:survey_form')
    else:
      form = SurveyForm()
      return render(request, 'survey/survey_form.html', {'form': form})
    
@login_required
def feedback_view(request):
    user = request.user
    end_date = datetime.now().date() + timedelta(days=1)
    start_date = end_date - timedelta(days=7)
    seven_days_ago = date.today() - timedelta(days=7)
    today_date = date.today()
    recent_surveys = UserSurvey.objects.filter(
        user=user,
        survey_date__range=(start_date, end_date)

    ).order_by('-survey_date')

    end_date = datetime.now().date() + timedelta(days=1)
    start_date = end_date - timedelta(days=7)

    recent_surveys = UserSurvey.objects.filter(
        user=user, 
        survey_date__range=(start_date, end_date) 
    ).order_by('-survey_date')
    distinct_dates_count = recent_surveys.dates('survey_date', 'day').count()

    if distinct_dates_count < 7:
        feedback_message = f"🤔 데이터 부족! 최근 7일 중 {distinct_dates_count}일만 기록했어요. 최소 7일의 기록이 있어야 정확한 주간 피드백이 제공됩니다. 매일매일 기록해 주세요!"
        stress_avg = 0
    else:
        averages = recent_surveys.aggregate(
            avg_stress=Avg('stress_score')
        )
        stress_avg = averages['avg_stress']
        
        if stress_avg >= 4.0:
            feedback_message = f"🚨 **스트레스 비상!** 평균 {stress_avg:.1f}점으로 매우 높습니다. 잠깐이라도 밖에서 햇볕을 쬐며 산책하는 것을 추천드려요."
        elif stress_avg >= 3.0:
            feedback_message = f"🤔 **주의 단계!** 평균 {stress_avg:.1f}점으로 스트레스 관리가 필요해요. 따뜻한 차나 좋아하는 음악으로 15분간 휴식을 취해 보세요."
        else:
            feedback_message = f"🥳 **안정적!** 평균 {stress_avg:.1f}점으로 잘 관리하고 계세요! 이 좋은 상태를 유지하기 위해 다음 주 목표를 세워보는 건 어떨까요?"
            
    context = {
        'feedback_message': feedback_message,
        'stress_avg': stress_avg,
    }
    return render(request, 'survey/feedback.html', context)
    if not recent_surveys.exists():
        feedback_message = "아직 일주일치 데이터가 부족해요! 매일매일 기분을 기록해 주세요."
        stress_avg = 0
    else:
        averages = recent_surveys.aggregate(
            avg_stress=Avg('stress_score')
        )
        stress_avg = averages['avg_stress']
        if stress_avg >= 4.0:
            feedback_message = f"🚨 **스트레스 비상!** 평균 {stress_avg:.1f}점으로 매우 높습니다. 잠깐이라도 밖에서 햇볕을 쬐며 산책하는 것을 추천드려요."
        elif stress_avg >= 3.0:
            feedback_message = f"🤔 **주의 단계!** 평균 {stress_avg:.1f}점으로 스트레스 관리가 필요해요. 따뜻한 차나 좋아하는 음악으로 15분간 휴식을 취해 보세요."
        else:
            feedback_message = f"🥳 **안정적!** 평균 {stress_avg:.1f}점으로 잘 관리하고 계세요! 이 좋은 상태를 유지하기 위해 다음 주 목표를 세워보는 건 어떨까요?"
    context = {
        'feedback_message': feedback_message,
        'stress_avg': stress_avg,
    }
    return render(request, 'survey/feedback.html', context)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login') 
            
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'survey/signup.html', {'form': form})