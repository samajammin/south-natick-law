__author__ = 'samrichards'

from django.contrib.syndication.views import Feed
from models import Post

class LatestPosts(Feed):
    title = 'South Natick Law Blog'
    link = '/feed'
    description = "Latest Posts From South Natick Law"

    def items(self):
         return Post.objects.published()[:5]
