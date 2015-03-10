from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.views import indexView
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', indexView.as_view()),
    # url(r'^$', 'blog.views.index', name='index'),
    # url(r'^sirius/', include('sirius.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
