from django.contrib import admin
from .models import UserProfile, Category, Course, Content, Assignment, News, Enrollment, Submission


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher')
    search_fields = ('user__username', 'is_teacher')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'teacher', 'is_public')
    search_fields = ('name', 'category__name', 'teacher__username')
    list_filter = ('is_public', 'category')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video', 'file')
    search_fields = ('title', 'course__name')
    list_filter = ('course',)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date')
    search_fields = ('title', 'course__name')
    list_filter = ('course', 'due_date')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__name')
    list_filter = ('course',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    search_fields = ('student__username', 'course__name')
    list_filter = ('course',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('assignment', 'submitted_at')
