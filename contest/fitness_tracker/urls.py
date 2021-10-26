from django.urls import path
from fitness_tracker.views import *

urlpatterns = [
    path('accounts/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('activity/create/', ActivityCreateAPIView.as_view()),
    path('activity/list/', ActivityListAPIView.as_view())
]