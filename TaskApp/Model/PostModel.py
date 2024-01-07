from django.db import models
class PostModel(models.Model):
    userId = models.IntegerField()
    postId = models.IntegerField()
    title = models.CharField()
    body = models.CharField()
    
    @classmethod
    def create_from_j(cls, post): 
        post = cls(userId= post['userId'], postId = post['id'], title=post['title'], body=post['body'])
        return post