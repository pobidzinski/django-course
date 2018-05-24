from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User')     # link author to core authentication User table
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())     # as a defult we set current date from timezone func.
    published_date = models.DateTimeField(blank=True, null=True)    # can be blank or null

    # any method inside class should take self
    def publish(self):
        self.published_date = timezone.now()    # set attribute published_date (for now)
        self.save()     # save changes in model

    def approve_comments(self):
        return self.comments.filer(approved_comment=True)      # return comments that are approved (linked comments)

    def get_absolute_url(self):     # set absolute URL (must be this name) -> show where to redirect when Post is created
        return reverse('post_detail', kwargs={'pk' : self.pk})      # return to post_details page with pk args from object pk

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')       # link comment to Post (set related name)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')         # return to list so not needed to provide primary key

    def __str__(self):
        return self.text


