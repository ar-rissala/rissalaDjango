import os
import django
import sys
import time

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from apps.books.models import Book
from apps.content.models import Content
from apps.courses.models import Course, Module, Lesson
from googletrans import Translator

def translate_db():
    print("Translating DB content...")
    translator = Translator()
    
    # Translate Books
    for book in Book.objects.all():
        print(f"Translating Book: {book.title}")
        try:
            if book.title:
                book.title = translator.translate(book.title, src='fr', dest='en').text
            if book.short_description:
                book.short_description = translator.translate(book.short_description, src='fr', dest='en').text
            if book.long_description:
                book.long_description = translator.translate(book.long_description, src='fr', dest='en').text
            book.save()
            time.sleep(1)
        except Exception as e:
            print(f"Error translating book {book.id}: {e}")

    # Translate Content
    for content in Content.objects.all():
        print(f"Translating Content: {content.title}")
        try:
            if content.title:
                content.title = translator.translate(content.title, src='fr', dest='en').text
            if content.excerpt:
                content.excerpt = translator.translate(content.excerpt, src='fr', dest='en').text
            if content.content:
                content.content = translator.translate(content.content, src='fr', dest='en').text
            content.save()
            time.sleep(1)
        except Exception as e:
            print(f"Error translating content {content.id}: {e}")
            
    # Translate Courses
    for course in Course.objects.all():
        print(f"Translating Course: {course.title}")
        try:
            if course.title:
                course.title = translator.translate(course.title, src='fr', dest='en').text
            if course.description:
                course.description = translator.translate(course.description, src='fr', dest='en').text
            course.save()
            time.sleep(1)
        except Exception as e:
            print(f"Error translating course {course.id}: {e}")

    print("Finished DB translation.")

if __name__ == "__main__":
    translate_db()
