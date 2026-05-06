from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView

urlpatterns = [
    path('', CourseListCreateAPIView.as_view()),
    path('<int:pk>/', CourseDetailAPIView.as_view())
]