from django import forms
from django.forms import ModelForm
from website.models import Contact, Comment, Attorney

__author__ = 'samrichards'

# todo phone number validation... limit to 10 integers

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        # first_name = forms
        # fields = ['first_name', 'last_name', 'email', 'phone_number', 'practice_area', 'description']
        exclude = ['description']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['points', 'post']

#     Non-model version...
# class CommentForm(forms.Form):
#     author = forms.ModelChoiceField(queryset=Attorney.objects.all())
#     comment_body = forms.CharField()