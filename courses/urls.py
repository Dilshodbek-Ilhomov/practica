from django.urls import path
from .views import (
    CourseListCreateGenericAPIView,
    CourseDetailGenericAPIView
)

urlpatterns = [
    path(
        '',
        CourseListCreateGenericAPIView.as_view(),
        name='course-list-create'
    ),

    path(
        '<int:pk>/',
        CourseDetailGenericAPIView.as_view(),
        name='course-detail'
    ),
]