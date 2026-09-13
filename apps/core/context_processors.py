from django.conf import settings
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def umami_analytics(request):
    """
    Expose Umami settings to templates.
    Disable tracking in admin interface.
    """
    if request.path.startswith('/admin/'):
        return {'UMAMI_ENABLED': False}

    return {
        'UMAMI_ENABLED': env.bool('UMAMI_ENABLED', default=False),
        'UMAMI_WEBSITE_ID': env.str('UMAMI_WEBSITE_ID', default=''),
        'UMAMI_SCRIPT_URL': env.str('UMAMI_SCRIPT_URL', default=''),
    }
