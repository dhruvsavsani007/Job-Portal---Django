from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", MyLogin, name="login"),
    path("jobs/", addjob, name="jobs"),
    path("reg/", Registration, name="reg"),
    path("view/", stream, name="view"),
    path('logout/', mylogout, name='logout'),
    path('profile/<str:id>', profile, name="profile"),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
