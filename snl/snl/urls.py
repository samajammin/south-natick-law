from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

# added for markdown
# from django_markdown import flatpages
# admin.autodiscover()
# flatpages.register()
from django.views.generic import TemplateView
# from snl.website import feed

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^about$', 'website.views.about', name='about'),

    # catch name as a parameter & pass into view for url assignment
    url(r'^about/(?P<slug>\S+)$', 'website.views.profile', name='profile'),
    # url(r'^about/james', 'website.views.james', name='james'),
    # url(r'^about/richard', 'website.views.richard', name='richard'),
    # url(r'^about/caren', 'website.views.caren', name='caren'),
    # url(r'^about/george', 'website.views.george', name='george'),

    url(r'^areas-of-practice$', 'website.views.aop', name='aop'),

    # todo content for FAQs and testimonials
    # url(r'^testimonials$', 'website.views.testimonials', name='testimonials'),
    # url(r'^faq$', 'website.views.faq', name='faq'),

    # logic to match specific resources posts first
    url(r'^blog$', 'website.views.blog', name='blog'),
    # url(r'^blog/(?P<post_id>\w+)/$', 'website.views.view_post', name='view_post'),

    url(r'^blog/author/(?P<slug>\S+)$', 'website.views.author_index', name='author_index'),
    url(r'^blog/tag/(?P<slug>\S+)$', 'website.views.tag_index', name='tag_index'),
    url(r'^blog/(?P<slug>\S+)$', 'website.views.view_post', name='view_post'),

    # url(r'^about$', 'website.views.about', name='about'),
    # url(r'^resources/', include('resources.urls')),
    url(r'^contact$', 'website.views.contact', name='contact'),
    url(r'^thanks$', 'website.views.thanks', name='thanks'),

    # url(r'form/$', 'website.views.comment_view', name='comment_view'),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt'), name="robots"),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml'), name="sitemap"),
)

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)