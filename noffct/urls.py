from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noffct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^blog/$',views.blogview, name='blog'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^events/$', views.event_view, name='events')
)
