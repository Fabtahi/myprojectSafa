from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
from .permissions import IsTeacher
from .serializers import *


class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsTeacher]
        return super().get_permissions()


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        if course_id:
            course = Course.objects.get(pk=course_id)
            if course.teacher != self.request.user:
                raise PermissionDenied("You are not authorized to create assignments for this course.")
            serializer.save()

    def perform_update(self, serializer):
        instance = self.get_object()
        course = instance.course
        if course.teacher != self.request.user:
            raise PermissionDenied("You are not authorized to update assignments for this course.")
        serializer.save()


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        if course_id:
            course = Course.objects.get(pk=course_id)
            if course.teacher != self.request.user:
                raise PermissionDenied("You are not authorized to create news for this course.")
            serializer.save()

    def perform_update(self, serializer):
        instance = self.get_object()
        course = instance.course
        if course.teacher != self.request.user:
            raise PermissionDenied("You are not authorized to update news for this course.")
        serializer.save()


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
