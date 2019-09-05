from django.urls import path
from . import views

urlpatterns = [
    path('message',views.Message.as_view()),
]
