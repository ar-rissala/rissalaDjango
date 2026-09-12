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
