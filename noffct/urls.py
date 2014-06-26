from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from blog import views
from noffct import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noffct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^blog/$',views.blogview, name='blog'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^events/$', views.event_view, name='events'),
    url(r'^event/(?P<event_id>[0-9]+)/$',views.event_detail, name='event_detail'),
    url(r'^media/$', views.media_view, name='media')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
