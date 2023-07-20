from django.urls import path
from .views import PersonView, PersonDetailView

urlpatterns = [
    path('person/', UserView.as_view()),
    path('person/<pk>/', UserDetailView.as_view()),
]