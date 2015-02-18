from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

# Create your views here.
from website.forms import ContactForm, CommentForm
from website.models import Contact, Post, Comment


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about/about.html')

# renders any about/name profile pages
def profile(request, name):
    return render(request, 'about/' + name + '.html')

def aop(request):
    return render(request, 'areas-of-practice.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    tags = post.tags.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            body = form.cleaned_data['body']
            Comment.objects.create(first_name=first, last_name=last, body=body, post=post)
            return redirect('/blog')
    else:
        form = CommentForm()
    comments = Comment.objects.all()
    data = {"post": post, "comment_form": form, "comments": comments, "tags": tags}
    return render(request, 'view_post.html', data)

def faq(request):
    return render(request, 'faq.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = ContactForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you, {}, for requesting a free consultation'.format(user.first_name)
            html_content = '<h2>{}, thanks for requesting a free consultation!</h2> ' \
                           '<div>One of our attorneys will connect with you shortly</div>'.format(user.first_name)
            msg = EmailMultiAlternatives("{}'s Request with South Natick Law".format(user.first_name), text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            request.session['contact_info'] = request.POST
            # After saving, redirect the user to the confirmation page
            return redirect("thanks.html")

    # Else if the user is looking at the form page
    else:
        form = ContactForm()

    contacts = Contact.objects.all()
    data = {'form': form,
            'contacts': contacts
    }
    return render(request, "contact.html", data)

def thanks(request):
    contact_info = request.session.get('contact_info')
    return render(request, 'thanks.html', {'contact_info':contact_info})