from django.urls import path
from .views import (
    EnrollmentListCreateGenericAPIView,
    EnrollmentDetailGenericAPIView
)

urlpatterns = [
    path(
        '',
        EnrollmentListCreateGenericAPIView.as_view(),
        name='enrollment-list-create'
    ),

    path(
        '<int:pk>/',
        EnrollmentDetailGenericAPIView.as_view(),
        name='enrollment-detail'
    ),
]