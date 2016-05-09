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
    url(r'^about/$', 'website.views.about', name='about'),
    url(r'^about/caren-schindel', 'website.views.caren', name='caren'),
    url(r'^about/erin-nihill', 'website.views.erin', name='erin'),
    url(r'^about/george-richards', 'website.views.george', name='george'),
    url(r'^about/james-mclaughlin', 'website.views.james', name='james'),
    url(r'^about/leah-kaine', 'website.views.leah', name='leah'),
    url(r'^about/richard-biller', 'website.views.richard', name='richard'),
    url(r'^about/(?P<slug>\S+)$', 'website.views.profile', name='profile'),
    url(r'^areas-of-practice$', 'website.views.aop', name='aop'),

    # todo content for FAQs and testimonials
    # url(r'^testimonials$', 'website.views.testimonials', name='testimonials'),
    # url(r'^faq$', 'website.views.faq', name='faq'),

    # logic to match specific resources posts first
    url(r'^blog$', 'website.views.blog', name='blog'),
    url(r'^blog/$', 'website.views.blog', name='blog'),
    url(r'^blog/author/(?P<slug>\S+)$', 'website.views.author_index', name='author_index'),
    url(r'^blog/tag/(?P<slug>\S+)$', 'website.views.tag_index', name='tag_index'),
    url(r'^blog/(?P<slug>\S+)$', 'website.views.view_post', name='view_post'),

    # url(r'^resources/', include('resources.urls')),
    url(r'^contact$', 'website.views.contact', name='contact'),
    url(r'^thanks$', 'website.views.thanks', name='thanks'),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^markdown/', include('django_markdown.urls')),
    # url(r'^base$', TemplateView.as_view(template_name='new-base.html'), name="base"),
    # url(r'^base-cta$', TemplateView.as_view(template_name='new-base-cta.html'), name="base-cta"),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt'), name="robots"),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml'), name="sitemap"),
)

# for dev environment to resolve "Exception Value:	Empty static prefix not permitted"
# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
