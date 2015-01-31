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
    return render(request, "view_post.html", data)

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

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/")

    # Else if the user is looking at the form page
    else:
        form = ContactForm()

    contacts = Contact.objects.all()

    data = {'form': form,
            'contacts': contacts
    }
    return render(request, "contact.html", data)