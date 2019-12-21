from django.contrib import admin
from django.conf.urls import include, url

api_endpoint_view = [
    # url(r'^(?P<version>(v1))/', include(example_urls)),
    ]

urlpatterns = [
    url('admin/', admin.site.urls),
    # url(r'^api/', include(api_endpoint_view)),
]
