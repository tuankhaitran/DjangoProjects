from django.db import models

from django.utils import timezone
from django.urls import reverse
# Create your models here.

# Blog post class
class Post(models.Model):
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)


    # Method to set the published_date or publish the post
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    #
    def filter_approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title


# Comment Class
class Comment(models.Model):
    
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # Approve a comment
    def approve(self):
        self.approved_comment = True
        self.save()

    #Once you create the model it tells where the website should go to
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text