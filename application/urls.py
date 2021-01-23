from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/space/', include('apps.space.urls')),
]





def trigger_error(request):
    division_by_zero = 1 / 0  # noqa
    return request

urlpatterns += [
    path('api/v1/sentry-debug/', trigger_error),
]
