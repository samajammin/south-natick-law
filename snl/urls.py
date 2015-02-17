from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),
    url(r'^about$', 'website.views.about', name='about'),

    # catch name as a parameter & pass into view for url assignment
    url(r'^about/(?P<name>\w+)', 'website.views.profile', name='profile'),
    # url(r'^about/james', 'website.views.james', name='james'),
    # url(r'^about/richard', 'website.views.richard', name='richard'),
    # url(r'^about/caren', 'website.views.caren', name='caren'),
    # url(r'^about/george', 'website.views.george', name='george'),

    url(r'^areas-of-practice', 'website.views.aop', name='aop'),
    url(r'^testimonials$', 'website.views.testimonials', name='testimonials'),
    url(r'^faq$', 'website.views.faq', name='faq'),

    # logic to match specific resources posts first
    url(r'^blog$', 'website.views.blog', name='blog'),
    url(r'^blog/(?P<post_id>\w+)/$', 'website.views.view_post', name='view_post'),

    # url(r'^about$', 'website.views.about', name='about'),
    # url(r'^resources/', include('resources.urls')),
    url(r'^contact', 'website.views.contact', name='contact'),
    url(r'^thanks', 'website.views.thanks', name='thanks'),

    # url(r'form/$', 'website.views.comment_view', name='comment_view'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)