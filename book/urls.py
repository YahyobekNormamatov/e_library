from django.urls import path
from .views import (AllCreateBookView,RUDBookrView)
urlpatterns = [
    path('', AllCreateBookView.as_view()),
    path('<pk>', RUDBookrView.as_view()),
]