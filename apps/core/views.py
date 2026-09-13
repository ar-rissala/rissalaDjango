from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/home.html'

class AboutView(TemplateView):
    template_name = 'core/legal/about.html'

class LegalView(TemplateView):
    template_name = 'core/legal/legal.html'

class PrivacyView(TemplateView):
    template_name = 'core/legal/privacy.html'

class TermsView(TemplateView):
    template_name = 'core/legal/terms.html'

def indexnow_view(request, key):
    import os
    from django.http import HttpResponse, Http404
    expected_key = os.getenv('INDEXNOW_KEY')
    if expected_key and key == expected_key:
        return HttpResponse(expected_key, content_type="text/plain")
    raise Http404("IndexNow key not found or mismatched.")
