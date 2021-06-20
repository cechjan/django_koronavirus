from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

import koronavirus


urlpatterns = [
    path('admin/', admin.site.urls),
    path('koronavirus/', include('koronavirus.urls')),
    path('', RedirectView.as_view(url='koronavirus/')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'koronavirus.views.error_404'
handler500 = 'koronavirus.views.error_500'
handler403 = 'koronavirus.views.error_403'
handler400 = 'koronavirus.views.error_400'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
    urlpatterns += [re_path(r'^500/$', koronavirus.views.error_500)]
    urlpatterns += [re_path(r'^400/$', koronavirus.views.error_400)]
    urlpatterns += [re_path(r'^404/$', koronavirus.views.error_404)]
    urlpatterns += [re_path(r'^403/$', koronavirus.views.error_403)]
