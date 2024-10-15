from django.urls import path, include

from accounts.views import test_cache1_view, test_cache2_view
app_name = "accounts"


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("test/cache/v1/", test_cache1_view, name='test-cache-v1'),
    path("test/cache/v2/", test_cache2_view, name='test-cache-v2'),
    path("api/v1/", include("accounts.api.v1.urls")),
]
