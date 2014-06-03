from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'progress.views.index', name='index'),
    url(r'^login/', 'progress.views.login', name='login'),
    url(r'^logout/', 'progress.views.logout', name='logout'),
    url(r'^register/', 'progress.views.register', name='register'),
    url(r'^result/', 'progress.views.result', name='result'),
)
