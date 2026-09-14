from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Course, Module, Lesson, Enrollment, LessonProgress

class LessonInline(TranslationTabularInline):
    model = Lesson
    extra = 1

class ModuleInline(TranslationTabularInline):
    model = Module
    extra = 1

@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ('title', 'instructor', 'status', 'price', 'featured')
    list_filter = ('status', 'featured')
    search_fields = ('title', 'instructor', 'description')
    prepopulated_fields = {'slug_en': ('title_en',), 'slug_ar': ('title_ar',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(TranslationAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    list_display = ('title', 'module', 'duration', 'order', 'free_preview')
    list_filter = ('free_preview', 'module__course')
    search_fields = ('title', 'description', 'video_id')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'progress', 'enrolled_at')
    list_filter = ('status', 'course')
    search_fields = ('user__email', 'course__title')

@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'watched_duration', 'completed_at')
    list_filter = ('completed', 'lesson__module__course')
    search_fields = ('user__email', 'lesson__title')
