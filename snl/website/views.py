from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from website.forms import ContactForm, CommentForm
from website.models import Contact, Post, Comment, PracticeArea, Attorney


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about/about.html')

# renders any about/name profile pages
def profile(request, slug):
    attorney = get_object_or_404(Attorney, slug = slug)
    return render(request, 'about/' + attorney.slug + '.html')

def aop(request):
    return render(request, 'areas-of-practice.html')

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3) # number of posts to show per page
    tags = PracticeArea.objects.all()
    authors = Attorney.objects.all()
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': posts, 'tags': tags, 'authors': authors})

def tag_index(request, slug):
    tag = get_object_or_404(PracticeArea, slug = slug)
    post_list = Post.objects.filter(tags = tag)
    paginator = Paginator(post_list, 3) # number of posts to show per page
    tags = PracticeArea.objects.all()
    authors = Attorney.objects.all()

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': posts, 'tags': tags, 'authors': authors, 'tag': tag})

def author_index(request, slug):
    author = get_object_or_404(Attorney, slug = slug)
    post_list = Post.objects.filter(author = author)
    paginator = Paginator(post_list, 3) # number of posts to show per page
    tags = PracticeArea.objects.all()
    authors = Attorney.objects.all()

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': posts, 'tags': tags, 'authors': authors, 'author': author})

def view_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    post_tags = post.tags.all()
    tags = PracticeArea.objects.all()
    authors = Attorney.objects.all()
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
    data = {"post": post, "comment_form": form, "comments": comments, "tags": tags, "post_tags": post_tags, "authors": authors}
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