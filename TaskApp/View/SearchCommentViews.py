import json
from django.http import HttpResponse
from TaskApp.Model.CommentModel import CommentModel
from TaskApp.Handler.dataHandler import *
from TaskApp.Handler.endpointRequest import fetchComment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
#from django.views.decorators.csrf import csrf_protect

# Create your views here.
#@csrf_protect
@csrf_exempt 
def searchComment(r):
    if r.method == 'POST':
        possIdField = "postId"
        commentIdField = "commentId"
        nameField = "name"
        emailField = "email"
        bodyField = "body"
        body_unicode = r.body.decode('utf-8')
        body = json.loads(body_unicode)
        postIdRequest = body[possIdField] if possIdField in body else None
        commentIdRequest = body[commentIdField] if commentIdField in body else None
        nameRequest = body[nameField] if nameField in body else None
        emailRequest = body[emailField] if emailField in body else None
        bodyRequest = body[bodyField] if bodyField in body else None
        comments = fetchComment()
        commentList = mapData(comments, CommentModel)
        commentList = filterData(commentList, possIdField, postIdRequest)
        commentList = filterData(commentList, commentIdField, commentIdRequest)
        commentList = filterData(commentList, nameField, nameRequest)
        commentList = filterData(commentList, emailField, emailRequest)
        commentList = filterData(commentList, bodyField, bodyRequest)
        response = []
        for comment in commentList:
            dictPost = comment.toJson()
            response.append(dictPost)
        data = json.dumps(response)
        return HttpResponse(data)
    