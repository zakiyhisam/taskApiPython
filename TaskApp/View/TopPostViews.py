from django.http import HttpResponse
import json
from TaskApp.Model.CommentModel import CommentModel
from TaskApp.Model.PostModel import PostModel
from TaskApp.Model.topPostModel import TopPostModel
from TaskApp.Handler.dataHandler import mapData
from TaskApp.Handler.endpointRequest import *
from django.shortcuts import render
def topPost(request):
    comments = fetchComment()
    allPost = fetchAllPost()
    
    commentList = mapData(comments, CommentModel)
    postList = mapData(allPost, PostModel)

    topPostList = []
    for post in postList:
        id = post.postId
        commentCount = 0
        for comment in commentList:
            if comment.postId == id:
                commentCount += 1
        topPost = TopPostModel(post_id = id, post_title = post.title, post_body = post.body, total_number_of_comments= commentCount)
        topPostList.append(topPost)
        
    sortedPost = sorted(topPostList, key=lambda x: x.total_number_of_comments, reverse= True)        
    response = []
    for topPost in sortedPost:
        dictPost = topPost.toJson()
        response.append(dictPost)
    data = json.dumps(response)
    return HttpResponse(data)