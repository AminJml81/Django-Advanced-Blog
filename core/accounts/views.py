from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page


import requests


def test_cache1_view(request):
    url = "https://7935fcc4-7613-4507-a61b-5b881d266180.mock.pstmn.io/test/cache/"
    data = cache.get_or_set(
        'test_cache',
        lambda: requests.get(url).json(),
        timeout=300
    )
    return JsonResponse(data)

@cache_page(300)
def test_cache2_view(request):
    url = "https://7935fcc4-7613-4507-a61b-5b881d266180.mock.pstmn.io/test/cache/"
    response = requests.get(url)
    return JsonResponse(response.json())