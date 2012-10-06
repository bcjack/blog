from django.conf.urls.defaults import patterns, include, url
from miniblog.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
	url(r'^$',main_page),
	url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'login_page.html'}),
	url(r'^register/$',register),
	url(r'^content/(?P<blog_id>.+)/$',content),
	url(r'^reply/(?P<blog_id>.+)/$',reply),
	url(r'^style/(?P<style_id>.+)/$',style),
	url(r'^public/$',public),
	url(r'^logout/$',logout_page),
	url(r'^add_style/$',add_style),
)

