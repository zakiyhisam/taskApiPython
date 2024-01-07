import requests

commentsEndpoint = "https://jsonplaceholder.typicode.com/comments"
allPostsEndpoint = "https://jsonplaceholder.typicode.com/posts"

def invokeEndpoint(endPoint):
    response = requests.get(endPoint)
    return response.json()

def fetchComment():
    return invokeEndpoint(commentsEndpoint)

def fetchAllPost():
    return invokeEndpoint(allPostsEndpoint)