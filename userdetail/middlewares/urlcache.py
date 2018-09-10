from userdetail import settings
from django.core.cache import cache
from django.http.response import HttpResponse

class UrlCache():
    def __init__(self, get_response):
        self.get_response = self.get_response
        self.urls = settings.CACHE_URL
    
    def __call__(self, request):
        req_url = request.path
        req_url_set = self.url_cache_config(req_url)
        if req_url_set:
            page_in_cache = cache.get(req_url)
            if page_in_cache:
                return HttpResponse.write(page_in_cache)
            else:
                response = self.get_response(request)
                cache.set(req_url, response, req_url_set[1])
                return response
        else:
            response = self.get_response(request)
            return response

    
    def url_cache_config(self, url):
      for urlconfig  in self.urls:
        if urlconfig[0] == url:
            return urlconfig
        else:
            return Null
    