from django.urls import path
from . import views

urlpatterns = [
    path('message',views.Message.as_view()),
    path('keyboard',views.Keyboard.as_view())
]