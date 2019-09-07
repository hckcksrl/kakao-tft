from django.urls import path
from . import views

urlpatterns = [
    path('tft',views.TFT.as_view()),
]
