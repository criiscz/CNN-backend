from django.urls import path, include

from ic_api import Prediction

urlpatterns = [
    path('predict/<slug:filename>', Prediction.as_view(), name='prediction'),
]
