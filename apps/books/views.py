from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils.translation import get_language
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        qs = Book.objects.filter(status='published', language=get_language()).order_by('order', '-publication_date')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(title__icontains=q) | 
                Q(author__icontains=q)
            )
        return qs

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    
    def get_queryset(self):
        return Book.objects.filter(status='published', language=get_language())
