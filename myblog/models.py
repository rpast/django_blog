from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    """
    Post object details
    :author: only registered users
    :published_date: initially blank and may be zero
    """
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    title = models.CharField(max_length=400)
    text = models.TextField(max_length=100000)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Post publish method. Sets the publication date
        and saves changes to the model
        """
        self.published_date = timezone.now()
        self.save()

    def get_approved_comments(self):
        """
        Approve all the comments linked to post.
        :return: filter all the comments and change their attribute to True.
        """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        """
        What should happen after I create a post?
        :return: show me detailed post view, identify post by its primary key
        """
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

        post.comments.count

class Comment(models.Model):
    """
    Similar object to Post. Every comment is initially not approved.
    """
    post = models.ForeignKey('myblog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        '''
        What should happen after I create a post?
        :return: show me the home page (list of the posts)
        '''
        return reverse('post_list')

    def __str__(self):
        return self.text