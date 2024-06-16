from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'news', NewsViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view({'post': 'register'}), name='user-register'),
    path('', include(router.urls)),
]