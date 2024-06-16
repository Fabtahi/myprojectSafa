from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='content')
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignment')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title


class News(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='submissions/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.student.username} for {self.assignment.title}"
