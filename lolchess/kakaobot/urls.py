from django.urls import path
from . import views

urlpatterns = [
    path('rank',views.Rank.as_view()),
    path('tft',views.TFT.as_view())
]
