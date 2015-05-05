from django.contrib import admin

# Register your models here.
from django.contrib import admin
from website.models import Firm, Attorney, Post, PracticeArea, Contact, Comment
from django_markdown.admin import MarkdownModelAdmin

class PostInLine(admin.TabularInline):
    model = Post

class FirmAdmin(admin.ModelAdmin):
    fields = ('name', 'llp', 'email', 'phone_number', 'street_address', 'city', 'zipcode', 'state', 'domain')
    list_display = ('name', 'llp', 'email', 'phone_number', 'street_address', 'city', 'zipcode', 'state', 'domain')

class AttorneyAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'title', 'email', 'phone_number', 'phone_extension', 'firm')
    list_display = ('first_name', 'last_name', 'title', 'email', 'phone_number', 'phone_extension')
    inlines = [PostInLine, ]

class PostAdmin(MarkdownModelAdmin):
    fields = (('title', 'author'), 'tags', 'body', 'image', 'image_alt_text')
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'published_date', 'body', 'image', 'image_alt_text')
    # list_filter = ('author', 'tags')
    # filter_horizontal = ('tags',)

class PracticeAreaAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'attorneys')
    list_display = ('name', 'description')
    filter_horizontal = ('attorneys',)

class ContactAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'practice_area', 'description')
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'creation_date', 'description')

class CommentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'body', 'post')
    list_display = ('first_name', 'last_name', 'body', 'post')


admin.site.register(Attorney, AttorneyAdmin)
# not positive this PostAdmin is right..
# https://github.com/klen/django_markdown
# admin.site.register(Post, MarkdownModelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PracticeArea, PracticeAreaAdmin)
admin.site.register(Firm, FirmAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)