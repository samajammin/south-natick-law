from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=120)
    llp = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    street_address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    domain = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.name)

class Attorney(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.BigIntegerField(default=5086511000)
    phone_extension = models.SmallIntegerField()
    firm = models.ForeignKey(Firm, related_name='attorneys')
    # image = models.ImageField(upload_to='author_images', blank=True, null=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

# categories for blog post tags, attorney practice areas & contact form topic inqueries
class PracticeArea(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    # posts = models.ManyToManyField(Post, related_name='practice_areas')
    attorneys = models.ManyToManyField(Attorney, related_name='practice_areas')

    def __unicode__(self):
        return u"{}".format(self.name)

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Attorney, related_name='posts')
    publish_date = models.DateField(auto_now_add="True")
    tags = models.ManyToManyField(PracticeArea, related_name='posts')

    def make_blurb(self):
        return self.body[:150] + "..."

    def __unicode__(self):
        return u"{}".format(self.title)

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.BigIntegerField(null=True)
    creation_date = models.DateField(null=True, auto_now_add=True)
    practice_area = models.ForeignKey(PracticeArea, related_name='contacts')
    description = models.TextField(blank=True)
    def __unicode__(self):
        return u"{}".format(self.email)

class Comment(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    body = models.TextField()
    submission_date = models.DateField(null=True, auto_now_add=True)
    points = models.SmallIntegerField(default=0)
    post = models.ForeignKey(Post, related_name='comments')

    def upvote(self):
        self.points -= 1
        return self.points

    def downvote(self):
        self.points += 1
        return self.points

    def __unicode__(self):
        return u"{} {} {}".format(self.id, self.first_name, self.last_name)

    # published_date = models.DateField(auto_now_add="True")

# todo testimonials class for users to submit testimonials (must be admin approved before adding to site)
        # will be exact same as comments...

# todo FAQs class for users to submit FAQs (must be admin approved before adding to site)
        # will be exact same as comments...
# todo FAQs... scrape quora questions to answer questions about legal issues