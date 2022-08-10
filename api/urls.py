from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import signup, LessonView, ProfessorView


urlpatterns = [
    path('v1/signup/', signup, name='signup'),
    path('v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/timetable/teacher/', TeacherView.as_view(), name='teacher'),
    path('v1/timatable/', LessonView.as_view(), name='schedule'),
]
