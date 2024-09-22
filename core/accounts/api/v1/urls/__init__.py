from django.urls import include, path

from .profiles import urlpatterns as p_urlpatterns
from .accounts import urlpatterns as a_urlpatterns


app_name = "api-v1"


urlpatterns = [
    path("", include(p_urlpatterns)),
    path("", include(a_urlpatterns)),
]
