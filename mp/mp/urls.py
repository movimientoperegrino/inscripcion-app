from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # View URLs
    #url(r'^fobi/', include('fobi.urls.view')),

    # Edit URLs
    #url(r'^fobi/', include('fobi.urls.edit')),
)
