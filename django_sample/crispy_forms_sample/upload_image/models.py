from django.db import models
from django.utils import timezone

class Image(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    # image_id = models.AutoField(primary_key=True)
    image_id = models.IntegerField()
    image_path = models.FileField(upload_to='./', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ""

#todo:postは一瞬で動いたので、filefieldかどっかの項目がうまく使えてない

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image_id = models.IntegerField()
    image_path = models.FileField(upload_to='./', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
