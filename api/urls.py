from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import signup, LessonView, TeacherView


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('timetable/teacher/', TeacherView.as_view(), name='teacher'),
    path('timatable/', LessonView.as_view(), name='schedule'),
]
