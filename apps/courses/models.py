from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import uuid

class Course(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(_('description'))
    thumbnail = models.ImageField(_('thumbnail'), upload_to='courses/thumbnails/', blank=True, null=True)
    instructor = models.CharField(_('instructor'), max_length=255)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(_('status'), max_length=20, choices=[('draft', 'Brouillon'), ('published', 'Publié')], default='draft')
    featured = models.BooleanField(_('featured'), default=False)
    difficulty = models.CharField(_('difficulty'), max_length=50, blank=True)
    estimated_duration = models.CharField(_('estimated duration'), max_length=50, blank=True)
    seo_title = models.CharField(_('SEO title'), max_length=255, blank=True)
    seo_description = models.TextField(_('SEO description'), blank=True)

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(_('title'), max_length=255)
    order = models.PositiveIntegerField(_('order'), default=0)

    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    video_id = models.CharField(_('video ID'), max_length=255, blank=True, help_text=_("ID from Bunny Stream or Mux"))
    duration = models.PositiveIntegerField(_('duration'), help_text=_("Duration in seconds"), default=0)
    order = models.PositiveIntegerField(_('order'), default=0)
    free_preview = models.BooleanField(_('free preview'), default=False)

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')
        ordering = ['order']

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(_('status'), max_length=20, choices=[('active', 'Actif'), ('completed', 'Terminé'), ('cancelled', 'Annulé')], default='active')
    progress = models.PositiveIntegerField(_('progress'), default=0)

    class Meta:
        unique_together = ('user', 'course')

class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    completed = models.BooleanField(default=False)
    watched_duration = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'lesson')
