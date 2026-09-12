from modeltranslation.translator import register, TranslationOptions
from .models import Course, Module, Lesson

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description', 'difficulty', 'estimated_duration', 'seo_title', 'seo_description')

@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
