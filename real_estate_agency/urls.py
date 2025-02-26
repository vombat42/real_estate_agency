from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.defaults import page_not_found


# from realtor.views import index


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('captcha/', include('captcha.urls')),
    re_path(r'^chaining/', include('smart_selects.urls')),
    # path('', index, name='home'),
    path('', include('realtor.urls', namespace='realtor')),
    path('users/', include('modules.system.urls', namespace='system')),
]

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
if DEBUG:
    # add debug toolbar only for DEBUG mode
    # urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

    # for show media files in DEBUG mode
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


# handler404 = page_not_found
handler403 = 'modules.system.views.my_handler403'
handler404 = 'modules.system.views.my_handler404'
handler500 = 'modules.system.views.my_handler500'

# Настройка админ панели
admin.site.site_header = 'Панель администрирования сайта'
admin.site.index_title = 'Риэлтор'