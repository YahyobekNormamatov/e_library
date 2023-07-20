from django.urls import path
from .views import (AllCreateAuthorView, RUDAuthorView)

urlpatterns = [
    path('', AllCreateAuthorView.as_view()),
    path('<pk>', RUDAuthorView.as_view())
]

