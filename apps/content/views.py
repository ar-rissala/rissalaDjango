from django.views.generic import ListView, DetailView
from django.utils.translation import get_language
from .models import Content

class ContentListView(ListView):
    model = Content
    template_name = 'content/content_list.html'
    context_object_name = 'contents'
    content_type_filter = None
    page_title = ""
    page_description = ""
    
    def get_queryset(self):
        qs = Content.objects.filter(status='published', language=get_language())
        if self.content_type_filter:
            qs = qs.filter(content_type=self.content_type_filter)
        return qs
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_description'] = self.page_description
        return context

class NewsListView(ListView):
    model = Content
    template_name = 'content/news/news_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def get_queryset(self):
        qs = Content.objects.filter(status='published', content_type='news', language=get_language()).order_by('-published_at')
        featured_qs = list(qs.filter(is_featured=True)[:2])
        if len(featured_qs) < 2:
            needed = 2 - len(featured_qs)
            excluded_ids = [a.id for a in featured_qs]
            recent = list(qs.exclude(id__in=excluded_ids)[:needed])
            featured_qs.extend(recent)
        featured_ids = [a.id for a in featured_qs]
        return qs.exclude(id__in=featured_ids).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Content.objects.filter(status='published', content_type='news', language=get_language()).order_by('-published_at')
        featured_qs = list(qs.filter(is_featured=True)[:2])
        if len(featured_qs) < 2:
            needed = 2 - len(featured_qs)
            excluded_ids = [a.id for a in featured_qs]
            recent = list(qs.exclude(id__in=excluded_ids)[:needed])
            featured_qs.extend(recent)
        context['featured_articles'] = featured_qs
        return context

class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content_obj'
    
    def get_template_names(self):
        if self.object.content_type == 'news':
            return ['content/news/news_detail.html']
        return ['content/content_detail.html']
    
    def get_queryset(self):
        return Content.objects.filter(status='published', language=get_language())
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.content_type == 'news':
            context['similar_articles'] = Content.objects.filter(
                status='published', 
                content_type='news',
                language=get_language()
            ).exclude(id=self.object.id).order_by('-published_at')[:3]
        return context
