from django.db import models
from rest_framework import serializers
class CommentModel(models.Model):
    postId = models.IntegerField()
    commentId = models.IntegerField()
    name = models.CharField()
    email = models.CharField()
    body = models.CharField()
    
    @classmethod
    def create_from_j(cls, comment): 
        comment = cls(postId= comment['postId'], commentId = comment['id'], name=comment['name'], email=comment['email'], body = comment['body'])
        return comment
    def toJson(self):
        return {
            "postId": self.postId,
            "Id": self.commentId,
            "name": self.name,
            "email": self.email,
            "body": self.body
	}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        Model = CommentModel
        fields = ('postId', 'id', 'name', 'email', 'body')