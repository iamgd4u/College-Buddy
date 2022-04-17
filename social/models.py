from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    content = models.TextField()
    image = models.ImageField(blank = True)

    def __str__(self):
        return str(self.content)

class Friends(models.Model):
    person1 = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "person1")
    person2 = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "person2")

    def __str__(self):
        return str("%s-%s" %(self.person1, self.person2))

class Like(models.Model):
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return str("%s likes %s" %(self.user, self.post.content))

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 200)
    def __str__(self):
        return str(self.content)

