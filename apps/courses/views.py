from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        qs = Course.objects.filter(status='published').exclude(slug__exact='').order_by('-id')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) | 
                Q(instructor__icontains=q)
            )
        return qs

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    
    def get_queryset(self):
        return Course.objects.filter(status='published').prefetch_related('modules__lessons')
