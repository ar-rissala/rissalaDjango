from django.conf import settings
import abc

class VideoProvider(abc.ABC):
    @abc.abstractmethod
    def get_video_url(self, video_id: str) -> str:
        pass
        
    @abc.abstractmethod
    def get_thumbnail_url(self, video_id: str) -> str:
        pass

class BunnyStreamProvider(VideoProvider):
    def __init__(self):
        self.api_key = getattr(settings, 'BUNNY_API_KEY', '')
        self.library_id = getattr(settings, 'BUNNY_LIBRARY_ID', '')
        
    def get_video_url(self, video_id: str) -> str:
        # Example implementation for Bunny Stream
        # Ideally returns a signed URL or iframe embed URL
        return f"https://iframe.mediadelivery.net/embed/{self.library_id}/{video_id}"
        
    def get_thumbnail_url(self, video_id: str) -> str:
        return f"https://vz-{self.library_id}.b-cdn.net/{video_id}/thumbnail.jpg"

class MuxProvider(VideoProvider):
    def __init__(self):
        self.token_id = getattr(settings, 'MUX_TOKEN_ID', '')
        self.token_secret = getattr(settings, 'MUX_TOKEN_SECRET', '')
        
    def get_video_url(self, video_id: str) -> str:
        return f"https://stream.mux.com/{video_id}.m3u8"
        
    def get_thumbnail_url(self, video_id: str) -> str:
        return f"https://image.mux.com/{video_id}/thumbnail.jpg"

def get_video_provider() -> VideoProvider:
    # Factory to return active provider
    return BunnyStreamProvider()
