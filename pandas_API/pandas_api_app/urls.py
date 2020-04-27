from django.urls import path
from .views  import CovidView

urlpatterns = [
    path('covid/', CovidView.as_view()),

]