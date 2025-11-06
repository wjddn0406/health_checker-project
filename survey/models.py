from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SCORE_CHOICES = [
    (1, '1점 (매우높음/편함/잘됨)'), 
    (2, '2점'), 
    (3, '3점 (보통)'), 
    (4, '4점'), 
    (5, '5점 (매우낮음/불편/안됨)')
]
class UserSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey_date = models.DateField(auto_now_add=True)
    stress_score = models.IntegerField(
        verbose_name='1. 오늘의 전반적인 스트레스 수준',
        choices=SCORE_CHOICES,
        default=3
    )
    energy_level = models.IntegerField(
        verbose_name='2. 오늘 에너지 수준',
        choices=SCORE_CHOICES,
        default=3
    )
    emotion_intensity = models.IntegerField(
        verbose_name='3. 오늘 느낀 긍정적 감정의 강도',
        choices=SCORE_CHOICES,
        default=3
    )
    relationship_discomfort_score = models.IntegerField(
        verbose_name='4. 관계에서의 불편함 수준',
        choices=SCORE_CHOICES,
        default=1 
    )
    self_care_satisfaction = models.IntegerField(
        verbose_name='5. 나를 위해 한 행동에 대한 만족도',
        choices=SCORE_CHOICES,
        default=3
    )
    focus_level = models.IntegerField(
        verbose_name='6. 오늘 집중이 잘 된 정도',
        choices=SCORE_CHOICES,
        default=3
    )
    goal_achievement = models.IntegerField(
        verbose_name='7. 오늘 목표 달성 정도',
        choices=SCORE_CHOICES,
        default=3
    )
    stress_score = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], 
        default=3
    )
    def __str__(self):
        return f"{self.user.username} - {self.survey_date}"